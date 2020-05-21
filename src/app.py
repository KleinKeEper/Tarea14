from flask import Flask, jsonify, request, make_response
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine
from json import dumps
from UsuarioDAO import Usuario
from ProductoDao import Producto
from ClienteDao import Cliente
produ = Producto()
user = Usuario()
clientes = Cliente()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def listar():
    return jsonify({'mensaje': 'Bienvenidos a Flask'})

@app.route('/usuario/listar', methods=['GET'])
def users():
    try:
        rows = user.readAll()
        respuesta = jsonify(rows)
        respuesta.status_code = 200
        return respuesta
    except Exception as e:
        print(e)

@app.route('/usuario/buscar/<int:id>')
def buscarescuela(id):
	try:
		user.idusuario = id
		row = user.buscarusuario()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)

@app.route('/usuario/create', methods=['POST'])
def agregarusuario():
    try:
        _json = request.json
        user.nomuser=_json['nomuser']
        user.clave=_json['pass']
        if request.method=='POST':
            resp=user.agregarusuario()
            resp=jsonify('USUARIO')
            resp.status_code=200
        return resp
    except Exception as e:
        print(e)

@app.route('/usuario/eliminar/<int:id>', methods=['GET'])
def eliminarusuario(id):
    try:
        user.idusuario=id
        resp=user.delete()
        resp=jsonify('Usuario Elimindado')
        resp.status_code=200
        return resp
    except Exception as e:
        print(e)    
@app.route('/usuario/modificar', methods=['PUT'])
def modificarusuario():
    try:
        _json=request.json
        user.nomuser=_json['nomuser']
        user.clave=_json['pass']
        user.idusuario=_json['iduser']
        if request.method == 'PUT':
            resp = user.modificarusuario()
            resp = jsonify('Usuario Modificada')
            resp.status_code=200
            return resp
    except Exception as e:
        print(e)



        
@app.route('/producto/listar', methods=['GET'])
def produs():
    try:
        rows = produ.readAll()
        respuesta = jsonify(rows)
        respuesta.status_code= 200
        return respuesta
    except Exception as e:
        print(e)

@app.route('/producto/create', methods=['POST'])
def agregarproducto():
    try:
        _json = request.json
        produ.nomproducto=_json['nomproducto']
        produ.precio=_json['precio']
        produ.cantidad=_json['cantidad']
        print(produ.cantidad)
        if request.method=='POST':
            resp=produ.agregarproducto()
            resp=jsonify('PRODUCTO')
            print("en el porst")
            resp.status_code=200
        return resp
    except Exception as e:
        print(e)

@app.route('/producto/delete/<int:id>', methods=['GET'])
def eliminarproducto(id):
    try:
        produ.idproducto=id
        resp=produ.delete()
        resp=jsonify('Producto Eliminado')
        resp.status_code=200
        return resp
    except Exception as e:
        print(e)

@app.route('/producto/edit', methods=['PUT'])
def modificarproducto():
    try:
        _json=request.json
        produ.nomproducto=_json['nomproducto']
        produ.precio=_json['precio']
        produ.cantidad=_json['cantidad']
        produ.idproducto=_json['idproducto']
        if request.method == 'PUT':
            resp = produ.edit()
            resp= jsonify('Producto Modificado')
            resp.status_code=200
            return resp
    except Exception as e:
        print(e)

@app.route('/producto/search/<int:id>')
def buscarproducto(id):
    try:
        produ.idproducto = id
        row = produ.searchproducto()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)




@app.route('/cliente/listar',methods=['GET'])
def clientesl():
    try:
        rows = clientes.readAll()
        respuesta = jsonify(rows)
        respuesta.status_code = 200
        return respuesta
    except Exception as e:
        print(e)
    
@app.route('/cliente/create', methods=['POST'])
def agregarcliente():
    print("Hola voy a crear")
    try:
        _json = request.json
        clientes.nombres = _json['nombres']
        clientes.apellidos = _json['apellidos']
        clientes.dni = _json['dni']
        clientes.correo= _json['correo']
        clientes.direccion= _json['direccion']
        clientes.telefono = _json['telefono']
        if request.method=='POST':
            resp=clientes.createcliente()
            resp=jsonify('CLIENTE CREADO')
            resp.status_code = 200
        return resp
    except Exception as e:
        print(e)


@app.route('/cliente/delete/<int:id>', methods=['GET'])
def eliminarcliente(id):
    try:
        clientes.idcliente=id
        resp=clientes.delete()
        resp=jsonify('Cliente Eliminadi')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

@app.route('/cliente/edit',methods=['PUT'])
def modificarcliente():
    try:
        _json=request.json
        clientes.nombres = _json['nombres']
        clientes.apellidos = _json['apellidos']
        clientes.dni = _json['dni']
        clientes.correo = _json['correo']
        clientes.direccion = _json['direccion']
        clientes.telefono = _json['telefono']
        clientes.idclientes = _json['idcliente']
        if request.method == 'PUT':
            resp = clientes.editcliente()
            resp = jsonify('Cliente Modificado')
            resp.status_code = 200
            return resp
    except Exception as e:
            print(e)


@app.route('/cliente/search/<int:id>')
def buscarclientes(id):
    try:
        clientes.idcliente = id
        row = clientes.searchcliente()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)




if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)    

