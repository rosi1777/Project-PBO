import user
from user import User
import sqlite3

def menu():
    connection = sqlite3.connect("rajaes.db")

    print("---------Login--------")
    username = str(input("Masukkan Username"))
    password = str(input("Masukkan Password"))

    tempUsername = []
    tempPassword = []
    tempName = []
    tempGender = []
    tempAddress = []
    tempPhone = []
    tempAcceptedWords = []
    tempId = []

    for x in user.getAll(connection):
        tempId.append(x[0])
        tempUsername.append(x[1])
        tempPassword.append(x[2])
        tempName.append(x[3])
        tempGender.append(x[4])
        tempAddress.append(x[5])
        tempPhone.append(x[6])
        tempAcceptedWords.append(x[7])

    for i in range(len(tempUsername)):
        if username == tempUsername[i] and password == tempPassword[i]:
            print("Login Sucsess\n")
            if tempAcceptedWords[i] == "NULL":
                ownerMenu()
            else:
                employeeMenu()
        else:
            menu()

def ownerMenu():
    print("""-------Selamat Datang Di Raja Es--------
        1. Info akun
        2. Mengubah akun
        3. Melihat data pesanan
        4. Melihat data penjualan
        5. Melihat data barang
        6. Info data pegawai
        7. Menambah data pegawai
        8. Menghapus data pegawai
        9. Logout
        
        Masukkan pilihan: """)

def employeeMenu():
    print("""-------Selamat Datang Di Raja Es--------
        1. Info akun
        2. Mengubah akun
        3. Menambah data pesanan
        4. Melihat data pesanan
        5. Menambah data penjualan
        6. Melihat data penjualan
        7. Menambah data barang
        8. Melihat data barang
        9. Mengubah data barang
        9. Logout
        
        masukkan pilihan: """)



