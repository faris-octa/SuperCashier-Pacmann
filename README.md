# SuperCashier-Pacmann
## Self-service cashier system build with Python

Aplikasi ini adalah sebuah program kasir sederhana yang dibuat menggunakan bahasa pemrograman Python. Program ini menggunakan database SQLite untuk menyimpan data transaksi. Program ini memiliki beberapa fitur dasar seperti memasukkan barang ke dalam keranjang belanja, mengubah barang yang sudah ada di dalam keranjang belanja, mengeluarkan barang dari keranjang belanja, menampilkan keranjang belanja, dan melakukan proses checkout. 

Berikut alur kerja program:

![flowchart](https://user-images.githubusercontent.com/31800666/230698352-521cbe01-4d0f-4d72-8401-0ca41750711a.png)

## Persyaratan & library

- Python 3.7
- Pandas
- SQLite3
- Tabulate


## Cara Menggunakan

1. Jalankan main.py

2. Pilih fungsi yang ingin dieksekusi:
- Masukkan barang ke keranjang belanja
- Update barang di keranjang belanja
- Keluarkan barang dari keranjang belanja
- Check keranjang belanja
- Checkout / Keluar

3. Jika memilih pilihan 1, akan diminta untuk memasukkan nama barang, jumlah, dan harga per item yang ingin dimasukkan ke keranjang.

4. Jika memilih pilihan 2, akan diminta untuk memasukkan nama barang yang ingin diubah dan kemudian memilih opsi apa yang ingin diubah: nama barang, jumlah barang, atau harga barang.

5. Jika memilih pilihan 3, akan diminta untuk memilih opsi apa yang ingin dilakukan: mengeluarkan satu barang atau mengosongkan keranjang belanja.

6. Jika memilih pilihan 4, akan menampilkan status keranjang belanja saat ini.

7. Jika memilih pilihan 5, program akan mengakumulasi seluruh barang di dalam keranjang belanja, menghitung diskon yang dikenakan, dan menampilkan total nilai belanja. Data transaksi akan disimpan ke dalam database SQLite3 dengan nama database.db.

## Kontribusi

Jika ingin berkontribusi pada program kasir E-Mart, silakan ikuti panduan berikut:

1. Fork repository ini
2. Buat branch baru (`git checkout -b feature/feature-baru`)
3. Commit perubahan yang dilakukan (`git commit -m 'Menambahkan fitur baru'`)
4. Push ke branch tersebut (`git push origin feature/feature-baru`)
5. Buat pull request
