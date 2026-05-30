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


def input_number(message):
    while True:
        value = input(message)

        if value.isdigit():
            return int(value)

        print("Input harus berupa angka. Silakan coba lagi.\n")


def input_main_menu():
    while True:
        selected_menu = input("Pilih menu: ")

        if selected_menu.isdigit():
            selected_menu = int(selected_menu)

            if selected_menu in range(1, 7):
                return selected_menu

        print("Menu yang dipilih tidak valid! Silakan pilih menu 1-6.")


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

                brand = input("Masukkan merk mobil: ")
                model = input("Masukkan model mobil: ")
                year = input_number("Masukkan tahun pembuatan: ")
                license_plate = input("Masukkan plat nomor: ")
                daily_rate = input_number("Masukkan harga sewa /hari: ")

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

                while True:
                    print("\nPilih kolom yang ingin diubah:")
                    print("1. Merk")
                    print("2. Model")
                    print("3. Tahun")
                    print("4. Plat Nomor")
                    print("5. Harga Sewa")
                    print("6. Semua")

                    selected_column = input("Pilih 1-6: ")

                    if selected_column.isdigit():
                        selected_column = int(selected_column)

                        if selected_column in range(1, 7):
                            break

                    print("Pilihan kolom tidak valid. Silakan pilih 1-6.\n")

                if selected_column == 1:
                    selected_car["brand"] = input("Masukkan merk baru: ")

                elif selected_column == 2:
                    selected_car["model"] = input("Masukkan model baru: ")

                elif selected_column == 3:
                    selected_car["year"] = input_number("Masukkan tahun baru: ")

                elif selected_column == 4:
                    selected_car["license_plate"] = input("Masukkan plat nomor baru: ")

                elif selected_column == 5:
                    selected_car["daily_rate"] = input_number("Masukkan harga sewa baru: ")

                elif selected_column == 6:
                    selected_car["brand"] = input("Masukkan merk baru: ")
                    selected_car["model"] = input("Masukkan model baru: ")
                    selected_car["year"] = input_number("Masukkan tahun baru: ")
                    selected_car["license_plate"] = input("Masukkan plat nomor baru: ")
                    selected_car["daily_rate"] = input_number("Masukkan harga sewa baru: ")

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
        clear_terminal()
        print("Kelola Data Customer")
        input("Tekan Enter untuk kembali ke menu utama...")

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