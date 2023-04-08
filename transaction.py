#### for transactions modules
import pandas as pd
from tabulate import tabulate

class Transaction:
    # constructor buat dataframe kosong sebagai keranjang belanja
    def __init__(self):
        """"
        Konstruktor inisiasi setiap pemanggilan objek transaksi

        args: None
        return: cart (dataframe)
        """      
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
        inventory = ['Gula', 'Minyak Goreng', 'Beras',
                     'Ayam Goreng', 'Pasta Gigi',
                     'Mainan Mobil', 'Mi instan']
        
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
        receipt['diskon'] = 0
        receipt.loc[receipt['total_harga'] > 200_000, 'diskon'] = receipt['total_harga'] * 0.05
        receipt.loc[receipt['total_harga'] > 300_000, 'diskon'] = receipt['total_harga'] * 0.06
        receipt.loc[receipt['total_harga'] > 500_000, 'diskon'] = receipt['total_harga'] * 0.07

        receipt['harga_diskon'] = receipt['total_harga'] - receipt['diskon']
        total = receipt['harga_diskon'].sum()

        print(f'\n------------Total nilai belanja sebesar: Rp. {total}------------')
        return receipt