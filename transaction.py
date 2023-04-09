"""
Modul transaction bertujuan sebagai sekumpulan fungsi utama proses transaksi digital.
Modul ini terdiri dari Class Transaction yang memiliki satu attributes inisiasi dan beberapa method.
"""

# import library
import pandas as pd
from tabulate import tabulate

class Transaction:
    # constructor cart -> dataframe
    def __init__(self):
        """"
        Konstruktor inisiasi yang melakukann pembuatan (cart) berupa dataframe kosong

        args: None
        return: 
            - cart (dataframe)
        """      
        self.cart = pd.DataFrame(columns=['nama_item', 'jumlah_item', 'harga', 'total_harga'])
        print("-"*55)
        print("SELAMAT DATANG DI E-MART")
        print("-"*55)

    def add_item(self, nama_item, jumlah_item, harga_per_item):
        """"
        Method yang berfungsi menambahkan item, jumlah, dan harga ke cart

        args: 
            - nama_item (str)
            - jumlah_item (int)
            - harga_per_item (float)
        return: 
            - cart (dataframe)
        """  
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
   
    def update_item_name(self, nama_item, nama_item_updated):
        """"
        Method yang berfungsi untuk melakukan update terhadap nama suatu item di dalam cart

        args: 
            - nama_item (str)
            - nama_item_updated (str)
        return: 
            - cart (dataframe)
        """
        # cari baris dengan item yang diinginkan
        updated_row = self.cart['nama_item'] == nama_item
        # ganti nilai nama_item menjadi nama_item yang baru
        self.cart.loc[updated_row, 'nama_item'] = nama_item_updated
        print(f"\n------------Item {nama_item} telah diupdate menjadi {nama_item_updated}------------")
        return self.cart

    def update_item_qty(self, nama_item, qty_item_updated):
        """"
        Method yang berfungsi untuk melakukan update terhadap kuantitas suatu item di dalam cart

        args: 
            - nama_item (str)
            - qty_item_updated (int)
        return: 
            - cart (dataframe)
        """
        # cari baris berdasarkan nama_item
        updated_row = self.cart['nama_item'] == nama_item
        # ubah jumlah_itemnya
        self.cart.loc[updated_row, 'jumlah_item'] = qty_item_updated
        # update total_harga
        self.cart.loc[updated_row, 'total_harga'] = qty_item_updated * self.cart.loc[updated_row, 'harga']
        print(f"\n------------jumlah_item {nama_item} telah diupdate menjadi {qty_item_updated} buah------------")
        return self.cart

    def update_item_price(self, nama_item, price_item_updated):
        """"
        Method yang berfungsi untuk melakukan update terhadap harga suatu item di dalam cart

        args: 
            - nama_item (str)
            - price_item_updated (int)
        return: 
            - cart (dataframe)
        """
        # cari baris yang diinginkan
        updated_row = self.cart['nama_item'] == nama_item
        # update harganya
        self.cart.loc[updated_row, 'harga'] = price_item_updated
        self.cart.loc[updated_row, 'total_harga'] = price_item_updated * self.cart.loc[updated_row, 'jumlah_item']
        print(f"\n------------Harga Item {nama_item} telah diupdate menjadi Rp. {price_item_updated}------------")
        return self.cart

    def delete_item(self, nama_item):
        """"
        Method yang berfungsi untuk melakukan penghapusan terhadap suatu item dari cart

        args: 
            - nama_item (str)
        return: 
            - cart (dataframe)
        """
        deleted_item = self.cart.loc[self.cart['nama_item'] == nama_item]
        self.cart.drop(deleted_item.index, inplace=True)
        print(f"\n------------Berhasil mengeluarkan {nama_item} dari keranjang belanja------------")
        return self.cart

    def reset_transaction(self):
        """"
        Method yang berfungsi untuk melakukan pengosongan cart

        args: 
            - None
        return: 
            - cart (dataframe)
        """
        self.cart = self.cart.iloc[0:0]
        return self.cart

    def check_order(self):
        """
        Fungsi untuk menampilkan status cart saat ini

        args: 
            - None
        return: 
            - None
        """
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

    def check_out(self):
        """"
        Method yang berfungsi untuk mengakumulasi seluruh belanjaan di dalam cart beserta diskon yang dikenakan

        args: 
            - None
        return: receipt (dataframe)
        """
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