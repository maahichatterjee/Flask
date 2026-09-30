#building CRUD API application

#step1  (initialize flask and create in memory)
from flask import Flask, jsonify
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

if __name__=="__main__":
    app.run(port=3000)