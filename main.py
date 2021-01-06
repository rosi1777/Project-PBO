import sqlite3
import owner
import item
import ordered
import employee


def ownerMenu():
    sytemMenu = """---------Raja Es-----------
1. Info Akun
2. Ubah Akun
3. Melihat Data Barang
4. Melihat Data Pesanan
5. Melihat Data Penjualan
6. Melihat Data Karyawan
7. Menambah Data Karyawan
8. Update Data Karyawan
9. Exit

Your Selection : """

    connection = sqlite3.connect("rajaes.db")

    while (userInput := input(sytemMenu)) != "10":
        if userInput == "1":
            owner.Owner.getAccount(connection)
        elif userInput == "2":
            owner.Owner.updateAccount(connection)
        elif userInput == "3":
            item.Item.getItem(connection)
        elif userInput == "4":
            ordered.Ordered.getOrder(connection)
        elif userInput == "5":
            ordered.Ordered.getSale(connection)
        elif userInput == "6":
            employee.Employee.getEmployee(connection)
        elif userInput == "7":
            employee.Employee.addEmployee(connection)
        elif userInput == "8":
            employee.Employee.updateEmployee(connection)
        elif userInput == "9":
            login()


def employeeMenu():
    sytemMenu = """---------Raja Es-----------
1. Melihat Data Barang
2. Menambah Data Barang
3. Update Data Barang
4. Melihat Data Pesanan
5. Menambah Data Pesanan
6. Melihat Data Penjualan
7. Menambah Data Penjualan
8. Exit

Your Selection : """

    connection = sqlite3.connect("rajaes.db")

    while (userInput := input(sytemMenu)) != "9":
        if userInput == "1":
            item.Item.getItem(connection)
        elif userInput == "2":
            item.Item.addItem(connection)
        elif userInput == "3":
            item.Item.updateItem(connection)
        elif userInput == "4":
            ordered.Ordered.getOrder(connection)
        elif userInput == "5":
            ordered.Ordered.addOrder(connection)
        elif userInput == "6":
            ordered.Ordered.getSale(connection)
        elif userInput == "7":
            ordered.Ordered.addSale(connection)
        elif userInput == "8":
            login()


def login():
    connection = sqlite3.connect("rajaes.db")

    print("-----------------Login-----------------")

    username = input("masukkan username : ")
    password = input("masukkan password : ")

    tempUsername = []
    tempPassword = []
    tempNama = []
    tempRole = []

    for x in owner.getOwner(connection):
        tempUsername.append(x[0])
        tempPassword.append(x[1])
        tempNama.append(x[2])
        tempRole.append(x[3])

    for y in employee.getEmployees(connection):
        tempUsername.append(y[1])
        tempPassword.append(y[2])
        tempNama.append(y[3])
        tempRole.append(y[4])

    for i in range(len(tempUsername)):
        if username == tempUsername[i] and password == tempPassword[i]:
            if tempRole[i] == "Owner":
                ownerMenu()
            else:
                employeeMenu()


login()
