import csv
from datetime import datetime


def catat_login(nama, role, status):
    with open("RiwayatLogin.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            nama,
            role,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            status
        ])

def menu_admin():
        while True:
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
                    break
                elif user_admin == 2:
                    print('tambah data')
                    break
                elif user_admin == 3:
                    print('Ubah data')
                    break
                elif user_admin == 4:
                    print('status buku')
                    break
                elif user_admin == 5:
                    print('Tambah anggota perpus')
                    break
                elif user_admin == 6:
                    print('kelola rak buku')
                    break
                elif user_admin == 7:
                    print('kelola rak buku')
                    break
                elif user_admin == 8:
                    print('logout')
                    break
                else: 
                    print('erorr')
                    break
                
            except ValueError:
               print("Input harus berupa angka")
               break
    
def menu_user():
        while True:
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
                    break
                elif user_peminjam == 2:
                    print('tambah data')
                    break
                elif user_peminjam == 3:
                    print('Ubah data')
                    break
                elif user_peminjam == 4:
                    print('status buku')
                    break
                elif user_peminjam == 5:
                    print('Jadwal pengembalian')
                    break
                elif user_peminjam == 6:
                    print('logout')
                    break
            
                else:
                    print('erorr')
            except ValueError:
                print("Input harus berupa angka")
    

def login():
    nama = input("Masukkan nama: ")
    pin = input("Masukkan PIN (5 digit): ")

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
        print("PIN tidak sesuai role")
        catat_login(nama, "unknown", "GAGAL")
        return

    with open(file_data, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == nama and row['password'] == pin:
                print(f"\nLogin berhasil sebagai {role.upper()}")
                catat_login(nama, role, "BERHASIL")

                if role == "admin":
                    menu_admin()
                else:
                    menu_user()
                return

    print("Nama atau PIN salah")
    catat_login(nama, role, "GAGAL")
    
login()
