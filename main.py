import os
from rich.console import Console
from rich.table import Table

console = Console()

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

car_list = [
    {
        "id": "M001",
        "brand": "Toyota",
        "model": "Avanza",
        "year": 2020,
        "license_plate": "B 1234 ABC",
        "daily_rate": 350000,
        "status": "available"
    },
    {
        "id": "M002",
        "brand": "Honda",
        "model": "Brio",
        "year": 2021,
        "license_plate": "B 5678 DEF",
        "daily_rate": 300000,
        "status": "available"
    },
    {
        "id": "M003",
        "brand": "Daihatsu",
        "model": "Xenia",
        "year": 2019,
        "license_plate": "B 9012 GHI",
        "daily_rate": 320000,
        "status": "rented"
    }
]

customer_list = [
    {
        "id_customer": "C001",
        "nama": "Budi Santoso",
        "no_ktp": "3171010101010001",
        "no_hp": "081234567890",
        "alamat": "Jakarta Selatan"
    },
    {
        "id_customer": "C002",
        "nama": "Andi Pratama",
        "no_ktp": "3171010202020002",
        "no_hp": "081298765432",
        "alamat": "Depok"
    },
    {
        "id_customer": "C003",
        "nama": "Siti Aminah",
        "no_ktp": "3171010303030003",
        "no_hp": "082112223333",
        "alamat": "Bekasi"
    }
]

def show_main_menu():
    print("=" * 50)
    print("SELAMAT DATANG DI SISTEM RENTAL MOBIL".center(50))
    print("=" * 50)
    print()
    print("================ MENU UTAMA ================")
    print("1. Kelola Data Mobil")
    print("2. Kelola Data Customer")
    print("3. Kelola Transaksi Rental")
    print("4. Pencarian dan Filter")
    print("5. Laporan")
    print("6. Keluar")
    print("============================================")

def show_submenu_1():
    print("=" * 50)
    print("KELOLA DATA MOBIL".center(50))
    print("=" * 50)
    print()
    print("1. Lihat Daftar Mobil")
    print("2. Tambah Mobil")
    print("3. Update Data Mobil")
    print("4. Hapus Data Mobil")
    print("5. Ubah Status Maintenance")
    print("6. Kembali ke Menu Utama")
    print("=" * 50)

def show_submenu_2():
    print("=" * 50)
    print("KELOLA DATA CUSTOMER".center(50))
    print("=" * 50)
    print()
    print("1. Lihat Daftar Customer")
    print("2. Tambah Customer")
    print("3. Update Data Customer")
    print("4. Hapus Data Customer")
    print("5. Kembali ke Menu Utama")
    print("=" * 50)

def input_required(message):
    while True:
        value = input(message).strip()

        if value != "":
            return value

        print("Input tidak boleh kosong. Silakan isi kembali.\n")

def input_number_required(message):
    while True:
        value = input(message).strip()

        if value == "":
            print("Input tidak boleh kosong. Silakan isi kembali.\n")
        elif not value.isdigit():
            print("Input harus berupa angka. Silakan coba lagi.\n")
        elif int(value) <= 0:
            print("Input harus lebih dari 0. Silakan coba lagi.\n")
        else:
            return int(value)

def input_main_menu():
    while True:
        selected_menu = input("Pilih menu: ")

        if selected_menu.isdigit():
            selected_menu = int(selected_menu)

            if selected_menu in range(1, 7):
                return selected_menu

        print("Menu yang dipilih tidak valid! Silakan pilih menu 1-6.")

# Function Helper Cars Menu
def show_car_list():
    table = Table(
        title="Daftar Mobil",
        show_header=True,
        header_style="bold magenta"
    )

    table.add_column("ID", style="dim", width=10)
    table.add_column("Merk")
    table.add_column("Model")
    table.add_column("Tahun", justify="center")
    table.add_column("Plat Nomor", justify="center")
    table.add_column("Harga Sewa /hari", justify="right")
    table.add_column("Status", justify="center")

    for car in car_list:
        if car["status"] == "available":
            status = "[green]Tersedia[/green]"
        elif car["status"] == "rented":
            status = "[yellow]Disewa[/yellow]"
        elif car["status"] == "maintenance":
            status = "[red]Maintenance[/red]"
        else:
            status = car["status"]

        table.add_row(
            car["id"],
            car["brand"],
            car["model"],
            str(car["year"]),
            car["license_plate"],
            f"Rp{car['daily_rate']:,}".replace(",", "."),
            status
        )

    console.print(table)

