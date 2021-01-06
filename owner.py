import sqlite3
from user import User

connection = sqlite3.connect("rajaes.db")


def createOwnerTable(connection):
    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS owner (id INTEGER NOT NULL PRIMARY KEY, username TEXT, password TEXT, nama TEXT, role TEXT);")


def insertOwner(connection):
    with connection:
        connection.execute(
            "INSERT INTO owner (username, password, nama, role) VALUES ('wnykhza', 'wnykhza77*', 'Fathorrosi', 'Owner');")


def updateOwner(connection, username, password, nama):
    with connection:
        connection.execute(
            "UPDATE owner SET username = ?, password = ?, nama = ? where id = 1", (username, password, nama))


def getOwner(connection):
    with connection:
        return connection.execute("SELECT username, password, nama, role FROM owner").fetchall()


class Owner(User):

    def __init__(self, username, password, nama):
        super().__init__(username, password, nama)
        self.__username = username
        self.__password = password
        self.__name = nama

    @property
    def getUsername(self):
        pass

    @getUsername.getter
    def getUsername(self):
        return self.__username

    @property
    def getPassword(self):
        pass

    @getPassword.getter
    def getPassword(self):
        return self.__password

    @property
    def getName(self):
        pass

    @getName.getter
    def getName(self):
        return self.__name

    @staticmethod
    def updateAccount(connection):
        owner = Owner(input("masukkan username : "), input(
            "masukkan password : "), input("masukkan nama : "))
        updateOwner(connection, owner.getUsername,
                    owner.getPassword, owner.getName)

    @staticmethod
    def getAccount(connection):
        account = getOwner(connection)
        print("--------Akun-------")

        for accounts in account:
            print("Username : {} \nPassword : {} \nNama : {}".format(
                accounts[0], accounts[1], accounts[2]))
