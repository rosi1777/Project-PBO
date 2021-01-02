import sqlite3
import owner
import item
import ordered


def menu():
    sytemMenu = """------Raja Es-------
1. Info Akun
2. Ubah Akun
3. Lihat Barang
4. Menambah Barang
5. Ubah barang
6. Menambah Pesanan
7. Melihat Pesanan
8. Menambah Penjualan
9. Melihat Penjualan
10. Exit

Your Selection : """

    connection = sqlite3.connect("rajaes.db")

    while (userInput := input(sytemMenu)) != "10":
        if userInput == "1":
            owner.Owner.getAccount(connection)
        elif userInput == "2":
            owner.Owner.promtUpdateOwner(connection)
        elif userInput == "3":
            item.Item.getAllItem(connection)
        elif userInput == "4":
            item.Item.addItem(connection)
        elif userInput == "5":
            item.Item.editItem(connection)
        elif userInput == "6":
            ordered.Ordered.addOrder(connection)
        elif userInput == "7":
            ordered.Ordered.seeOrdered(connection)
        elif userInput == "8":
            ordered.Ordered.addSales(connection)
        elif userInput == "9":
            ordered.Ordered.seeSale(connection)
        else:
            print("Inputan anda invalid")


def login():
    connection = sqlite3.connect("rajaes.db")

    print("----------Login-----------")

    username = input("masukkan username : ")
    password = input("masukkan password : ")

    tempUsername = []
    tempPassword = []
    tempNama = []

    for x in owner.getOwner(connection):
        tempUsername.append(x[0])
        tempPassword.append(x[1])
        tempNama.append(x[2])

    for i in range(len(tempUsername)):
        if username == tempUsername[i] and password == tempPassword[i]:
            menu()
        else:
            login()



login()
