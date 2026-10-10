kode_barang = "" # BRG + 3 digit angka
nomor_urut = 1
nama_barang = ""
kategori = ""
harga = 0
stok = 0
data_barang = []

while True:
    print("\n=== SELAMAT DATANG DI MANAJEMEN BARANG ===")
    print("1. Tambah Barang")
    print("2. Lihat Barang")
    print("3. Ubah Barang")
    print("4. Hapus Barang")
    print("5. Print Barang")
    print("6. Keluar Program")
    pilih = input("Masukkan Pilihan (1-5): ")

    match pilih:
        case "1": # Tambah Barang

            print("\n== Silahkan Masukkan Data Berikut ==")
            while True: 
                # kode barang
                nomor_urut += 0
                kode_barang = (f"BRG{nomor_urut:03d}")

                # Nama Barang
                input_nama = input("Nama Barang: ")
                check_nama = input_nama.replace(" ", "")

                if 5 <= len(check_nama) <= 60 and check_nama.isalnum():
                    nama_barang = input_nama.strip().title()
                    break
                print("== Input tidak valid ==")

            while True: # Kategori Barang
                input_kategori = input("Kategori Barang [keyboard | Mouse | Aksesoris | Audio | Kamera | Monitor | Penyimpanan]: ")

                match input_kategori.lower():
                    case "keyboard":
                        kategori = "Keyboard"
                        break
                    case "mouse":
                        kategori = "Mouse"
                        break
                    case "aksesoris":
                        kategori = "Aksesoris"
                        break
                    case "audio":
                        kategori = "Audio"
                        break
                    case "kamera":
                        kategori = "Kamera"
                        break
                    case "monitor":
                        kategori = "Monitor"
                        break
                    case "penyimpanan":
                        kategori = "Penyimpanan"
                        break
                    case _:
                        print("== Input tidak valid ==")

            while True: # Harga
                input_harga = input("Harga: ")
                check_harga = input_harga.replace(".", "").replace(",", "")

                if input_harga.isdigit():
                    harga = check_harga.strip()
                    break
                print("== Input tidak valid ==")

            while True: # Stok
                    input_stok = input("Stok: ").strip()
    
                    if input_stok.isdigit():
                        stok = input_stok
                        break
                    print("== Input tidak valid ==")

            # menambahkan barang kedalam list
            barang_baru = [kode_barang,
                           nama_barang,
                           kategori,
                           harga,
                           stok]
            data_barang.append(barang_baru)
            print("Data berhasil ditambahkan")
            input("PENCET ENTER UNTUK LANJUT...")

# ========= LIST BARANG 
        case "2": 
            if data_barang == []:
                print("== data kosong ==")    
            else:
                print("\n=== LIST BARANG ===")
                print("=" * 150)

                print(f"{'No':<5}| {'Kode Barang':<30}| {'Nama Barang':<30}| {'Kategori':<20}| {'harga':<20}| {'Stok':<10}")
                print("=" * 150)
                
                nomor_urut = 1
                for barang in data_barang:
                    print(f"{nomor_urut:<5}| {barang[0]:<30}| {barang[1]:<30}| {barang[2]:<20}| {barang[3]:<20}| {barang[4]:<10}")
                    nomor_urut += 1

                print("=" * 150)
                input("PENCET ENTER UNTUK LANJUT...")

# ========= UBAH BARANG 
        case "3": 
            if data_barang == []:
                print("== data kosong ==")
            else:
                print("=" * 150)
                
                print(f"{'No':<5}| {'Kode Barang':<30}| {'Nama Barang':<30}| {'Kategori':<20}| {'harga':<20}| {'Stok':<10}")
                print("=" * 150)
                
                nomor_urut = 1
                for barang in data_barang:
                    print(f"{nomor_urut:<5}| {barang[0]:<30}| {barang[1]:<30}| {barang[2]:<20}| {barang[3]:<20}| {barang[4]:<10}")
                    nomor_urut += 1

                print("=" * 150)
                
                print("\n=== UBAH BARANG ===")
                pilih = input("Masukkan Nomor Barang:")

                if pilih.strip().isdigit():
                    index_target = int(pilih) - 1

                    print("== Silahkan Masukkan Data Berikut ==")

                    while True:
                        # Nama Barang
                        ubah_nama = input("Nama Barang: ")
                        check_nama = ubah_nama.replace(" ", "")
        
                        if 5 <= len(check_nama) <= 60 and check_nama.isalnum():
                            nama_barang = ubah_nama.strip().title()
                            break
                        print("== Input tidak valid ==")

                    while True: # Kategori Barang
                        ubah_kategori = input("Kategori Barang [keyboard | Mouse | Aksesoris | Audio | Kamera | Monitor | Penyimpanan]: ")
        
                        match ubah_kategori.lower():
                            case "keyboard":
                                kategori = "Keyboard"
                                break
                            case "mouse":
                                kategori = "Mouse"
                                break
                            case "aksesoris":
                                kategori = "Aksesoris"
                                break
                            case "audio":
                                kategori = "Audio"
                                break
                            case "kamera":
                                kategori = "Kamera"
                                break
                            case "monitor":
                                kategori = "Monitor"
                                break
                            case "penyimpanan":
                                kategori = "Penyimpanan"
                                break
                            case _:
                                print("== Input tidak valid ==")

                    while True: # Harga
                        ubah_harga = input("Harga: ")
                        check_harga = ubah_harga.replace(".", "").replace(",", "")
        
                        if ubah_harga.isdigit():
                            harga = check_harga.strip()
                            break
                        print("== Input tidak valid ==")
        
                    while True: # Stok
                            ubah_stok = input("Stok: ").strip()
            
                            if ubah_stok.isdigit():
                                stok = ubah_stok
                                break
                            print("== Input tidak valid ==")

                    # Memasukkan edit data barang ke dalam list
                    data_barang[index_target] = [kode_barang, ubah_nama, ubah_kategori, ubah_harga, ubah_stok]
                    print("Data berhasil diubah")
                    input("PENCET ENTER UNTUK LANJUT...")
                else:
                    print("== Input tidak valid ==")




# 1. tambahin dibagian insert harga harus punya 000
# 2. format harga belum diubah jadi 30.000