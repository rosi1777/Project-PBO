from user import connection

create_Item = "CREATE TABLE IF NOT EXISTS item (id INTEGER NOT NULL PRIMARY KEY, nama text , hargaJual integer, hargaBeli integer, stok integer );"

insert_Item = "INSERT INTO item (nama, hargaJual, hargaBeli, stok) VALUES ('Jelly', 10000, 7000, 100), ('Cincau', 5000, 7000, 70), ('Mutiara', 12000, 8000, 77), ('Rumput Laut', 20000, 15000, 150), ('Kolang Kaling', 15000, 13000, 177);"

def createItemTable(connection):
    with connection:
        connection.execute(create_Item)

def insertItem(connection):
    with connection:
        connection.execute(insert_Item)
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

