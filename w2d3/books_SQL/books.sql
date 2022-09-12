SELECT * FROM books_schema.books;

-- Query: Create 5 books with the following names: C Sharp, Java, Python, PHP, Ruby
INSERT INTO books(title, num_of_pages)
VALUES("C Sharp", null), ("Java", null), ("Python", null), ("PHP", null), ("Ruby", null);

-- Query: Change the name of the C Sharp book to C#
SET SQL_SAFE_UPDATES = 0;
UPDATE books SET title = "C#"
WHERE title = "C Sharp";