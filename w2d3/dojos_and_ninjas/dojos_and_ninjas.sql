-- Query: Create 3 new dojos
INSERT INTO dojos(name) VALUES("dojo1");
INSERT INTO dojos(name) VALUES("dojo2");
INSERT INTO dojos(name) VALUES("dojo3");

-- Query: Delete the 3 dojos you just created
DELETE FROM dojos WHERE id BETWEEN 4 AND 6;

-- Query: Create 3 more dojos
INSERT INTO dojos(name) VALUES("dojo1");
INSERT INTO dojos(name) VALUES("dojo2");
INSERT INTO dojos(name) VALUES("dojo3");

-- Query: Create 3 ninjas that belong to the first dojo
INSERT INTO ninjas(first_name,last_name,age,dojo_id)
VALUES("Claire","Cho",31,4);
INSERT INTO ninjas(first_name,last_name,age,dojo_id)
VALUES("Smith","Lee",20,4),("Jane","Addison",39,4);

-- Query: Create 3 ninjas that belong to the second dojo
INSERT INTO ninjas(first_name,last_name,age,dojo_id)
VALUES("Ninja4","Four",35,5),
("Ninja5","Five",29,5),
("Ninja6","Six",38,5);

-- Query: Create 3 ninjas that belong to the third dojo
INSERT INTO ninjas(first_name,last_name,age,dojo_id)
VALUES("Ninja7","Seven",35,6),
("Ninja8","Eight",29,6),
("Ninja9","Nine",38,6);

-- Query: Retrieve all the ninjas from the first dojo
SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = 4;

-- Query: Retrieve all the ninjas from the last dojo
SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojo_id = (SELECT id FROM dojos ORDER BY id DESC Limit 1);
-- DESC means that the order will be descending (largest values first). LIMIT 1 means only return at most one result

-- Query: Retrieve the last ninja's dojo
SELECT * FROM dojos WHERE dojos.id = (SELECT dojo_id FROM ninjas ORDER BY ninjas.id DESC LIMIT 1);