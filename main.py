from user import User
from founder import Founder
import sqlite3
import user
import founder

menuPrompt = """----Raja Es----
1. Menambah data user
2. Melihat info user
3. Melihat info karyawan
4. Exit

Your Selection : """


def menu():
    users = User("0", "0", "0", "0", "0", 0, "0")
    founders = Founder("0", "0", "0", "0", "0", 0, "0")

    connection = user.connect()
    user.createUserTable(connection)

    while (userInput := input(menuPrompt)) != "4":
        if userInput == "1":
            users.promtAddUser(connection)
        elif userInput == "2":
            founders.userInfo(connection)
        elif userInput == "3":
            users.userInfo(connection)
        else:
            print("Inputan anda invalid")


menu()
