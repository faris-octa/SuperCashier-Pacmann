import pandas as pd
import sqlite3

# create a connection to database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS transaction
#                 (nama_item TEXT,
#                 jumlah_item INT,
#                 harga_item INT)''')

#### dummy databases ####
df = pd.DataFrame({'trnsct_id': [1, 2]})

# dummy inventory
inventory = ['gula', 'minyak goreng', 'beras']

##########################


class Transaction:
    # constructor buat dataframe kosong sebagai keranjang belanja
    def __init__(self):
        self.cart = pd.DataFrame(columns=['Nama Item', 'Jumlah Item', 'Harga/Item', 'Harga Total'])
        print("\nSelamat datang di e-Mart")

    #### add item feature ####
    def add_item(self):
        nama_item = input('Nama Item: ')
        jumlah_item = int(input('Jumlah: '))
        harga_per_item = int(input('Harga: '))
        harga_total = jumlah_item * harga_per_item
        new_item = pd.DataFrame({
                                'Nama Item': [nama_item],
                                'Jumlah Item': [jumlah_item],
                                'Harga/Item': [harga_per_item],
                                'Harga Total': [harga_total]
                                })
        self.cart = pd.concat([self.cart, new_item], ignore_index=True)
        print(f"\nBerhasil memasukkan {nama_item} seharga Rp. {harga_per_item} sebanyak {jumlah_item} buah ke keranjang...")
        return self.cart
    ##########################

    #### update item features ####
    def update_item_name(self, nama_item, nama_item_updated):
        # cari baris dengan item yang diinginkan
        updated_row = self.cart['Nama Item'] == nama_item
        # ganti nilai nama item menjadi nama item yang baru
        self.cart.loc[updated_row, 'Nama Item'] = nama_item_updated
        print(f"\nItem {nama_item} telah diupdate menjadi {nama_item_updated}")
        return self.cart

    def update_item_qty(self, nama_item, qty_item_updated):
        # cari baris berdasarkan nama item
        updated_row = self.cart['Nama Item'] == nama_item
        # ubah jumlah itemnya
        self.cart.loc[updated_row, 'Jumlah Item'] = qty_item_updated
        # update harga total
        self.cart.loc[updated_row, 'Harga Total'] = qty_item_updated * self.cart.loc[updated_row, 'Harga/Item']
        print(f"\nJumlah Item {nama_item} telah diupdate menjadi {qty_item_updated} buah")
        return self.cart

    def update_item_price(self, nama_item, price_item_updated):
        # cari baris yang diinginkan
        updated_row = self.cart['Nama Item'] == nama_item
        # update harganya
        self.cart.loc[updated_row, 'Harga/Item'] = price_item_updated
        self.cart.loc[updated_row, 'Harga Total'] = price_item_updated * self.cart.loc[updated_row, 'Jumlah Item']
        print(f"\nHarga Item {nama_item} telah diupdate menjadi Rp. {price_item_updated}")
        return self.cart
    ##############################

    #### delete item feature ####
    def delete_item(self, nama_item):
        deleted_item = self.cart.loc[self.cart['Nama Item'] == nama_item]
        self.cart.drop(deleted_item.index, inplace=True)
        print(f"\nBerhasil mengeluarkan {nama_item} dari keranjang belanja...")
        return self.cart
    #############################

    #### empty cart feature ####
    def reset_transaction(self):
        self.cart = self.cart.iloc[0:0]
        return self.cart
    #############################

    #### check order feature ####
    def check_order(self):
        # iterasi setiap nama barang if not in inventory -> execute
        for item in self.cart:
            if item not in inventory:
                print('Terdapat kesalahan input data')
                break
            else:
                print('Pemesanan sudah benar')
        print(self.cart) #total harga 
    #############################

    #### checkout feature ####
    def check_out():
        pass

# commit and close database
conn.commit()
conn.close()    

# test1 = Transaction()
# test1.add_item()
# test1.update_item_name('tepung', 'tepung terigu')
# test1.update_item_qty('tepung terigu', 200)
# test1.update_item_price('tepung terigu', 10000000000)
# #test1.delete_item('tepung terigu')
# test1.reset_transaction()

if __name__ == "__main__":
    trnsct_123 = Transaction()

    while True:
        if trnsct_123.cart.empty:
            print("\nkeranjang belanja anda kosong, mari berbelanja!")

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
            nama_item = input('Nama barang yang ingin diubah: ')
            if nama_item not in trnsct_123.cart['Nama Item'].to_list():
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
            pass
            print("\nPilih opsi:")
            print("1. Keluarkan satu barang")
            print("2. Kosongkan keranjang belanja")
            choice_remove = input("Masukkan pilihan anda (1 or 2): ")
            if choice_remove == "1":
                nama_item = input('Nama barang yang ingin dikeluarkan: ')
                if nama_item in trnsct_123.cart['Nama Item'].to_list():
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
        print(trnsct_123.cart['Nama Item'].to_list())

        # if choice == '1':
        #     amount = float(input("Masukkan jumlah yang ingin disetor: "))
        #     t.deposit(amount)
        #     print("Setor tunai sebesar ${} berhasil dilakukan.".format(amount))
        # elif choice == '2':
        #     amount = float(input("Masukkan jumlah yang ingin ditarik: "))
        #     t.withdraw(amount)
        #     print("Tarik tunai sebesar ${} berhasil dilakukan.".format(amount))
        # elif choice == '3':
        #     t.show_balance()
        # elif choice == '4':
        #     break
        # else:
        #     print("Pilihan tidak valid. Silahkan pilih angka 1, 2, 3, atau 4.")

    print("Terima kasih telah menggunakan layanan kami.")