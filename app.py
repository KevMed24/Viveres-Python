from flask import Flask, render_template, request, redirect, url_for
import funciones

app = Flask(__name__)

nombresproduc = [[["" for _ in range(30)] for _ in range(3)] for _ in range(10)]
precio = [0.0] * 10
n = [0]

@app.route('/')
def index():
    funciones.leer_datos("Datos.txt", nombresproduc, precio, n)
    productos = [
        {"nombre": nombresproduc[i][0], "cantidad": nombresproduc[i][1], "fecha": nombresproduc[i][2], "precio": precio[i]}
        for i in range(n[0])
    ]
    return render_template('index.html', productos=productos)

@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form['nombre']
    cantidad = request.form['cantidad']
    fecha = request.form['fecha']
    precio_producto = float(request.form['precio'])
    funciones.agregar_producto(nombre, cantidad, fecha, precio_producto, nombresproduc, precio, n)
    funciones.guardar_datos("Datos.txt", nombresproduc, precio, n[0])
    return redirect(url_for('index'))

@app.route('/editar/<nombre>', methods=['POST'])
def editar(nombre):
    cantidad = request.form['cantidad']
    fecha = request.form['fecha']
    precio_producto = float(request.form['precio'])
    funciones.editar_producto(nombre, cantidad, fecha, precio_producto, nombresproduc, precio, n[0])
    funciones.guardar_datos("Datos.txt", nombresproduc, precio, n[0])
    return redirect(url_for('index'))

@app.route('/eliminar/<nombre>', methods=['POST'])
def eliminar(nombre):
    funciones.eliminar_producto(nombre, nombresproduc, precio, n)
    funciones.guardar_datos("Datos.txt", nombresproduc, precio, n[0])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
