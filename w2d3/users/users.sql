INSERT INTO users(first_name, last_name, email) VALUES('Claire','Cho','cc@email.com');
INSERT INTO users(first_name, last_name, email) VALUES('John','Doe','jd@email.com');
INSERT INTO users(first_name, last_name, email) VALUES('Janice','Lee','jl@email.com');

SELECT * FROM users;

SELECT * FROM users WHERE email = "cc@email.com";

SELECT * FROM users WHERE id = 3;

UPDATE users SET last_name = "Pancakes" WHERE id = 3;

DELETE FROM users WHERE id = 2;

SELECT * FROM users ORDER BY first_name DESC;