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


if __name__ == "__main__":
    app.run(debug=True)
