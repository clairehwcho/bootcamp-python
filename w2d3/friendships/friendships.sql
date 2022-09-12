-- Forward engineer the friendships_schema from the previous chapter: DONE
-- TEST
SELECT * FROM friendships;
SELECT * FROM users;

-- Query: Create 6 new users
INSERT INTO users(first_name,last_name)
VALUES("Amy","Giver"),("Eli","Byers"),("Marky","Mark"),("Big","Bird"),("Kermit","The Frog"),("Anne","Hathaway");

-- Query: Have user 1 be friends with user 2, 4 and 6
-- Query: Have user 2 be friends with user 1, 3 and 5
-- Query: Have user 3 be friends with user 2 and 5
-- Query: Have user 4 be friends with user 3
-- Query: Have user 5 be friends with user 1 and 6
-- Query: Have user 6 be friends with user 2 and 3
INSERT INTO friendships(user_id,friend_id)
VALUES(1,2),(1,4),(1,6),(2,1),(2,3),(2,5),(3,2),(3,5),(4,3),(5,1),(5,6),(6,2),(6,3);

-- Query: Display the relationships created as shown in the table in the above image
SELECT users.first_name, users.last_name, users2.first_name as friend_first_name, users2.last_name as friend_last_name FROM users
JOIN friendships ON friendships.user_id = users.id
LEFT JOIN users as users2 ON users2.id = friendships.friend_id;

-- NINJA Query: Return all users who are friends with the first user, make sure their names are displayed in results.
SELECT users2.first_name as friend_first_name, users2.last_name as friend_last_name FROM users
JOIN friendships ON friendships.user_id  = users.id
LEFT JOIN users as users2 on users2.id = friendships.friend_id
WHERE users.id = 1;

-- NINJA Query: Return the count of all friendships
SELECT COUNT(*) as num_of_friendships from friendships;

-- NINJA Query: Find out who has the most friends and return the count of their friends.
SELECT user_id, users.first_name, users.last_name, count(user_id) as num_of_friends from friendships
JOIN users ON friendships.user_id = users.id
GROUP BY user_id
ORDER BY num_of_friends DESC
LIMIT 1;

-- NINJA Query: Return the friends of the third user in alphabetical order
SELECT users2.first_name as friend_first_name, users2.last_name as friend_last_name FROM users
JOIN friendships ON friendships.user_id = users.id
LEFT JOIN users as users2 ON users2.id = friendships.friend_id
WHERE users.id = 3
ORDER BY users.first_name ASC;