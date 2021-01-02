import sqlite3

create_Item = "CREATE TABLE IF NOT EXISTS item (id INTEGER NOT NULL PRIMARY KEY, nama text , hargaJual integer, hargaBeli integer, stok integer);"

insert_Item = "INSERT INTO item (nama, hargaJual, hargaBeli, stok) VALUES ('Jelly', 10000, 7000, 100), ('Cincau', 5000, 7000, 70), ('Mutiara', 12000, 8000, 77), ('Rumput Laut', 20000, 15000, 150), ('Kolang Kaling', 15000, 13000, 177);"

insert_New_Item = "INSERT INTO item (nama, hargaJual, hargaBeli, stok) VALUES (?, ?, ?, ?);"

update_item = "UPDATE item SET nama = ?, hargaJual = ?, hargaBeli = ?, stok = ? WHERE id = ?"

get_item = "SELECT * FROM item"

connection = sqlite3.connect("rajaes.db")


def createItemTable(connection):
    with connection:
        connection.execute(create_Item)


def insertItem(connection):
    with connection:
        connection.execute(insert_Item)


def insertNewItem(connection, nama, hargaJual, hargaBeli, stok):
    with connection:
        connection.execute(insert_New_Item, (nama, hargaJual, hargaBeli, stok))


def getItem(connection):
    with connection:
        return connection.execute(get_item).fetchall()


def updateItem(connection, nama, hargaJual, hargaBeli, stok, idItem):
    with connection:
        connection.execute(update_item, (nama, hargaJual, hargaBeli, stok, idItem))


class Item:

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
    def getAllItem(connection):
        items = getItem(connection)

        print("ID \t Nama \t\t Harga Jual \t Harga Beli \t Stok")
        for barang in items:
            print("{} \t {} \t {} \t\t {} \t\t {}".format(
                barang[0], barang[1], barang[2], barang[3], barang[4]))

    @staticmethod
    def editItem(connection):
        idItem = input("masukkan ID : ")
        item = Item(input("masukkan nama : "), input("masukkan harga jual : "), input(
            "masukkan harga beli : "), input("masukkan stok : "))

        updateItem(connection, item.getName, item.getSellPrice,
                      item.getPurchasePrice, item.getStock, idItem)
