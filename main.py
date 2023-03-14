import pandas as pd


#### dummy databases ####
df = pd.DataFrame({'trnsct_id': [1, 2]})

class Transaction:
    # constructor buat dataframe kosong sebagai keranjang belanja
    def __init__(self):
        self.cart = pd.DataFrame(columns=['Nama Item', 'Jumlah Item', 'Harga/Item'])

    def perkenalan(self):
        print(f'Nomor transaksi sekarang: {self.trnsct_id}')

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

        

    

    

test1 = Transaction()
test1.add_item()