#building CRUD API application

#step1  (initialize flask and create in memory)
from flask import Flask, jsonify
app = Flask(__name__)

items_db=[{"id":1, "name":"Mahima"},{"id":2, "name":"Kumar"}]
print(items_db)
#step2 (read all items)
@app.route("/items", methods=["GET"])
def items():
    return jsonify(items_db)

#step 3 (get a single item)
@app.route("/items/<int:item_id>", methods=["GET"])
def get_single_item(item_id):
    for item in items_db:
        if item["id"]==item_id:
            return jsonify(item)
    return jsonify({"message":"error"})    


if __name__=="__main__":
    app.run(port=3000)
