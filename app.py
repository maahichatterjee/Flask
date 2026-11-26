#building CRUD API application

#step1  (initialize flask and create in memory)
from flask import Flask, jsonify, request
app = Flask(__name__)

items_db =[{"id":1, "name":"john"}, {"id":2, "name":"doe"}]
#step2 (read all items)

@app.route("/items",methods=["GET"])
def items():
    return jsonify(items_db)

#step 3 (get a single item)
@app.route("/items/<int:id>", methods=["GET"])
def get_single_item(id):
    for item in items_db:
        if item["id"]==id:
            return jsonify(item)

    return {"message":"item not found"}



#step4: get data from client and add it to the in memory db
@app.route("/items", methods=["POST"])
def post_item():
    data = request.get_json()           #get data from clint

    new_data= {
        "id": len(items_db)+1,
        "name": data.get("name")
    }

    items_db.append(new_data)
    return jsonify(items_db)


if __name__=="__main__":
    app.run(port=3000)