import sqlite3
from user import User
from tabulate import tabulate

connection = sqlite3.connect("rajaes.db")


def createItemTable(connection):
    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS item (id INTEGER NOT NULL PRIMARY KEY, nama text , hargaJual integer, hargaBeli integer, stok integer);")


def insertItem(connection):
    with connection:
        connection.execute("INSERT INTO item (nama, hargaJual, hargaBeli, stok) VALUES ('Jelly', 10000, 7000, 100), ('Cincau', 5000, 7000, 70), ('Mutiara', 12000, 8000, 77), ('Rumput Laut', 20000, 15000, 150), ('Kolang Kaling', 15000, 13000, 177);")


def insertNewItem(connection, nama, hargaJual, hargaBeli, stok):
    with connection:
        connection.execute(
            "INSERT INTO item (nama, hargaJual, hargaBeli, stok) VALUES (?, ?, ?, ?);", (nama, hargaJual, hargaBeli, stok))


def getItems(connection):
    with connection:
        return connection.execute("SELECT * FROM item").fetchall()


def updateItems(connection, nama, hargaJual, hargaBeli, stok, idItem):
    with connection:
        connection.execute("UPDATE item SET nama = ?, hargaJual = ?, hargaBeli = ?, stok = ? WHERE id = ?",
                           (nama, hargaJual, hargaBeli, stok, idItem))


class Item(User):

    def __init__(self, nama, hargaJual, hargaBeli, stok):
        self.__name = nama
        self.__sellPrice = hargaJual
        self.__purchasePrice = hargaBeli
        self.__stock = stok

    @property
    def getName(self):
        pass

    @getName.getter
    def getName(self):
        return self.__name

    @property
    def getSellPrice(self):
        pass

    @getSellPrice.getter
    def getSellPrice(self):
        return self.__sellPrice

    @property
    def getPurchasePrice(self):
        pass

    @getPurchasePrice.getter
    def getPurchasePrice(self):
        return self.__purchasePrice

    @property
    def getStock(self):
        pass

    @getStock.getter
    def getStock(self):
        return self.__stock

    @staticmethod
    def addItem(connection):
        item = Item(input("masukkan nama : "), input("masukkan harga jual : "), input(
            "masukkan harga beli : "), input("masukkan stok : "))

        insertNewItem(connection, item.getName, item.getSellPrice,
                      item.getPurchasePrice, item.getStock)

    @staticmethod
    def getItem(connection):
        items = getItems(connection)
        header = ["ID Barang", "Nama Barang",
                  "Harga Jual", "Harga Beli", "Stok"]
        result = []

        for barang in items:
            result.append(barang)
        return print(tabulate(result, headers=header))

    @staticmethod
    def updateItem(connection):
        idItem = input("masukkan ID : ")
        item = Item(input("masukkan nama : "), input("masukkan harga jual : "), input(
            "masukkan harga beli : "), input("masukkan stok : "))

        updateItems(connection, item.getName, item.getSellPrice,
                    item.getPurchasePrice, item.getStock, idItem)
