from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route("/books")
def show_all_books():
    books = Book.get_all()
    return render_template("books.html", all_books=books)

@app.route("/add_book", methods=["POST"])
def add_book():
    data = {
        "title": request.form["title"],
        "num_of_pages": request.form["num_of_pages"]
    }
    book_id = Book.save(data)
    return redirect("/books")

@app.route('/book/<int:id>')
def show_book(id):
    data = {
        "id":id
    }
    books_favorites = Book.get_by_id(data)
    unfavorited_authors = Author.unfavorited_authors(data)
    return render_template('show_book.html',all_books_favorites=books_favorites, unfav_authors=unfavorited_authors)

@app.route('/join/author',methods=['POST'])
def join_author():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/book/{request.form['book_id']}")