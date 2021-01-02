import sqlite3

create_Owner_Table = "CREATE TABLE IF NOT EXISTS owner (id INTEGER NOT NULL PRIMARY KEY, username TEXT, password TEXT, nama TEXT);"

insert_owner = "INSERT INTO owner (username, password, nama) VALUES ('synerfo', 'synerfo1234', 'Rafi Cahya Putra');"

update_owner = "UPDATE owner SET username = ?, password = ?, nama = ? where id = 1"

get_owner = "SELECT username, password, nama FROM owner"

connection = sqlite3.connect("rajaes.db")


def createOwnerTable(connection):
    with connection:
        connection.execute(create_Owner_Table)


def insertOwner(connection):
    with connection:
        connection.execute(insert_owner)


def updateOwner(connection, username, password, nama):
    with connection:
        connection.execute(update_owner, (username, password, nama))


def getOwner(connection):
    with connection:
        return connection.execute(get_owner).fetchall()


class Owner:

    def __init__(self, username, password, nama):
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
    def promtUpdateOwner(connection):
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