def generate_car_id():
    if len(car_list) == 0:
        return "M001"

    max_number = 0

    for car in car_list:
        number = int(car["id"][1:])

        if number > max_number:
            max_number = number

    new_number = max_number + 1

    return "M" + str(new_number).zfill(3)

def input_submenu_1():
    while True:
        selected_menu = input("Pilih menu: ")

        if selected_menu.isdigit():
            selected_menu = int(selected_menu)

            if selected_menu in range(1, 7):
                return selected_menu

        print("Menu yang dipilih tidak valid! Silakan pilih menu 1-6.")

def find_car_by_id(car_id):
    for car in car_list:
        if car["id"] == car_id:
            return car

    return None

# Function Helper Customer Menu
def show_customer_list():
    table = Table(
        title="Daftar Customer",
        show_header=True,
        header_style="bold magenta"
    )

    table.add_column("ID Customer", style="dim", width=12)
    table.add_column("Nama")
    table.add_column("No. KTP", justify="center")
    table.add_column("No. HP", justify="center")
    table.add_column("Alamat")

    for customer in customer_list:
        table.add_row(
            customer["id_customer"],
            customer["nama"],
            customer["no_ktp"],
            customer["no_hp"],
            customer["alamat"]
        )

    console.print(table)


def generate_customer_id():
    if len(customer_list) == 0:
        return "C001"

    max_number = 0

    for customer in customer_list:
        number = int(customer["id_customer"][1:])

        if number > max_number:
            max_number = number

    new_number = max_number + 1

    return "C" + str(new_number).zfill(3)


def input_submenu_2():
    while True:
        selected_menu = input("Pilih menu: ")

        if selected_menu.isdigit():
            selected_menu = int(selected_menu)

            if selected_menu in range(1, 6):
                return selected_menu

        print("Menu yang dipilih tidak valid! Silakan pilih menu 1-5.")


def find_customer_by_id(customer_id):
    for customer in customer_list:
        if customer["id_customer"] == customer_id:
            return customer

    return None

