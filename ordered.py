import sqlite3
from user import User
from tabulate import tabulate

connection = sqlite3.connect("rajaes.db")


def createOrderedTable(connection):
    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS ordered (id INTEGER NOT NULL PRIMARY KEY, namaPemesan TEXT, alamat TEXT, barang TEXT, jumlah INTEGER, tanggalPesan TEXT, status TEXT);")


def insertOrder(connection, namaPemesan, alamat, barang, jumlah, tanggalPesan, status):
    with connection:
        connection.execute("INSERT INTO ordered (namaPemesan, alamat, barang, jumlah, tanggalPesan, status) VALUES (?, ?, ?, ?, ?, ?);",
                           (namaPemesan, alamat, barang, jumlah, tanggalPesan, status))


def updateStatus(connection, idStatus):
    with connection:
        connection.execute(
            "UPDATE ordered SET status = 'selesai' WHERE id = ?", (idStatus))


createOrderedTable(connection)


def getOrders(connection):
    with connection:
        return connection.execute("SELECT id, namaPemesan, alamat, barang, jumlah, tanggalPesan, status FROM ordered WHERE status = 'proses'").fetchall()


def getSales(connection):
    with connection:
        return connection.execute("SELECT id, namaPemesan, alamat, barang, jumlah, tanggalPesan, status FROM ordered WHERE status = 'selesai'").fetchall()


class Ordered:

    def __init__(self, namaPemesan, alamat, barang, jumlah, tanggalPesan, status):
        self.__orderName = namaPemesan
        self.__address = alamat
        self.__item = barang
        self.__amount = jumlah
        self.__orderDate = tanggalPesan
        self.__status = status

    @property
    def getOrderName(self):
        pass

    @getOrderName.getter
    def getOrderName(self):
        return self.__orderName

    @property
    def getAddress(self):
        pass

    @getAddress.getter
    def getAddress(self):
        return self.__address

    @property
    def getItem(self):
        pass

    @getItem.getter
    def getItem(self):
        return self.__item

    @property
    def getAmount(self):
        pass

    @getAmount.getter
    def getAmount(self):
        return self.__amount

    @property
    def getOrderDate(self):
        pass

    @getOrderDate.getter
    def getOrderDate(self):
        return self.__orderDate

    @property
    def getStatus(self):
        pass

    @getStatus.getter
    def getStatus(self):
        return self.__status

    @staticmethod
    def addOrder(connection):
        order = Ordered(input("masukkan nama pemesan : "), input("masukkan alamat : "), input("masukkan barang : "), input(
            "masukkan jumlah : "), input("masukkan tanggal pesanan : "), input("masukkan status : "))

        insertOrder(connection, order.getOrderName, order.getAddress,
                    order.getItem, order.getAmount, order.getOrderDate, order.getStatus)

    @staticmethod
    def getOrder(connection):
        orders = getOrders(connection)

        header = ["ID Pesanan", "Nama Pemesan", "Alamat Pemesan",
                  "Barang", "Jumlah", "Tanggal Pesanan", "Status"]
        result = []

        for order in orders:
            result.append(order)

        return print(tabulate(result, headers=header))

    @staticmethod
    def addSale(connection):
        idStatus = input("masukkan id : ")

        updateStatus(connection, idStatus)

    @staticmethod
    def getSale(connection):
        sales = getSales(connection)

        header = ["ID Penjualan", "Nama Pemesan", "Alamat Pemesan",
                  "Barang", "Jumlah", "Tanggal Pesanan", "Status"]
        result = []

        for sale in sales:
            result.append(sale)

        return print(tabulate(result, headers=header))
