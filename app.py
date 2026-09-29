from flask import Flask,jsonify,request 
app = Flask(__name__)
@app.route("/home", methods=["GET"])
def home():
    return {"message": "this is home page"} #dictionary :- {"key", "value"}

books = [{"id":1,"name":"Harry Porter", "author":"JK Rowling"},
         {"id":2,"name":"animal farm", "author":"george orwell"}
        ]

#get all the books 
@app.route("/api/books",methods=["GET"])
def books_name():
    return jsonify(books)  #import jsonify from flask 

#post new book 
@app.route("/api/books", methods=["POST"])
def new_books():
    book = request.get_json()
    books.append(book)
    return jsonify(books)


if __name__=="__main__":
    app.run(port=3000)