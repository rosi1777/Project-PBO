import sqlite3

create_Ordered_Table = "CREATE TABLE IF NOT EXISTS ordered (id INTEGER NOT NULL PRIMARY KEY, namaPemesan TEXT, alamat TEXT, barang TEXT, jumlah INTEGER, tanggalPesan TEXT, status TEXT);"

insert_order = "INSERT INTO ordered (namaPemesan, alamat, barang, jumlah, tanggalPesan, status) VALUES (?, ?, ?, ?, ?, ?);"

update_order_status = "UPDATE ordered SET status = 'selesai' WHERE id = ?"

get_order = "SELECT id, namaPemesan, alamat, barang, jumlah, tanggalPesan, status FROM ordered WHERE status = 'proses'"

get_sales = "SELECT id, namaPemesan, alamat, barang, jumlah, tanggalPesan, status FROM ordered WHERE status = 'selesai'"

connection = sqlite3.connect("rajaes.db")

def createOrderTable(connection):
    with connection:
        connection.execute(create_Ordered_Table)


def addOrder(connection, namaPemesan, alamat, barang, jumlah, tanggalPesan, status):
    with connection:
        connection.execute(insert_order, (namaPemesan, alamat, barang, jumlah, tanggalPesan, status))


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
