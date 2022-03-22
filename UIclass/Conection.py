import mysql.connector


class Conection():
    """Controla la conexion a la base de datos"""

    def newConnection():
        """Crea una nueva conexion a la base de datos"""
        con = mysql.connector.connect(host="localhost", port=3307, user="root", passwd="abc123.", database="eztest")
        return con
