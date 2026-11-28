#building CRUD API application

#step1  (initialize flask and create in memory)
from flask import Flask , jsonify, request
app = Flask(__name__)

items_db =[
    {"id":1, "name":"mahima"}, {"id":2, "name": "chatterjee"}
]

#step2 (read all items)
@app.route('/items', methods =['GET'])
def get_all_items():
    return jsonify(items_db), 200



#step 3 (get a single item)
@app.route('/items/<int:item_id>', methods=['GET'])
def get_single_item(item_id):
    for item in items_db:
        if item("id")== item_id:
            return jsonify(item), 200
    return jsonify ({"error: item does not exist"}) , 404
    

#step4: create a new item
@app.route('/items', methods= ['POST'])
def create_item():
    data = request.get_json()

    new_item= {
        "id": len(items_db)+1,
        "name": data.get("name")
    }

    items_db.append(new_item)
    return jsonify (new_item), 200



#step5: update an existing item 
@app.route('/items', methods= ['POST'])
def update_item(item_id):
    data = request.get_json()
    for item in item_db():
        if item['id']== item_id:
            item['name']= data.get('name', item('name'))
            return jsonify({"error":"item not found"}), 404



#delete an item 
@app.route('/items/<int: item_id>'), methods=['DELETE']
def delete_item(item_id):
    for item in items_db:
        if item("id")== item_id:
            items_db.remove(item)
            return jsonify({"message":"deleted"})
    return jsonofy ({"error":"item_not_found"})    


if __name__== "__main__":
    app.run(port=3000)



