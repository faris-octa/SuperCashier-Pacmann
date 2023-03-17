import pandas as pd


#### dummy databases ####
df = pd.DataFrame({'trnsct_id': [1, 2]})



##########################

class Transaction:
    # constructor buat dataframe kosong sebagai keranjang belanja
    def __init__(self):
        self.cart = pd.DataFrame(columns=['Nama Item', 'Jumlah Item', 'Harga/Item'])

    # add item
    def add_item(self):
        nama_item = input('Nama Item: ')
        jumlah_item = int(input('Jumlah: '))
        harga_per_item = int(input('Harga: '))
        new_item = {'Nama Item': nama_item,
                    'Jumlah Item': jumlah_item,
                    'Harga/Item': harga_per_item}
        self.cart = self.cart.append(new_item, ignore_index=True)
        print(f"Berhasil memasukkan {nama_item} seharga Rp. {harga_per_item} sebanyak {jumlah_item} buah ke keranjang")
        print(self.cart)

    # update item
    def update_item_name(self, nama_item, nama_item_updated):
        ### cari nama item di self.cart['Nama Item'] pake for trus ganti jadi nama_item_updated
        for item in self.cart['Nama Item']:
            if item == nama_item:
                self.cart.loc[self.cart['Nama Item'] == nama_item, 'Nama Item'] = nama_item_updated
        print(self.cart)



    

    

test1 = Transaction()
test1.add_item()
test1.add_item()
test1.update_item_name('tepung', 'tepung terigu')