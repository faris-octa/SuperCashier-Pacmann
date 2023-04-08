#### for transactions modules
import pandas as pd
import sqlite3
from tabulate import tabulate

# insert data to database func.
def insert_to_table(source_data, data):
    """
    Fungsi untuk mengimport daftar suatu transaksi ke database sqlite

    args:
            - source_data (str): nama database sqlite
            - data (dataframe): dataframe transaksi

    return: None
    """
    # create a connection to database
    try:
        conn = sqlite3.connect(source_data)
    except sqlite3.Error as error:
        print('Gagal terkoneksi dengan database:', error)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions 
                    (no_id INT, 
                    nama_item TEXT, 
                    jumlah_item INT, 
                    harga INT, 
                    total_harga INT, 
                    Diskon INT, 
                    harga_Diskon INT
                    )''')
    
    # GET no_id -> no_id terakhir di database + 1
    cursor.execute('SELECT MAX(no_id) FROM transactions')
    no_id = cursor.fetchone()[0] + 1

    # ASSIGN kolom no_id
    data = pd.concat([pd.Series(no_id, index=data.index, name='no_id'), data], axis=1)
    # print(data) <-- for debugging
    data.to_sql('transactions', con=conn, if_exists='append', index=False)

    conn.commit()  
    conn.close()

class Transaction:
    # constructor buat dataframe kosong sebagai keranjang belanja
    def __init__(self):      
        self.cart = pd.DataFrame(columns=['nama_item', 'jumlah_item', 'harga', 'total_harga'])
        print("\n------------Selamat datang di e-Mart------------")

    #### add item feature ####
    def add_item(self, nama_item, jumlah_item, harga_per_item):
        harga_total = jumlah_item * harga_per_item
        new_item = pd.DataFrame({
                                'nama_item': [nama_item],
                                'jumlah_item': [jumlah_item],
                                'harga': [harga_per_item],
                                'total_harga': [harga_total]
                                })
        self.cart = pd.concat([self.cart, new_item], ignore_index=True)
        print(f"\n------------Berhasil memasukkan {nama_item} seharga Rp. {harga_per_item} sebanyak {jumlah_item} buah ke keranjang------------")
        return self.cart
    ##########################

    #### update item features ####
    def update_item_name(self, nama_item, nama_item_updated):
        # cari baris dengan item yang diinginkan
        updated_row = self.cart['nama_item'] == nama_item
        # ganti nilai nama_item menjadi nama_item yang baru
        self.cart.loc[updated_row, 'nama_item'] = nama_item_updated
        print(f"\n------------Item {nama_item} telah diupdate menjadi {nama_item_updated}------------")
        return self.cart

    def update_item_qty(self, nama_item, qty_item_updated):
        # cari baris berdasarkan nama_item
        updated_row = self.cart['nama_item'] == nama_item
        # ubah jumlah_itemnya
        self.cart.loc[updated_row, 'jumlah_item'] = qty_item_updated
        # update total_harga
        self.cart.loc[updated_row, 'total_harga'] = qty_item_updated * self.cart.loc[updated_row, 'harga']
        print(f"\n------------jumlah_item {nama_item} telah diupdate menjadi {qty_item_updated} buah------------")
        return self.cart

    def update_item_price(self, nama_item, price_item_updated):
        # cari baris yang diinginkan
        updated_row = self.cart['nama_item'] == nama_item
        # update harganya
        self.cart.loc[updated_row, 'harga'] = price_item_updated
        self.cart.loc[updated_row, 'total_harga'] = price_item_updated * self.cart.loc[updated_row, 'jumlah_item']
        print(f"\n------------Harga Item {nama_item} telah diupdate menjadi Rp. {price_item_updated}------------")
        return self.cart
    ##############################

    #### delete item feature ####
    def delete_item(self, nama_item):
        deleted_item = self.cart.loc[self.cart['nama_item'] == nama_item]
        self.cart.drop(deleted_item.index, inplace=True)
        print(f"\n------------Berhasil mengeluarkan {nama_item} dari keranjang belanja------------")
        return self.cart
    #############################

    #### empty cart feature ####
    def reset_transaction(self):
        self.cart = self.cart.iloc[0:0]
        return self.cart
    ############################

    #### check order feature ####
    def check_order(self):
        """
        Fungsi untuk menampilkan keranjang belanja saat ini

        args: None
        return: None
        """
        # iterasi setiap nama barang if not in inventory -> execute
        # dummy inventory
        inventory = ['gula', 'minyak goreng', 'beras']
        
        if all(item in inventory for item in list(self.cart['nama_item'])):
            print('------------Pesanan sudah benar------------')
        else:
            print('------------Terdapat kesalahan input data------------')

        index = list(range(1, len(self.cart)+1))
        cart = self.cart.set_index(pd.Series(index))
        header = ['Nama Item', 'Jumlah Item', 'Harga', 'Total Harga']
        print(tabulate(cart, headers= header, tablefmt='psql', numalign='center'))
    #############################

    #### checkout feature ####
    def check_out(self):
        # modifikasi cart agar strukturnya sesuai dengan database
        receipt = self.cart
        receipt['Diskon'] = 0
        receipt.loc[receipt['total_harga'] > 200_000, 'Diskon'] = receipt['total_harga'] * 0.05
        receipt.loc[receipt['total_harga'] > 300_000, 'Diskon'] = receipt['total_harga'] * 0.06
        receipt.loc[receipt['total_harga'] > 500_000, 'Diskon'] = receipt['total_harga'] * 0.07

        receipt['harga_Diskon'] = receipt['total_harga'] - receipt['Diskon']
        total = receipt['harga_Diskon'].sum()

        print(f'\n------------Total nilai belanjaan: Rp. {total}------------')
        insert_to_table(source_data='database.db', data=receipt)
        return total