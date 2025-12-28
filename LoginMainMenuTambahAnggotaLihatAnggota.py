import csv
from datetime import datetime
import pandas as pd


def catat_login(nama, role, status):
    with open("RiwayatLogin.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            nama,
            role,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            status
        ])
def tambah_anggota(role):
    
    if role != "admin":
        print("Hanya admin yang dapat menambahkan anggota perpustakaan.")
        return
    
    print("======MENAMBAHKAN ANGGOTA======")
    
    username = str(input("Masukkan nama lengkap Anggota Baru Perpustakaan: "))
    password = str(input("Masukkan Password dari Anggota baru (Diawali dengan angka 2 dan bejumlah 5 digit): "))
    
    if not (password.isdigit() and len(password) == 5 and password[0] == "2"):
        print("Password tidak valid, harus berjumlah 5 digit dan diawali angka 2")
        return
    
    alamat = str(input("Masukkan Alamat tempat tinggal Anggota baru: "))
    nomer_hp = int(input("Masukkan nomer handphone yang bisa dihubungi: "))
    
    with open("dataAnggotaPerpus.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            username,
            password,
            alamat,
            nomer_hp,
        ])
    
    print(f"Anggota baru sudah ditambahkan, dengan nama {username}")
    
    tambah_lagi = str(input("Apakah ingin menambahkan Anggota Perpustakaan lainnya?(yes/no): " ))
    if tambah_lagi == "yes":
        tambah_anggota()
    else:
        menu_admin()
    return

def lihat_data_anggota(role):
    if role != "admin":
        print("Hanya admin yang dapat menambahkan anggota perpustakaan.")
        return
    
    print("====== DATA ANGGOTA PERPUSTAKAAN ======")
    try:
        data_anggota = pd.read_csv("dataAnggotaPerpus.csv")

        if data_anggota.empty:
            print("Belum ada data anggota.")
            return
    
        print(data_anggota.to_string(index=False))
  
    except FileNotFoundError:
            print("File data anggota belum tersedia.")
        
    

def menu_admin():
            print('==================================')
            print('=========== MAIN MENU ============')
            print('= 1. Lihat data buku             =')
            print('= 2. Tambah data buku            =')
            print('= 3. Ubah data buku              =')
            print('= 4. Status buku                 =')
            print('= 5. Kelola rak buku             =')
            print('= 6. Tambah anggota perpustakaan =')
            print('= 7. lihat anggota perpustakaan  =')
            print('= 8. Logout                      =')
            print('==================================')
            try:
                user_admin = int(input("pilih menu = "))
                if user_admin == 1 :
                    print("lihat data")
                elif user_admin == 2:
                    print('tambah data')
                elif user_admin == 3:
                    print('Ubah data')
                elif user_admin == 4:
                    print('status buku')
                elif user_admin == 5:
                    print('Kelola rak buku')
                elif user_admin == 6:
                    tambah_anggota("admin")
                elif user_admin == 7:
                    lihat_data_anggota("admin")
                elif user_admin == 8:
                    print('logout')
                else: 
                    print('erorr')
                
            except ValueError:
               print("Input harus berupa angka")
    
def menu_user():
            print('==================================')
            print('=========== MAIN MENU ============')
            print('= 1. Lihat daftar buku           =')
            print('= 2. Lihat status buku           =')
            print('= 3. Cari buku                   =')
            print('= 4. Booking buku                =')
            print('= 5. jadwal pengembalian         =')
            print('= 6. keluar                      =')
            print('==================================')    
            try:
                user_peminjam = int(input("pilih menu = "))
                if user_peminjam == 1 :
                    print("lihat data")
                elif user_peminjam == 2:
                    print('tambah data')
                elif user_peminjam == 3:
                    print('Ubah data')
                elif user_peminjam == 4:
                    print('status buku')
                elif user_peminjam == 5:
                    print('Jadwal pengembalian')
                elif user_peminjam == 6:
                    print('logout')
            
                else:
                    print('erorr')
            except ValueError:
                print("Input harus berupa angka")
    

def login():
    nama = (input("Masukkan Nama Anda: "))
    pin = (input("Masukkan PIN (5 digit angka): "))

    if not (pin.isdigit() and len(pin) == 5):
        print("PIN harus 5 digit angka")
        catat_login(nama, "Telah GAGAL melakukan Login")
        return

    if pin[0] == '1':
        role = "admin"
        file_data = "dataAdmin.csv"
    elif pin[0] == '2':
        role = "Anggota"
        file_data = "dataAnggotaPerpus.csv"
    else:
        file_data = ""
        catat_login(nama, "Tidak Diketahui", "Telah  GAGAL Melakukan Login")
        
    
    try:
        with open(file_data, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['username'] == nama and row['password'] == pin:
                    print(f"\nLogin berhasil sebagai {role.upper()} Perpustakaan")
                    catat_login(nama, role, "BERHASIL")

                    if role == "admin":
                        menu_admin()
                    else:
                        menu_user()
                    return
    except FileNotFoundError:
        print("Data akun tidak ditemukan.")
        catat_login(nama, "Tidak Diketahui ", "Telah Gagal Melakukan Login")
    
login()

