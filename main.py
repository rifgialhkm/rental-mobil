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
        "customer_id": "C001",
        "name": "Budi Santoso",
        "national_id": "3171010101010001",
        "phone_number": "081234567890",
        "address": "Jakarta Selatan"
    },
    {
        "customer_id": "C002",
        "name": "Andi Pratama",
        "national_id": "3171010202020002",
        "phone_number": "081298765432",
        "address": "Depok"
    },
    {
        "customer_id": "C003",
        "name": "Siti Aminah",
        "national_id": "3171010303030003",
        "phone_number": "082112223333",
        "address": "Bekasi"
    }
]

trx_list = [
    {
        "transaction_id": "T001",
        "customer_id": "C001",
        "car_id": "M001",
        "rental_days": 3,
        "daily_rate": 350000,
        "subtotal": 1050000,
        "discount": 52500,
        "fine": 0,
        "total_payment": 997500,
        "status": "selesai"
    },
    {
        "transaction_id": "T002",
        "customer_id": "C002",
        "car_id": "M002",
        "rental_days": 2,
        "daily_rate": 300000,
        "subtotal": 600000,
        "discount": 0,
        "fine": 0,
        "total_payment": 600000,
        "status": "berjalan"
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
    print("4. Keluar")
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

def show_submenu_3():
    print("=" * 50)
    print("KELOLA TRANSAKSI RENTAL".center(50))
    print("=" * 50)
    print()
    print("1. Sewa Mobil")
    print("2. Kembalikan Mobil")
    print("3. Lihat Semua Transaksi")
    print("4. Lihat Transaksi Berjalan")
    print("5. Lihat Transaksi Selesai")
    print("6. Kembali ke Menu Utama")
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

def input_number_min_zero(message):
    while True:
        value = input(message).strip()

        if value == "":
            print("Input tidak boleh kosong. Silakan isi kembali.\n")
        elif not value.isdigit():
            print("Input harus berupa angka. Silakan coba lagi.\n")
        elif int(value) < 0:
            print("Input tidak boleh kurang dari 0. Silakan coba lagi.\n")
        else:
            return int(value)

def confirm_action(message):
    while True:
        confirmation = input(message).strip().lower()

        if confirmation == "y":
            return True
        elif confirmation == "n":
            return False

        print("Input tidak valid. Masukkan y atau n.\n")

def input_main_menu():
    while True:
        selected_menu = input("Pilih menu: ")

        if selected_menu.isdigit():
            selected_menu = int(selected_menu)

            if selected_menu in range(1, 5):
                return selected_menu

        print("Menu yang dipilih tidak valid! Silakan pilih menu 1-4.")

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
            customer["customer_id"],
            customer["name"],
            customer["national_id"],
            customer["phone_number"],
            customer["address"]
        )

    console.print(table)

def generate_customer_id():
    if len(customer_list) == 0:
        return "C001"

    max_number = 0

    for customer in customer_list:
        number = int(customer["customer_id"][1:])

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
        if customer["customer_id"] == customer_id:
            return customer

    return None

def customer_has_running_transaction(customer_id):
    for trx in trx_list:
        if trx["customer_id"] == customer_id and trx["status"] == "berjalan":
            return True

    return False

# Function Helper Transaction Menu
def input_submenu_3():
    while True:
        selected_menu = input("Pilih menu: ")

        if selected_menu.isdigit():
            selected_menu = int(selected_menu)

            if selected_menu in range(1, 7):
                return selected_menu

        print("Menu yang dipilih tidak valid! Silakan pilih menu 1-6.")

def generate_transaction_id():
    if len(trx_list) == 0:
        return "T001"

    max_number = 0

    for trx in trx_list:
        number = int(trx["transaction_id"][1:])

        if number > max_number:
            max_number = number

    new_number = max_number + 1

    return "T" + str(new_number).zfill(3)

def find_transaction_by_id(transaction_id):
    for trx in trx_list:
        if trx["transaction_id"] == transaction_id:
            return trx

    return None

def get_customer_name(customer_id):
    customer = find_customer_by_id(customer_id)

    if customer is not None:
        return customer["name"]

    return "-"

def get_car_name(car_id):
    car = find_car_by_id(car_id)

    if car is not None:
        return f"{car['brand']} {car['model']}"

    return "-"

def calculate_discount(rental_days, subtotal):
    if rental_days >= 14:
        return int(subtotal * 0.15)
    elif rental_days >= 7:
        return int(subtotal * 0.10)
    elif rental_days >= 3:
        return int(subtotal * 0.05)
    else:
        return 0

def show_transaction_list(status_filter=None):
    table = Table(
        title="Daftar Transaksi Rental",
        show_header=True,
        header_style="bold magenta"
    )

    table.add_column("ID Transaksi", style="dim", width=12)
    table.add_column("Customer")
    table.add_column("Mobil")
    table.add_column("Lama Sewa", justify="center")
    table.add_column("Harga /hari", justify="right")
    table.add_column("Subtotal", justify="right")
    table.add_column("Diskon", justify="right")
    table.add_column("Denda", justify="right")
    table.add_column("Total Bayar", justify="right")
    table.add_column("Status", justify="center")

    is_empty = True

    for trx in trx_list:
        if status_filter is not None and trx["status"] != status_filter:
            continue

        is_empty = False

        if trx["status"] == "berjalan":
            status = "[yellow]Berjalan[/yellow]"
        elif trx["status"] == "selesai":
            status = "[green]Selesai[/green]"
        else:
            status = trx["status"]

        table.add_row(
            trx["transaction_id"],
            get_customer_name(trx["customer_id"]),
            get_car_name(trx["car_id"]),
            f"{trx['rental_days']} hari",
            f"Rp{trx['daily_rate']:,}".replace(",", "."),
            f"Rp{trx['subtotal']:,}".replace(",", "."),
            f"Rp{trx['discount']:,}".replace(",", "."),
            f"Rp{trx['fine']:,}".replace(",", "."),
            f"Rp{trx['total_payment']:,}".replace(",", "."),
            status
        )

    if is_empty:
        print("Data transaksi tidak tersedia.")
    else:
        console.print(table)

def is_car_has_running_transaction(car_id):
    for trx in trx_list:
        if trx["car_id"] == car_id and trx["status"] == "berjalan":
            return True

    return False

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

                print("\nData mobil yang akan ditambahkan:")
                print(f"ID Mobil        : {new_id}")
                print(f"Merk            : {brand}")
                print(f"Model           : {model}")
                print(f"Tahun           : {year}")
                print(f"Plat Nomor      : {license_plate}")
                print(f"Harga Sewa/Hari : Rp{daily_rate:,}".replace(",", "."))

                if not confirm_action("\nSimpan data mobil? y/n: "):
                    print("\nData mobil batal ditambahkan.")
                    input("Tekan Enter untuk kembali ke submenu...")
                    continue

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

                updated_brand = selected_car["brand"]
                updated_model = selected_car["model"]
                updated_year = selected_car["year"]
                updated_license_plate = selected_car["license_plate"]
                updated_daily_rate = selected_car["daily_rate"]

                new_brand = input("Masukkan merk baru: ").strip()
                new_model = input("Masukkan model baru: ").strip()

                while True:
                    new_year = input("Masukkan tahun baru: ").strip()

                    if new_year == "":
                        break

                    if new_year.isdigit() and int(new_year) > 0:
                        updated_year = int(new_year)
                        break

                    print("Tahun harus berupa angka lebih dari 0. Silakan coba lagi.\n")

                new_license_plate = input("Masukkan plat nomor baru: ").strip().upper()

                while True:
                    new_daily_rate = input("Masukkan harga sewa baru: ").strip()

                    if new_daily_rate == "":
                        break

                    if new_daily_rate.isdigit() and int(new_daily_rate) > 0:
                        updated_daily_rate = int(new_daily_rate)
                        break

                    print("Harga sewa harus berupa angka lebih dari 0. Silakan coba lagi.\n")

                if new_brand != "":
                    updated_brand = new_brand

                if new_model != "":
                    updated_model = new_model

                if new_license_plate != "":
                    updated_license_plate = new_license_plate

                print("\nData mobil setelah update:")
                print(f"ID Mobil        : {selected_car['id']}")
                print(f"Merk            : {updated_brand}")
                print(f"Model           : {updated_model}")
                print(f"Tahun           : {updated_year}")
                print(f"Plat Nomor      : {updated_license_plate}")
                print(f"Harga Sewa/Hari : Rp{updated_daily_rate:,}".replace(",", "."))
                print(f"Status          : {selected_car['status']}")

                if not confirm_action("\nUpdate data mobil? y/n: "):
                    print("\nData mobil batal diubah.")
                    input("Tekan Enter untuk kembali ke submenu...")
                    continue

                selected_car["brand"] = updated_brand
                selected_car["model"] = updated_model
                selected_car["year"] = updated_year
                selected_car["license_plate"] = updated_license_plate
                selected_car["daily_rate"] = updated_daily_rate

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

                print("\nData mobil yang akan dihapus:")
                print(f"ID Mobil        : {selected_car['id']}")
                print(f"Merk            : {selected_car['brand']}")
                print(f"Model           : {selected_car['model']}")
                print(f"Plat Nomor      : {selected_car['license_plate']}")

                if not confirm_action("\nHapus data mobil? y/n: "):
                    print("\nData mobil batal dihapus.")
                    input("Tekan Enter untuk kembali ke submenu...")
                    continue

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
                    if not confirm_action("\nUbah status mobil menjadi maintenance? y/n: "):
                        print("\nPerubahan status mobil dibatalkan.")
                        input("Tekan Enter untuk kembali ke submenu...")
                        continue

                    selected_car["status"] = "maintenance"
                    print("\nStatus mobil berhasil diubah menjadi maintenance.")

                elif selected_car["status"] == "maintenance":
                    if not confirm_action("\nUbah status mobil menjadi tersedia? y/n: "):
                        print("\nPerubahan status mobil dibatalkan.")
                        input("Tekan Enter untuk kembali ke submenu...")
                        continue

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

                name = input_required("Masukkan nama customer: ")
                national_id = input_number_required("Masukkan nomor KTP: ")
                phone_number = input_number_required("Masukkan nomor HP: ")
                address = input_required("Masukkan alamat: ")

                print("\nData customer yang akan ditambahkan:")
                print(f"ID Customer : {new_id}")
                print(f"Nama        : {name}")
                print(f"No. KTP     : {national_id}")
                print(f"No. HP      : {phone_number}")
                print(f"Alamat      : {address}")

                if not confirm_action("\nSimpan data customer? y/n: "):
                    print("\nData customer batal ditambahkan.")
                    input("Tekan Enter untuk kembali ke submenu...")
                    continue

                customer_list.append({
                    "customer_id": new_id,
                    "name": name,
                    "national_id": str(national_id),
                    "phone_number": str(phone_number),
                    "address": address
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
                print(f"ID Customer : {selected_customer['customer_id']}")
                print(f"Nama        : {selected_customer['name']}")
                print(f"No. KTP     : {selected_customer['national_id']}")
                print(f"No. HP      : {selected_customer['phone_number']}")
                print(f"Alamat      : {selected_customer['address']}")
                print("=" * 50)
                print("Kosongkan input jika tidak ingin mengubah data.\n")

                updated_name = selected_customer["name"]
                updated_national_id = selected_customer["national_id"]
                updated_phone_number = selected_customer["phone_number"]
                updated_address = selected_customer["address"]

                new_name = input("Masukkan nama baru: ").strip()

                while True:
                    new_national_id = input("Masukkan nomor KTP baru: ").strip()

                    if new_national_id == "":
                        break

                    if new_national_id.isdigit():
                        updated_national_id = new_national_id
                        break

                    print("Nomor KTP harus berupa angka. Silakan coba lagi.\n")

                while True:
                    new_phone_number = input("Masukkan nomor HP baru: ").strip()

                    if new_phone_number == "":
                        break

                    if new_phone_number.isdigit():
                        updated_phone_number = new_phone_number
                        break

                    print("Nomor HP harus berupa angka. Silakan coba lagi.\n")

                new_address = input("Masukkan alamat baru: ").strip()

                if new_name != "":
                    updated_name = new_name

                if new_address != "":
                    updated_address = new_address

                print("\nData customer setelah update:")
                print(f"ID Customer : {selected_customer['customer_id']}")
                print(f"Nama        : {updated_name}")
                print(f"No. KTP     : {updated_national_id}")
                print(f"No. HP      : {updated_phone_number}")
                print(f"Alamat      : {updated_address}")

                if not confirm_action("\nUpdate data customer? y/n: "):
                    print("\nData customer batal diubah.")
                    input("Tekan Enter untuk kembali ke submenu...")
                    continue

                selected_customer["name"] = updated_name
                selected_customer["national_id"] = updated_national_id
                selected_customer["phone_number"] = updated_phone_number
                selected_customer["address"] = updated_address

                print("\nData customer berhasil diubah!\n")
                show_customer_list()

                input("Tekan Enter untuk kembali ke submenu...")

            elif selected_submenu == 4:
                clear_terminal()
                show_customer_list()

                while True:
                    selected_id = input("Masukkan ID customer yang ingin dihapus: ").upper()
                    selected_customer = find_customer_by_id(selected_id)

                    if selected_customer is None:
                        print("ID customer tidak ada. Silakan masukkan kembali.\n")
                    elif customer_has_running_transaction(selected_id):
                        print("Customer yang masih punya transaksi berjalan tidak boleh dihapus. Silakan pilih customer lain.\n")
                    else:
                        break

                print("\nData customer yang akan dihapus:")
                print(f"ID Customer : {selected_customer['customer_id']}")
                print(f"Nama        : {selected_customer['name']}")
                print(f"No. KTP     : {selected_customer['national_id']}")
                print(f"No. HP      : {selected_customer['phone_number']}")
                print(f"Alamat      : {selected_customer['address']}")

                if not confirm_action("\nHapus data customer? y/n: "):
                    print("\nData customer batal dihapus.")
                    input("Tekan Enter untuk kembali ke submenu...")
                    continue

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
        while True:
            clear_terminal()
            show_submenu_3()

            selected_submenu = input_submenu_3()

            if selected_submenu == 1:
                clear_terminal()
                print("=" * 50)
                print("SEWA MOBIL".center(50))
                print("=" * 50)

                show_customer_list()

                while True:
                    selected_customer_id = input("Masukkan ID customer: ").upper()
                    selected_customer = find_customer_by_id(selected_customer_id)

                    if selected_customer is not None:
                        break

                    print("ID customer tidak ada. Silakan masukkan kembali.\n")

                clear_terminal()
                show_car_list()

                while True:
                    selected_car_id = input("Masukkan ID mobil yang ingin disewa: ").upper()
                    selected_car = find_car_by_id(selected_car_id)

                    if selected_car is None:
                        print("ID mobil tidak ada. Silakan masukkan kembali.\n")
                    elif selected_car["status"] != "available":
                        print("Mobil tidak tersedia untuk disewa. Silakan pilih mobil lain.\n")
                    elif is_car_has_running_transaction(selected_car_id):
                        print("Mobil masih memiliki transaksi berjalan. Silakan pilih mobil lain.\n")
                    else:
                        break

                rental_days = input_number_required("Masukkan lama sewa: ")

                subtotal = selected_car["daily_rate"] * rental_days
                discount = calculate_discount(rental_days, subtotal)
                fine = 0
                total_payment = subtotal - discount + fine

                new_transaction_id = generate_transaction_id()

                print("\nData transaksi yang akan disimpan:")
                print(f"ID Transaksi : {new_transaction_id}")
                print(f"Customer     : {selected_customer['name']}")
                print(f"Mobil        : {selected_car['brand']} {selected_car['model']}")
                print(f"Lama Sewa    : {rental_days} hari")
                print(f"Subtotal     : Rp{subtotal:,}".replace(",", "."))
                print(f"Diskon       : Rp{discount:,}".replace(",", "."))
                print(f"Total Bayar  : Rp{total_payment:,}".replace(",", "."))

                if not confirm_action("\nSimpan transaksi rental? y/n: "):
                    print("\nTransaksi rental batal disimpan.")
                    input("Tekan Enter untuk kembali ke submenu...")
                    continue

                trx_list.append({
                    "transaction_id": new_transaction_id,
                    "customer_id": selected_customer["customer_id"],
                    "car_id": selected_car["id"],
                    "rental_days": rental_days,
                    "daily_rate": selected_car["daily_rate"],
                    "subtotal": subtotal,
                    "discount": discount,
                    "fine": fine,
                    "total_payment": total_payment,
                    "status": "berjalan"
                })

                selected_car["status"] = "rented"

                print("\nTransaksi rental berhasil dibuat!")
                print(f"ID Transaksi : {new_transaction_id}")
                print(f"Subtotal     : Rp{subtotal:,}".replace(",", "."))
                print(f"Diskon       : Rp{discount:,}".replace(",", "."))
                print(f"Total Bayar  : Rp{total_payment:,}".replace(",", "."))
                print()

                show_transaction_list()

                input("Tekan Enter untuk kembali ke submenu...")

            elif selected_submenu == 2:
                clear_terminal()
                print("=" * 50)
                print("KEMBALIKAN MOBIL".center(50))
                print("=" * 50)

                show_transaction_list("berjalan")

                while True:
                    selected_transaction_id = input("Masukkan ID transaksi: ").upper()
                    selected_transaction = find_transaction_by_id(selected_transaction_id)

                    if selected_transaction is None:
                        print("ID transaksi tidak ada. Silakan masukkan kembali.\n")
                    elif selected_transaction["status"] != "berjalan":
                        print("Transaksi ini sudah selesai. Silakan pilih transaksi berjalan.\n")
                    else:
                        break

                late_days = input_number_min_zero("Masukkan jumlah hari terlambat: ")
                fine = late_days * 50000

                updated_total_payment = (
                    selected_transaction["subtotal"]
                    - selected_transaction["discount"]
                    + fine
                )

                print("\nData pengembalian:")
                print(f"ID Transaksi : {selected_transaction['transaction_id']}")
                print(f"Customer     : {get_customer_name(selected_transaction['customer_id'])}")
                print(f"Mobil        : {get_car_name(selected_transaction['car_id'])}")
                print(f"Denda        : Rp{fine:,}".replace(",", "."))
                print(f"Total Bayar  : Rp{updated_total_payment:,}".replace(",", "."))

                if not confirm_action("\nProses pengembalian mobil? y/n: "):
                    print("\nPengembalian mobil dibatalkan.")
                    input("Tekan Enter untuk kembali ke submenu...")
                    continue

                selected_transaction["fine"] = fine
                selected_transaction["total_payment"] = updated_total_payment
                selected_transaction["status"] = "selesai"

                selected_car = find_car_by_id(selected_transaction["car_id"])

                if selected_car is not None:
                    selected_car["status"] = "available"

                print("\nMobil berhasil dikembalikan!")
                print(f"Denda       : Rp{fine:,}".replace(",", "."))
                print(f"Total Bayar : Rp{selected_transaction['total_payment']:,}".replace(",", "."))
                print()

                show_transaction_list()

                input("Tekan Enter untuk kembali ke submenu...")

            elif selected_submenu == 3:
                clear_terminal()
                show_transaction_list()
                input("Tekan Enter untuk kembali ke submenu...")

            elif selected_submenu == 4:
                clear_terminal()
                show_transaction_list("berjalan")
                input("Tekan Enter untuk kembali ke submenu...")

            elif selected_submenu == 5:
                clear_terminal()
                show_transaction_list("selesai")
                input("Tekan Enter untuk kembali ke submenu...")

            elif selected_submenu == 6:
                clear_terminal()
                print("Kembali ke Menu Utama...")
                input("Tekan Enter untuk lanjut...")
                break

    elif selected_main_menu == 4:
        clear_terminal()
        print("Terima kasih telah menggunakan Sistem Rental Mobil.")
        break