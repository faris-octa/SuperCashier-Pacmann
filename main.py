import transaction

if __name__ == "__main__":
    trnsct_123 = transaction.Transaction()

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