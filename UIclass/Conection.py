import mysql.connector


class Conection():
    def newConnection():
        con = mysql.connector.connect(host="localhost", port=3307, user="root", passwd="abc123.", database="eztest")
        return con
