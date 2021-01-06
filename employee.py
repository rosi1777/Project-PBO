import sqlite3
from user import User
from tabulate import tabulate

connection = sqlite3.connect("rajaes.db")


def createEmployeeTable(connection):
    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS employee (id INTEGER NOT NULL PRIMARY KEY, username TEXT, password TEXT, nama TEXT, gender TEXT, alamat TEXT, telepon INTEGER, tanggalMasuk TEXT);")


def insertEmployee(connection):
    with connection:
        connection.execute("INSERT INTO employee (username, password, nama, gender, alamat, telepon, tanggalMasuk) VALUES ('synefo', 'synefo77*', 'Rafi Cahya Putra', 'Pria', 'Probolinggo', 085335211419, '21-02-1994'), ('eren', 'eren1234', 'Eren Yeager', 'Pria', 'Paradise', 837283628362, '12-08-2013'), ('naruto', 'naruto1234', 'Uzumaki Naruto', 'Pria', 'Konoha', 18371739173, '07-07-1919');")


def addEmployees(connection, username, password, nama, gender, alamat, telepon, tanggalMasuk):
    with connection:
        connection.execute("INSERT INTO employee (username, password, nama, gender, alamat, telepon, tanggalMasuk) VALUES (?, ?, ?, ?, ?, ?, ?);",
                           (username, password, nama, gender, alamat, telepon, tanggalMasuk))


def updateEmployees(connection, username, password, nama, gender, alamat, telepon, tanggalMasuk, idKaryawan):
    with connection:
        connection.execute("UPDATE employee SET username = ?, password = ?, nama = ?, gender = ?, alamat = ?, telepon = ?, tanggalMasuk = ? WHERE id = ?",
                           (username, password, nama, gender, alamat, telepon, tanggalMasuk, idKaryawan))


def getEmployees(connection):
    with connection:
        return connection.execute("SELECT * FROM employee;").fetchall()


class Employee(User):

    def __init__(self, username, password, nama, gender, alamat, telepon, tanggalMasuk):
        super().__init__(username, password, nama)
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

    @staticmethod
    def updateEmployee(connection):
        idKaryawan = input("masukkan id karyawan : ")

        employee = Employee(input("masukkan username : "), input(
            "masukkan password : "), input("masukkan nama : "), input("masukkan gender : "), input("masukkan alamat : "), input("masukkan telepon : "), input("masukkan tanggal masuk : "))

        updateEmployees(connection, employee.getUsername, employee.getPassword, employee.getName,
                        employee.getGender, employee.getAddress, employee.getPhone, employee.getAcceptedWork, idKaryawan)

    @staticmethod
    def addEmployee(connection):
        employee = Employee(input("masukkan username : "), input(
            "masukkan password : "), input("masukkan nama : "), input("masukkan gender : "), input("masukkan alamat : "), input("masukkan telepon : "), input("masukkan tanggal masuk : "))

        addEmployees(connection, employee.getUsername, employee.getPassword, employee.getName,
                     employee.getGender, employee.getAddress, employee.getPhone, employee.getAcceptedWork)

    @staticmethod
    def getEmployee(connection):
        employees = getEmployees(connection)
        header = ["ID Karyawan", "Username", "Password", "Nama Karyawan",
                  "Gender", "Alamat", "Telepon", "Tanggal Masuk"]
        result = []

        for employee in employees:
            result.append(employee)
        return print(tabulate(result, headers=header))
