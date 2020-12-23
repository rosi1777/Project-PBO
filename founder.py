import user
import sqlite3


class Founder(user.User):

    def __init__(self, username, password, nama, gender, alamat, telepon, tanggalMasuk):
        super().__init__(username, password, nama, gender, alamat, telepon, tanggalMasuk)

    def userInfo(self, connection):
        founders = user.getUserFounder(connection)

        for founder in founders:
            print(founder)
