from prettytable import PrettyTable
import os
import time

role = {
    "admin": {
        "password": "admin123",
        "role": "admin"
    },
    "user": {
        "password": "12365",
        "role": "user"
    }
}

data_mahasiswa = [
    ("Gloria", "Sistem Informasi", 98),
    ("Darman", "Elektro", 90),
    ("Rin", "Informatika", 87)
]

def login():
    while True:
        print("=== LOGIN ===")
        username = input("Username: ")
        password = input("Password: ")

        if username in role:
            if password == role[username]["password"]:
                print("Login berhasil.")
                print("Role:", role[username]["role"])
                return role[username]["role"]
            else:
                print("Username atau password salah.")
        print("Silakan coba lagi.")

def tampilkan_data():
    if len(data_mahasiswa) == 0:
        print("Data mahasiswa masih kosong.")
    else:
        table = PrettyTable()
        table.field_names = ["No", "Nama", "Jurusan", "Nilai"]

        for i in range(len(data_mahasiswa)):
            table.add_row([
                i + 1,
                data_mahasiswa[i][0],
                data_mahasiswa[i][1],
                data_mahasiswa[i][2]
            ])

        print(table)

def tambah_data():
    nama = input("Nama mahasiswa: ")
    jurusan = input("Jurusan: ")
    nilai = int(input("Nilai: "))

    data_mahasiswa.append((nama, jurusan, nilai))

    print("Data berhasil ditambahkan.")
    time.sleep(3)

def ubah_data():
    if len(data_mahasiswa) == 0:
        print("Data mahasiswa masih kosong.")
    else:
        tampilkan_data()

        nomor = int(input("Pilih nomor data yang ingin diubah: "))

        if 1 <= nomor <= len(data_mahasiswa):
            nama = input("Nama baru: ")
            jurusan = input("Jurusan baru: ")
            nilai = int(input("Nilai baru: "))

            data_mahasiswa[nomor - 1] = (nama, jurusan, nilai)

            print("Data berhasil diubah.")
            time.sleep(3)
        else:
            print("Nomor data tidak ditemukan.")

def hapus_data():
    if len(data_mahasiswa) == 0:
        print("Data mahasiswa masih kosong.")
    else:
        tampilkan_data()

        nomor = int(input("Pilih nomor data yang ingin dihapus: "))

        if 1 <= nomor <= len(data_mahasiswa):
            data_mahasiswa.pop(nomor - 1)

            print("Data berhasil dihapus.")
            time.sleep(3)
        else:
            print("Nomor data tidak ditemukan.")

role = login()
if role == "admin":    
    os.system("cls" if os.name == "nt" else "clear")
    print("Layar berhasil dibersihkan dengan os.system()")
    while True:
        print("\n=== DATA MAHASISWA ===")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Ubah Data")
        print("4. Hapus Data")
        print("5. Keluar")
        

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah_data()

        elif pilihan == "2":
            tampilkan_data()

        elif pilihan == "3":
            ubah_data()

        elif pilihan == "4":
            hapus_data()

        elif pilihan == "5":
            print("Program selesai.")
            break

        else:
            print("Pilihan menu tidak valid.") 

elif role == "user":
    os.system("cls" if os.name == "nt" else "clear")
    print("Layar berhasil dibersihkan dengan os.system()")
    while True:
        print("\n=== DATA MAHASISWA ===")
        print("1. Tampilkan Data")
        print("2. Keluar")

        pilihan = input("Pilih menu (1-2): ")

        if pilihan == "1":
            tampilkan_data()

        elif pilihan == "2":
            print("Program selesai.")
            break

        else:
            print("Pilihan menu tidak valid.")