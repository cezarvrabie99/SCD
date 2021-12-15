from os import abort
from flask import Flask, jsonify, abort, request

app = Flask(__name__)

library = [
    {
        'id': 1,
        'title': u'title book 111111',
        'author': u'author book 1',
        'available': False
    },
    {
        'id': 2,
        'title': u'title book 2',
        'author': u'author book 2',
        'available': True
    }
]


@app.route("/")
def welcome():
    return "Hello to our library!\n"


@app.route("/api/v1/books", methods=['GET'])
def get_books():
    return jsonify({'library': library})


@app.route("/api/v1/books/<int:book_id>", methods=['GET'])
def get_book(book_id):
    book = [book for book in library if book['id'] == book_id]
    if len(book) == 0:
        abort(404)
    return jsonify({'book': book[0]})


@app.route("/api/v1/books", methods=['POST'])
def create_book():
    if not request.json or not 'title' in request.json:
        abort(404)
    book = {
        'id': library[-1]['id'] + 1,
        'title': request.json['title'],
        'author': request.json.get('author', ""),
        'available': True
    }
    library.append(book)
    return jsonify({'book': book}), 201


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
