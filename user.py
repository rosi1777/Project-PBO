import sqlite3
import item
import ordered

create_User_Table = "CREATE TABLE IF NOT EXISTS user (id INTEGER NOT NULL PRIMARY KEY, username TEXT, password TEXT, nama TEXT, gender TEXT, alamat TEXT, telepon INTEGER, tanggalMasuk TEXT);"

insert_employee = "INSERT INTO user (username, password, nama, gender, alamat, telepon, tanggalMasuk) VALUES ('wnykhza', 'wnykhza77*', 'Fathorrosi', 'Pria', 'Probolinggo', 085335211419, '21-02-1994'), ('eren', 'eren1234', 'Eren Yeager', 'Pria', 'Paradise', 837283628362, '12-08-2013'), ('naruto', 'naruto1234', 'Uzumaki Naruto', 'Pria', 'Konoha', 18371739173, '07-07-1919');"

insert_new_employee = "INSERT INTO user (username, password, nama, gender, alamat, telepon, tanggalMasuk) VALUES (?, ?, ?, ?, ?, ?, ?);"

insert_owner = "INSERT INTO user (username, password, nama, gender, alamat, telepon) VALUES ('synerfo', 'synerfo1234', 'Rafi Cahya Putra', 'Pria', 'Probolinggo', 081238657974);"

update_owner = "UPDATE user SET username = ?, password = ?, nama = ?, gender = ?, alamat = ?, telepon = ? WHERE username = ?"

update_employee = "UPDATE user SET username = ?, password = ?, nama = ?, gender = ?, alamat = ?, telepon = ?, tanggalMasuk = ? WHERE username = ?"

get_employee = "SELECT id, username, password, nama, gender, alamat, telepon, tanggalMasuk FROM user WHERE tanggalMasuk != NULL;"

get_owner = "SELECT username, password, nama, gender, alamat, telepon FROM user WHERE tanggalMasuk = NULL;"

get_All = "SELECT * FROM user"

connection = sqlite3.connect("rajaes.db")

def createUserTable(connection):
    with connection:
        connection.execute(create_User_Table)

def addEmployee(connection):
    with connection:
        connection.execute(insert_employee)


def addOwner(connection):
    with connection:
        connection.execute(insert_owner)


def addNewEmployee(connection, username, password, nama, gender, alamat, telepon, tanggalMasuk):
    with connection:
        connection.execute(
            insert_new_employee, (username, password, nama, gender, alamat, telepon, tanggalMasuk))

def updateOwner(connection, username, password, nama, gender, alamat, telepon):
    with connection:
        connection.execute(update_owner, (username, connection, username, password, nama, gender, alamat, telepon))

def updateEmployee(connection, username, password, nama, gender, alamat, telepon, tanggalMasuk):
    with connection:
        connection.execute(update_owner, (username, connection, username, password, nama, gender, alamat, telepon, tanggalMasuk))

def getEmployee(connection):
    with connection:
        return connection.execute(get_employee).fetchall()


def getOwner(connection):
    with connection:
        return connection.execute(get_owner).fetchone()

def getAll(connection):
    with connection:
        return connection.execute(get_All).fetchall()


class User:

    def __init__(self, username, password, nama, gender, alamat, telepon):
        self.__username = username
        self.__password = password
        self.__name = nama
        self.__gender = gender
        self.__address = alamat
        self.__phone = telepon

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

    @property
    def getGender(self):
        pass

    @getGender.getter
    def getGender(self):
        return self.__gender

    @property
    def getAddress(self):
        pass

    @getAddress.getter
    def getAddress(self):
        return self.__address

    @property
    def getPhone(self):
        pass

    @getPhone.getter
    def getPhone(self):
        return self.__phone







