import sqlite3

create_User_Table = "CREATE TABLE IF NOT EXISTS user (id INTEGER NOT NULL PRIMARY KEY, username TEXT, password TEXT, nama TEXT, gender TEXT, alamat TEXT, telepon INTEGER, tanggalMasuk TEXT);"

insert_User_Table = "INSERT INTO user (username, password, nama, gender, alamat, telepon, tanggalMasuk) VALUES (?, ?, ?, ?, ?, ?, ?);"

get_User_Table = "SELECT * FROM user"

get_User_Founder = "SELECT username, password, nama, gender, alamat, telepon FROM user WHERE tanggalMasuk = 'none';"


def connect():
    return sqlite3.connect("rajaes.db")


def createUserTable(connection):
    with connection:
        connection.execute(create_User_Table)


def addUser(connection, username, password, nama, gender, alamat, telepon, tanggalMasuk):
    with connection:
        connection.execute(
            insert_User_Table, (username, password, nama, gender, alamat, telepon, tanggalMasuk))


def getAllUser(connection):
    with connection:
        return connection.execute(get_User_Table).fetchall()


def getUserFounder(connection):
    with connection:
        return connection.execute(get_User_Founder).fetchall()


class User:

    def __init__(self, username, password, nama, gender, alamat, telepon, tanggalMasuk):
        self.__username = username
        self.__password = password
        self.__name = nama
        self.__gender = gender
        self.__address = alamat
        self.__phone = telepon
        self.__acceptedWork = tanggalMasuk

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

    @property
    def getAcceptedWork(self):
        pass

    @getAcceptedWork.getter
    def getAcceptedWork(self):
        return self.__acceptedWork

    def promtAddUser(self, connection):
        user = User(input("Masukkan username : "), input(
            "Masukkan password : "), input("Masukkan nama : "), input("Masukkan gender : "), input("Masukkan alamat : "), input("Masukkan telepon : "), input("Masukkan tanggal masuk : "))
        addUser(connection, user.getUsername, user.getPassword, user.getName,
                user.getGender, user.getAddress, user.getPhone, user.getAcceptedWork)

    def userInfo(self, connection):
        users = getAllUser(connection)

        for user_info in users:
            print(user_info)
