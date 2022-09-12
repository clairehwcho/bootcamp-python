from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route("/")
def index():
    return redirect("/authors")

@app.route("/authors")
def show_all_authors():
    authors = Author.get_all()
    return render_template("authors.html", all_authors=authors)

@app.route("/add_author", methods=["POST"])
def add_author():
    data = {
        "name": request.form["name"]
    }
    Author.save(data)
    return redirect("/authors")


@app.route("/authors/<int:id>")
def show_author(id):
    data = {
        "id": id
    }
    authors_favorites = Author.get_by_id(data)
    # unfavorited_books = Book.unfavorited_books(data)
    return render_template("show_author.html", all_authors_favorites=authors_favorites)

@app.route('/join/book',methods=['POST'])
def join_book():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/author/{request.form['author_id']}")