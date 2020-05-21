import pymysql
class Conexion:
    def __init__(self):
        self._HOST = "localhost"
        self._USER = "root"
        self._PASS = ""
        self._BD = "bdrest1"
    def conecta(self):
        bd = pymysql.connect(self._HOST, self._USER, self._PASS, self._BD, port=3306)
        print("Conexion Exitosa...!")
        return bd
cx = Conexion()
print(cx.conecta())