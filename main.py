import pandas as pd


#### dummy databases ####
df = pd.DataFrame({'trnsct_id': [1, 2]})

class Transaction:
    # constructor buat id transaksi = +1 dari last id
    def __init__(self):
        self.trnsct_id = df['trnsct_id'].iloc[-1] + 1

    def perkenalan(self):
        print(f'Nomor transaksi sekarang: {self.trnsct_id}')

    # add item
    def add_item(nama_item, jumlah_item, harga_per_item):
        nama_item = input('Nama Item: ')
        jumlah_item = int(input('Jumlah: '))
        harga_per_item = int(input('Harga: '))

    

    

test1 = Transaction()
test1.perkenalan()