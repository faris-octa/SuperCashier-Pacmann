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

3. Jika memilih pilihan 1, pengguna dapat memasukkan item yang ingin dimasukkan ke keranjang.
![input_item](https://user-images.githubusercontent.com/31800666/231710642-030e5600-edc7-4bd5-85f6-8c5a1be73c26.png)

4. Jika memilih pilihan 2, pengguna dapat mengubah barang di keranjang.
![update_item](https://user-images.githubusercontent.com/31800666/231711424-53a302b1-7b76-40eb-828a-f9beca0dc6d4.png)

5. Jika memilih pilihan 3, pengguna dapat mengeluarkan satu barang atau mengosongkan keranjang belanja.
![delete_item](https://user-images.githubusercontent.com/31800666/231711938-e865ed23-7c5a-4fd4-9be1-c545fb32fb70.png)

6. Jika memilih pilihan 4, akan menampilkan status keranjang belanja saat ini.
![check_order](https://user-images.githubusercontent.com/31800666/231712206-5fcc37c6-0d96-42fb-8bf0-7be9eee070f0.png)

7. Jika memilih pilihan 5, program akan mengakumulasi seluruh barang di dalam keranjang belanja, menghitung diskon yang dikenakan, dan menampilkan total nilai belanja. Data transaksi akan disimpan ke dalam database SQLite3 dengan nama database.db.
![check_out](https://user-images.githubusercontent.com/31800666/231713338-8b91c0df-08d7-4291-81a0-e5f083a96e1b.png)

## Kontribusi

Jika ingin berkontribusi pada program kasir E-Mart, silakan ikuti panduan berikut:

1. Fork repository ini
2. Buat branch baru (`git checkout -b feature/feature-baru`)
3. Commit perubahan yang dilakukan (`git commit -m 'Menambahkan fitur baru'`)
4. Push ke branch tersebut (`git push origin feature/feature-baru`)
5. Buat pull request
