# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

# model the class after the friend table from our database
class Author:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorite_books = []

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('books_schema').query_db(query)
        # Create an empty list to append our instances of friends
        authors = []
        # Iterate over the db results and create instances of friends with cls.
        for row in results:
            authors.append( cls(row) )
        return authors

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO authors (name) VALUES (%(name)s);"
        # data is a dictionary that will be passed into the save method from server.py
        result = connectToMySQL('books_schema').query_db( query, data )
        return result

    @classmethod
    def unfavorited_authors(cls,data):
        query = "SELECT * FROM authors WHERE authors.id NOT IN ( SELECT author_id FROM favorites WHERE book_id = %(id)s );"
        authors = []
        results = connectToMySQL('books_schema').query_db(query,data)
        for row in results:
            authors.append(cls(row))
        return authors

    @classmethod
    def add_favorite(cls,data):
        query = "INSERT INTO favorites (author_id,book_id) VALUES (%(author_id)s,%(book_id)s);"
        return connectToMySQL('books_schema').query_db(query,data)


    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON books.id = favorites.book_id WHERE authors.id = %(id)s;"
        results = connectToMySQL('books_schema').query_db(query,data)
        # Creates instance of author object from row one
        author = cls(results[0])
        # append all book objects to the instances favorites list.
        for row in results:
            # if there are no favorites
            if row['books.id'] == None:
                break
            # common column names come back with specific tables attached
            data = {
                "id": row['books.id'],
                "title": row['title'],
                "num_of_pages": row['num_of_pages'],
                "created_at": row['books.created_at'],
                "updated_at": row['books.updated_at']
            }
            author.favorite_books.append(book.Book(data))
        return author


