from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from http import HTTPStatus

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/books_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False)


def find_book(book_id):
    return Book.query.get(book_id)


@app.route("/")
def hello_user():
    return "Hello, User!"

@app.route("/api/books", methods=["GET"])
def get_books():
    books = Book.query.all()
    books_data = [{"id": book.id, "title": book.title, "author": book.author, "year": book.year} for book in books]
    return jsonify({"success": True, "data": books_data, "total": len(books_data)}), HTTPStatus.OK


@app.route("/api/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = find_book(book_id)
    if book is None:
        return (
            jsonify({"success": False, "error": "Book not found"}),
            HTTPStatus.NOT_FOUND,
        )
    book_data = {"id": book.id, "title": book.title, "author": book.author, "year": book.year}
    return jsonify({"success": True, "data": book_data}), HTTPStatus.OK

if __name__ == "__main__":
    app.run(debug=True)