while True:
    clear_terminal()
    show_main_menu()

    selected_main_menu = input_main_menu()

    if selected_main_menu == 1:
        while True:
            clear_terminal()
            show_submenu_1()

            selected_submenu = input_submenu_1()

            if selected_submenu == 1:
                clear_terminal()
                show_car_list()
                input("Tekan Enter untuk kembali ke submenu...")

            elif selected_submenu == 2:
                clear_terminal()
                print("=" * 50)
                print("TAMBAH MOBIL".center(50))
                print("=" * 50)

                new_id = generate_car_id()
                print(f"ID Mobil: {new_id}")

                brand = input_required("Masukkan merk mobil: ")
                model = input_required("Masukkan model mobil: ")
                year = input_number_required("Masukkan tahun pembuatan: ")
                license_plate = input_required("Masukkan plat nomor: ").upper()
                daily_rate = input_number_required("Masukkan harga sewa /hari: ")

                car_list.append({
                    "id": new_id,
                    "brand": brand,
                    "model": model,
                    "year": year,
                    "license_plate": license_plate,
                    "daily_rate": daily_rate,
                    "status": "available"
                })

                print("\nData mobil berhasil ditambahkan!\n")
                show_car_list()

                input("Tekan Enter untuk kembali ke submenu...")

            elif selected_submenu == 3:
                clear_terminal()
                show_car_list()

                while True:
                    selected_id = input("Masukkan ID mobil yang ingin diubah: ").upper()
                    selected_car = find_car_by_id(selected_id)

                    if selected_car is not None:
                        break

                    print("ID mobil tidak ada. Silakan masukkan kembali.\n")

                clear_terminal()
                print("=" * 50)
                print("UPDATE DATA MOBIL".center(50))
                print("=" * 50)
                print(f"ID Mobil        : {selected_car['id']}")
                print(f"Merk            : {selected_car['brand']}")
                print(f"Model           : {selected_car['model']}")
                print(f"Tahun           : {selected_car['year']}")
                print(f"Plat Nomor      : {selected_car['license_plate']}")
                print(f"Harga Sewa/Hari : Rp{selected_car['daily_rate']:,}".replace(",", "."))
                print(f"Status          : {selected_car['status']}")
                print("=" * 50)
                print("Kosongkan input jika tidak ingin mengubah data.\n")

                new_brand = input("Masukkan merk baru: ").strip()
                new_model = input("Masukkan model baru: ").strip()

                while True:
                    new_year = input("Masukkan tahun baru: ").strip()

                    if new_year == "":
                        break

                    if new_year.isdigit() and int(new_year) > 0:
                        selected_car["year"] = int(new_year)
                        break

                    print("Tahun harus berupa angka lebih dari 0. Silakan coba lagi.\n")

                new_license_plate = input("Masukkan plat nomor baru: ").strip().upper()

                while True:
                    new_daily_rate = input("Masukkan harga sewa baru: ").strip()

                    if new_daily_rate == "":
                        break

                    if new_daily_rate.isdigit() and int(new_daily_rate) > 0:
                        selected_car["daily_rate"] = int(new_daily_rate)
                        break

                    print("Harga sewa harus berupa angka lebih dari 0. Silakan coba lagi.\n")

                if new_brand != "":
                    selected_car["brand"] = new_brand

                if new_model != "":
                    selected_car["model"] = new_model

                if new_license_plate != "":
                    selected_car["license_plate"] = new_license_plate

                print("\nData mobil berhasil diubah!\n")
                show_car_list()

                input("Tekan Enter untuk kembali ke submenu...")

            elif selected_submenu == 4:
                clear_terminal()
                show_car_list()

                while True:
                    selected_id = input("Masukkan ID mobil yang ingin dihapus: ").upper()

                    selected_car = None
                    car_found = False

                    for car in car_list:
                        if car["id"] == selected_id:
                            car_found = True

                            if car["status"] == "rented":
                                print("Mobil yang sedang disewa tidak bisa dihapus. Silakan pilih ID mobil lain.\n")
                                break

                            selected_car = car
                            break

                    if selected_car is not None:
                        break

                    if not car_found:
                        print("ID mobil tidak ada. Silakan masukkan kembali.\n")

                car_list.remove(selected_car)

                print("\nData mobil berhasil dihapus!\n")
                show_car_list()

                input("Tekan Enter untuk kembali ke submenu...")

            elif selected_submenu == 5:
                clear_terminal()
                show_car_list()

                while True:
                    selected_id = input("Masukkan ID mobil yang ingin diubah statusnya: ").upper()
                    selected_car = find_car_by_id(selected_id)

                    if selected_car is not None:
                        break

                    print("ID mobil tidak ada. Silakan masukkan kembali.\n")

                if selected_car["status"] == "rented":
                    print("\nMobil yang sedang disewa tidak bisa diubah status maintenance.")

                elif selected_car["status"] == "available":
                    selected_car["status"] = "maintenance"
                    print("\nStatus mobil berhasil diubah menjadi maintenance.")

                elif selected_car["status"] == "maintenance":
                    selected_car["status"] = "available"
                    print("\nStatus mobil berhasil diubah menjadi tersedia.")

                print()
                show_car_list()

                input("Tekan Enter untuk kembali ke submenu...")

            elif selected_submenu == 6:
                clear_terminal()
                print("Kembali ke Menu Utama...")
                input("Tekan Enter untuk lanjut...")
                break

    elif selected_main_menu == 2:
        while True:
            clear_terminal()
            show_submenu_2()

            selected_submenu = input_submenu_2()

            if selected_submenu == 1:
                clear_terminal()
                show_customer_list()
                input("Tekan Enter untuk kembali ke submenu...")

            elif selected_submenu == 2:
                clear_terminal()
                print("=" * 50)
                print("TAMBAH CUSTOMER".center(50))
                print("=" * 50)

                new_id = generate_customer_id()
                print(f"ID Customer: {new_id}")

                nama = input_required("Masukkan nama customer: ")
                no_ktp = input_number_required("Masukkan nomor KTP: ")
                no_hp = input_number_required("Masukkan nomor HP: ")
                alamat = input_required("Masukkan alamat: ")

                customer_list.append({
                    "id_customer": new_id,
                    "nama": nama,
                    "no_ktp": str(no_ktp),
                    "no_hp": str(no_hp),
                    "alamat": alamat
                })

                print("\nData customer berhasil ditambahkan!\n")
                show_customer_list()

                input("Tekan Enter untuk kembali ke submenu...")

            elif selected_submenu == 3:
                clear_terminal()
                show_customer_list()

                while True:
                    selected_id = input("Masukkan ID customer yang ingin diubah: ").upper()
                    selected_customer = find_customer_by_id(selected_id)

                    if selected_customer is not None:
                        break

                    print("ID customer tidak ada. Silakan masukkan kembali.\n")

                clear_terminal()
                print("=" * 50)
                print("UPDATE DATA CUSTOMER".center(50))
                print("=" * 50)
                print(f"ID Customer : {selected_customer['id_customer']}")
                print(f"Nama        : {selected_customer['nama']}")
                print(f"No. KTP     : {selected_customer['no_ktp']}")
                print(f"No. HP      : {selected_customer['no_hp']}")
                print(f"Alamat      : {selected_customer['alamat']}")
                print("=" * 50)
                print("Kosongkan input jika tidak ingin mengubah data.\n")

                new_nama = input("Masukkan nama baru: ").strip()

                while True:
                    new_no_ktp = input("Masukkan nomor KTP baru: ").strip()

                    if new_no_ktp == "":
                        break

                    if new_no_ktp.isdigit():
                        selected_customer["no_ktp"] = new_no_ktp
                        break

                    print("Nomor KTP harus berupa angka. Silakan coba lagi.\n")

                while True:
                    new_no_hp = input("Masukkan nomor HP baru: ").strip()

                    if new_no_hp == "":
                        break

                    if new_no_hp.isdigit():
                        selected_customer["no_hp"] = new_no_hp
                        break

                    print("Nomor HP harus berupa angka. Silakan coba lagi.\n")

                new_alamat = input("Masukkan alamat baru: ").strip()

                if new_nama != "":
                    selected_customer["nama"] = new_nama

                if new_alamat != "":
                    selected_customer["alamat"] = new_alamat

                print("\nData customer berhasil diubah!\n")
                show_customer_list()

                input("Tekan Enter untuk kembali ke submenu...")

            elif selected_submenu == 4:
                clear_terminal()
                show_customer_list()

                while True:
                    selected_id = input("Masukkan ID customer yang ingin dihapus: ").upper()
                    selected_customer = find_customer_by_id(selected_id)

                    if selected_customer is not None:
                        break

                    print("ID customer tidak ada. Silakan masukkan kembali.\n")

                customer_list.remove(selected_customer)

                print("\nData customer berhasil dihapus!\n")
                show_customer_list()

                input("Tekan Enter untuk kembali ke submenu...")

            elif selected_submenu == 5:
                clear_terminal()
                print("Kembali ke Menu Utama...")
                input("Tekan Enter untuk lanjut...")
                break

    elif selected_main_menu == 3:
        clear_terminal()
        print("Kelola Transaksi Rental")
        input("Tekan Enter untuk kembali ke menu utama...")

    elif selected_main_menu == 4:
        clear_terminal()
        print("Pencarian dan Filter")
        input("Tekan Enter untuk kembali ke menu utama...")

    elif selected_main_menu == 5:
        clear_terminal()
        print("Laporan")
        input("Tekan Enter untuk kembali ke menu utama...")

    elif selected_main_menu == 6:
        clear_terminal()
        print("Terima kasih telah menggunakan Sistem Rental Mobil.")
        break