import pandas as pd


#### dummy databases ####
df = pd.DataFrame({'trnsct_id': [1, 2]})



##########################

class Transaction:
    # constructor buat dataframe kosong sebagai keranjang belanja
    def __init__(self):
        self.cart = pd.DataFrame(columns=['Nama Item', 'Jumlah Item', 'Harga/Item'])
        print("")
        print("Selamat datang di e-Mart")
        print("Silakan masukkan barang belanja anda ke cart...")

    #### add item feature ####
    def add_item(self):
        nama_item = input('Nama Item: ')
        jumlah_item = int(input('Jumlah: '))
        harga_per_item = int(input('Harga: '))
        new_item = pd.DataFrame({'Nama Item': [nama_item],
                                 'Jumlah Item': [jumlah_item],
                                 'Harga/Item': [harga_per_item]})
        self.cart = pd.concat([self.cart, new_item], ignore_index=True)
        print(f"Berhasil memasukkan {nama_item} seharga Rp. {harga_per_item} sebanyak {jumlah_item} buah ke keranjang")
        print(self.cart)
        print("")
    ##########################

    #### update item features ####
    def update_item_name(self, nama_item, nama_item_updated):
        ### cari nama item di self.cart['Nama Item'] pake for trus ganti jadi nama_item_updated
        for item in self.cart['Nama Item']:
            if item == nama_item:
                self.cart.loc[self.cart['Nama Item'] == nama_item, 'Nama Item'] = nama_item_updated
        print(f"Item {nama_item} telah diupdate menjadi {nama_item_updated}")
        print(self.cart)
        print("")

    def update_item_qty(self, nama_item, qty_item_updated):
        for item in self.cart['Nama Item']:
            if item == nama_item:
                self.cart.loc[self.cart['Nama Item'] == nama_item, 'Jumlah Item'] = qty_item_updated
        print(f"Jumlah Item {nama_item} telah diupdate menjadi {qty_item_updated} buah")
        print(self.cart)
        print("")

    def update_item_price(self, nama_item, price_item_updated):
        for item in self.cart['Nama Item']:
            if item == nama_item:
                self.cart.loc[self.cart['Nama Item'] == nama_item, 'Harga/Item'] = price_item_updated
        print(f"Harga Item {nama_item} telah diupdate menjadi Rp. {price_item_updated}")
        print(self.cart)
        print("")
    ##############################

    


    

    

test1 = Transaction()
test1.add_item()
test1.update_item_name('tepung', 'tepung terigu')
test1.update_item_qty('tepung terigu', 200)
test1.update_item_price('tepung terigu', 10000000000)