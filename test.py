import pandas as pd
import sqlite3

# dummy inventory
inventory = ['gula', 'minyak goreng', 'beras']

# insert data to database func.
def insert_to_table(source_data, data):
    # create a connection to database
    try:
        conn = sqlite3.connect(source_data)
        print('berhasil konek')
    except sqlite3.Error as error:
        print('gagal konek:', error)
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
    
    # GET no_id -> no_id terakhir + 1
    cursor.execute('SELECT MAX(no_id) FROM transactions')
    no_id = cursor.fetchone()[0] + 1

    # assign column no_id dengan value = no_id
    data = pd.concat([pd.Series(no_id, index=data.index, name='no_id'), data], axis=1)
    print(data)
    data.to_sql('transactions', con=conn, if_exists='append', index=False)

    conn.commit()  
    conn.close()
    print('koneksi ditutup') 




##########################

class Transaction:
    # constructor buat dataframe kosong sebagai keranjang belanja
    def __init__(self):      
        self.cart = pd.DataFrame(columns=['nama_item', 'jumlah_item', 'harga', 'total_harga'])
        print("\n------------Selamat datang di e-Mart------------")

    #### add item feature ####
    def add_item(self):
        nama_item = input('nama_item: ')
        jumlah_item = int(input('Jumlah: '))
        harga_per_item = int(input('Harga: '))
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
        # iterasi setiap nama barang if not in inventory -> execute
        # for item in self.cart['nama_item'].to_list():
        #     if item not in inventory:
        #         print('------------Terdapat kesalahan input data------------')
        #         break
        #     else:
        #         print('------------Pesanan sudah benar------------')
        
        if all(item in inventory for item in list(self.cart['nama_item'])):
            print('------------Pesanan sudah benar------------')
        else:
            print('------------Terdapat kesalahan input data------------')

        index = list(range(1, len(self.cart)+1))
        print(self.cart.set_index(pd.Series(index)))
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

        print(f'\nTotal nilai belanjaan: {total}')
        insert_to_table(source_data='database.db', data=receipt)
        return total

 

if __name__ == "__main__":
    trnsct_123 = Transaction()

    while True:
        if trnsct_123.cart.empty:
            print("\nkeranjang belanja anda masih kosong, mari berbelanja!")

        print("\nPilih fungsi yang ingin dieksekusi:")
        print("1. Masukkan barang ke keranjang belanja")
        print("2. Update barang di keranjang belanja")
        print("3. Keluarkan barang dari keranjang belanja")
        print("4. Check keranjang belanja")
        print("5. Checkout / Keluar")

        choice = input("Masukkan pilihan anda (1/2/3/4/5): ")
        if choice == '5':
            break

        elif choice == '1':
            print(trnsct_123.add_item())

        elif choice == '2':
            nama_item = input('Nama barang yang ingin diubah: ').lower()
            if nama_item not in trnsct_123.cart['nama_item'].to_list():
                print(f"\nTidak ada {nama_item} di keranjang")
            else:
                print("\nApa yang ingin diupdate:")
                print("1. Nama Barang")
                print("2. Jumlah Barang")
                print("3. Harga Barang")
                choice_update = input("Masukkan pilihan anda (1/2/3): ")
                if choice_update == "1":
                    updated_item = input(f'{nama_item} diubah menjadi: ')
                    trnsct_123.update_item_name(nama_item, updated_item)
                elif choice_update == "2":
                    updated_item_qty = int(input(f"jumlah barang {nama_item} diubah menjadi: "))
                    trnsct_123.update_item_qty(nama_item, updated_item_qty)
                elif choice_update == '3':
                    updated_item_price = int(input(f"harga barang {nama_item} diubah menjadi: "))
                    trnsct_123.update_item_price(nama_item, updated_item_price)
                else:
                    print("Pilihan tidak valid")

        elif choice == '3':
            print("\nPilih opsi:")
            print("1. Keluarkan satu barang")
            print("2. Kosongkan keranjang belanja")
            choice_remove = input("Masukkan pilihan anda (1 or 2): ")
            if choice_remove == "1":
                nama_item = input('Nama barang yang ingin dikeluarkan: ').lower()
                if nama_item in trnsct_123.cart['nama_item'].to_list():
                    trnsct_123.delete_item(nama_item)
                else:
                    print(f"\nTidak ada item {nama_item} di keranjang")
            elif choice_remove == '2':
                trnsct_123.reset_transaction()
            else:
                print("Pilihan tidak valid")


        elif choice == '4':
            if trnsct_123.cart.empty:
                continue
            else:
                trnsct_123.check_order()

        elif choice == '6':
            trnsct_123.check_out()

        else:
            print("Pilihan tidak valid. Silahkan pilih angka 1, 2, 3, 4 atau 5")
        

    
    print("Terima kasih telah menggunakan layanan kami.")
    