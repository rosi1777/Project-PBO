import sqlite3

create_order_table = "CREATE TABLE IF NOT EXISTS Order(id INTEGER NOT NULL PRIMARY KEY, namaPemesan TEXT, alamat TEXT, barang TEXT, jumlah INTEGER, tanggalPesan TEXT, status TEXT)"

insert_order = "INSERT INTO Order (namaPemesan, alamat, barang, jumlah, tanggalPesan, status) VALUES('Subagyo','Probolinggo','cincau',30,12-12-2020,'proses'),('Muzakir','Lumajang','mutiara',25,3-9-2020,'proses')"

update_order = "UPDATE Order SET namaPemesan=?, alamat=?, barang=?, jumlah=?, tanggalPesan=?"

update_order_status = "UPDATE Order SET status='selesai"

get_order = "SELECT * FROM Order"

connection = sqlite3.connect('rajaes.db')


def createOrderTable(connection):
    with connection:
        connection.execute(create_order_table)


def addOrder(connection):
    with connection:
        connection.execute(insert_order)


def updateOrder(connection):
    with connection:
        connection.execute(update_order)


def updateStatus(connection):
    with connection:
        connection.execute(update_order_status)


def getOrder(connection):
    with connection:
        return connection.execute(get_order).fectall()


class Ordered:

    def __init__(self, id, namaPemesan, alamat, barang, jumlah, tanggalPesan):
        self.id = id
        self.orderName = namaPemesan
        self.address = alamat
        self.item = barang
        self.amount = jumlah
        self.orderDate = tanggalPesan
