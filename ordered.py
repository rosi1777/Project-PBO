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


def insertOrder(connection, namaPemesan, alamat, barang, jumlah, tanggalPesan, status):
    with connection:
        connection.execute(insert_order, (namaPemesan, alamat,
                                          barang, jumlah, tanggalPesan, status))


def updateStatus(connection, idStatus):
    with connection:
        connection.execute(update_order_status, (idStatus))


def getOrder(connection):
    with connection:
        return connection.execute(get_order).fetchall()


def getSales(connection):
    with connection:
        return connection.execute(get_sales).fetchall()


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

        insertOrder(connection, order.getOrderName, order.getAddress, order.getItem, order.getAmount, order.getOrderDate, order.getStatus)

    @staticmethod
    def seeOrdered(connection):
        orders = getOrder(connection)

        print("ID \t Nama Pemesan \t\t Alamat \t Barang \t Jumlah \t Tanggal Pesanan  Status")
        for ordered in orders:
            print("{} \t {} \t {} \t {} \t {} \t\t {}       {}".format(ordered[0], ordered[1], ordered[2], ordered[3], ordered[4], ordered[5], ordered[6]))

    @staticmethod
    def addSales(connection):
        idStatus = input("masukkan id : ")

        updateStatus(connection, idStatus)

    @staticmethod
    def seeSale(connection):
        sales = getSales(connection)

        print(
            "ID \t Nama Pemesan \t\t Alamat \t Barang \t Jumlah \t Tanggal Pesanan  Status")
        for sale in sales:
            print("{} \t {} \t {} \t {} \t {} \t\t {}       {}".format(
                sale[0], sale[1], sale[2], sale[3], sale[4], sale[5], sale[6]))
