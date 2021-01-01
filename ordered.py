import sqlite3

create_order_table = "CREATE TABLE IF NOT EXISTS order (id INTEGER NOT NULL PRIMARY KEY, namaPemesan TEXT, alamat TEXT, barang TEXT, jumlah INTEGER, tanggalPesan TEXT, status TEXT);"

insert_order = "INSERT INTO order (namaPemesan, alamat, barang, jumlah, tanggalPesan, status) VALUES (?, ?, ?, ?, ?, ?);"

update_order_status = "UPDATE order SET status = 'selesai' WHERE id = ?"

get_order = "SELECT id, namaPemesan, alamat, barang, jumlah, tanggalPesan, status FROM order WHERE status = 'proses'"

get_sales = "SELECT id, namaPemesan, alamat, barang, jumlah, tanggalPesan, status FROM order WHERE status = 'selesai'"

connection = sqlite3.connect("rajaes.db")

def createOrderTable(connection):
    with connection:
        connection.execute(create_order_table)


def addOrder(connection):
    with connection:
        connection.execute(insert_order)


def updateStatus(connection):
    with connection:
        connection.execute(update_order_status)


def getOrder(connection):
    with connection:
        return connection.execute(get_order).fectall()

def getSales(connection):
    with connection:
        return connection.execute(get_sales).fectall()


class Ordered:

    def __init__(self, namaPemesan, alamat, barang, jumlah, tanggalPesan):
        self.__orderName = namaPemesan
        self.__address = alamat
        self.__item = barang
        self.__amount = jumlah
        self.__orderDate = tanggalPesan

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


createOrderTable(connection)
