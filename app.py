from flask import Flask 
app = Flask(__name__)
@app.route("/home", methods=["GET"])
def home():
    return {"message": "this is home page"} #dictionary :- {"key", "value"}

if __name__=="__main__":
    app.run(port=3000)