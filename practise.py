#building CRUD API application
#
#1. import flask and initialize app 
from flask import Flask ,jsonify, request
app = Flask(__name__)

items_db= [
    {'id':1,'name':"mahima"},
    {"id":2, "name":"chatterjee"}
]


#2. read all items (get)
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items_db)


#3. read a single item (get)
@app.route('/items/<int:item_id>' , methods=['GET'])
def get_single_item(item_id):
    for item in items_db:
        if item("id")== item_id :
            return jsonify(item)
    return jsonify({"message":"item not found"})


#4. create a new item (post)
@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()

    new_item= {
        "id":len(items_db)+1,
        "name": data.get("name")
    }
    items_db.append(new_item)
    return jsonify(new_item)


#5. update an existing item(put)
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()

    for item in items_db:
        if item["id"]==  item_id:
            item["name"]=data.get("name", item["name"])
            return jsonify(item)
    return jsonify({"message":"item not found"})


#6.delete an item (delete)
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    for item in items_db:
        if item["id"]== item_id:
            items_db.remove(item)
            return jsonify({"message":"deleted the item"})
    return jsonify({"message":"items not found"})


if __name__=='__main__':
    app.run(debug=True)
