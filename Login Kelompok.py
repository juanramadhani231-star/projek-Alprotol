import csv
from datetime import datetime

login_klpk = "Login_Kelompok.csv"

def login_pengguna():
    username = input("Masukkan username: ")
    aktivitas = input("Masukkan Kegiatan yang sudah/akan dilakukan: ")

    sekarang = datetime.now()
    tanggal = sekarang.strftime("%Y-%m-%d")
    waktu = sekarang.strftime("%H:%M:%S")
   

    with open(login_klpk, mode="a", newline="") as file:
        writer = csv.writer(file)

        if login_klpk:
            writer.writerow(["username", "tanggal", "waktu", "aktivitas"])

        writer.writerow([username, tanggal, waktu, aktivitas])

    print(f"\nLogin berhasil!")
    print(f"Pengguna  : {username}")
    print(f"Tanggal   : {tanggal}")
    print(f"Waktu     : {waktu}")
    
login_pengguna()
