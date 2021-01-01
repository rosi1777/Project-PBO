from user import connection

create_Item = "CREATE TABLE IF NOT EXISTS item (id INTEGER NOT NULL PRIMARY KEY, nama text , hargaJual integer, hargaBeli integer, stok integer );"

insert_Item = "INSERT INTO item (nama, hargaJual, hargaBeli, stok) VALUES ('Jelly', 10000, 7000, 100), ('Cincau', 5000, 7000, 70), ('Mutiara', 12000, 8000, 77), ('Rumput Laut', 20000, 15000, 150), ('Kolang Kaling', 15000, 13000, 177);"

def createItemTable(connection):
    with connection:
        connection.execute(create_Item)

def insertItem(connection):
    with connection:
        connection.execute(insert_Item)

def addItem(connection, nama, hargaJual, hargaBeli, stok):
    with connection:
        connection.execute(
            insert_Item, (nama, hargaJual, hargaBeli, stok)
        )

class Item:

    def __init__(self, nama, hargaJual, hargaBeli, stok):
        self.name = nama
        self.sellPrice = hargaJual
        self.purchasePrice = hargaBeli
        self.stock = stok

