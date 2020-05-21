import pymysql 
from conexion import Conexion
from sqlalchemy import create_engine
from json import dumps
cx = Conexion()

class Cliente:
    idcliente = 0
    nombres = ""
    apellidos= ""
    dni = "" 
    correo=""
    direccion=""
    telefono=""

    def readAll(self):
        try:
            conexion=cx.conecta()
            cursor = conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc('listar_cliente')
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print(e)
        finally:
            conexion.close()
    def delete(self):
        try:
            conexion=cx.conecta()
            cursor=conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc('delete_cliente',[self.idcliente])
            conexion.commit()
            return 1
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conexion.close()
    def createcliente(self):
        nombres=self.nombres
        apellidos=self.apellidos
        dni=self.dni
        correo=self.correo
        direccion=self.direccion
        telefono=self.telefono
        data=[nombres,apellidos,dni,correo,direccion,telefono]
        try:
            conexion=cx.conecta()
            cursor=conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc("CREATE_CLIENTE",data)
            conexion.commit()
            return 1
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conexion.close()
    def searchcliente(self):
        try:
            conexion = cx.conecta()
            cursor=conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc('read_cliente',[self.idcliente])
            rows=cursor.fetchall()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conexion.close()
    def editcliente(self):
        try:
            idc=self.idcliente
            nombres=self.nombres
            apellidos=self.apellidos
            dni=self.dni
            correo=self.correo
            direccion=self.direccion
            telefono=self.telefono
            data=[nombres,apellidos,dni,correo,direccion,telefono,idc]
            conexion=cx.conecta()
            cursor=conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc("update_cliente",data)
            conexion.commit()
            return 1
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conexion.close()


