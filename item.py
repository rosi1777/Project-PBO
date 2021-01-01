import sqlite3

create_Item = "create table if not exist Item (id integer not null primary key, nama text , hargaJual integer, hargaBeli integer, stok integer );"

insert_Item = "insert into Item(nama, hargaJual, hargaBeli, stok)values (?,?,?,?);"

get_Item = "select * from Item"


def connect():
    return sqlite3.connect("rajaes.db")


def createItemTable(connection):
    with connection:
        connection.execute(create_Item)


def addItem(connection, nama, hargaJual, hargaBeli, stok):
    with connection:
        connection.execute(
            insert_Item, (nama, hargaJual, hargaBeli, stok)
        )


def getAllItem(connection):
    with connection:
        return connection.execute(get_Item).fetchall()


class Item:

    def __init__(self, id, nama, hargaJual, hargaBeli, stok):
        self.id = id
        self.name = nama
        self.sellPrice = hargaJual
        self.purchasePrice = hargaBeli
        self.stock = stok

    def promtAddItem(self, connection):
        Item = Item(input('masukkan nama barang:'),
                    input('masukkan harga jual  barang:'), input('masukkan harga beli barang:'), input('masukkan stok:'))

    def itemInfo(self, connection):
        Item = getAllItem(connection)

        for item_Info in Item:
            print(item_Info)
