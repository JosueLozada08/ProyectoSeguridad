# EJECUTAR COMANDO = pip install flask
from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de datos temporal en memoria
items = []

@app.route('/')
def root():
    return 'Hola mundo xd'

# GET: Obtener todos los elementos
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# POST: Agregar un nuevo elemento
@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.json
    items.append(new_item)
    return jsonify(new_item), 201

# PUT: Actualizar un elemento existente
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    updated_item = request.json
    for item in items:
        if item['id'] == item_id:
            item.update(updated_item)
            return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

# DELETE: Eliminar un elemento existente
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return '', 204

#app = Flask(__name__) ##creacion de una instancia 
if __name__ == "__main__":#verifica si el script se está ejecutando directamente desde el intérprete de Python.
    app.run(debug=True) #Inicia el servidor web integrado de Flask.