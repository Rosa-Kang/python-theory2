# Database Design
# Never put the same string of data more than once.**
# What is the best practice for how many times a piece of string data should be stored in a database? 1
# What is a foreign key?
# A number that points to the primary key of an associated row in a different table.
# Three Kinds of Keys.
# 1. Primary key - generally an integer auto-increment field
# 2. Logical key - what the outside world uses for lookup
# 3. Foreign key - generally an integer key pointing to a row in another table.


# What does the INSERT command do in SQL?   
# It defines a new row by listing the fields we want to include followed by the values we want to placed in the new row.


#Many to Many relationships
from inspect import CORO_SUSPENDED


CREATE  TABLE  User (
id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name  TEXT UNIQUE,
    email  TEXT
);
    

CREATE  TABLE  Course (
id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);
    

CREATE  TABLE  Member (
user_id  INTEGER,
    course_id  INTEGER,
    role  INTEGER,
    PRIMARY KEY (user_id, course_id)
);
    
INSERT INTO User (name, email) VALUES ('Jane', 'jane@gmail.com');
INSERT INTO User (name, email) VALUES ('Tonny', 'tonny@gmail.com');
INSERT INTO User (name, email) VALUES ('Kate', 'kate@gmail.com');

INSERT INTO Course (title) VALUES ('Python');
INSERT INTO Course (title) VALUES ('SQL');
INSERT INTO Course (title) VALUES ('PHP');

INSERT INTO Member (user_id, course_id, role) VALUES (1, 1, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (2, 1, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (3, 1, 0);

INSERT INTO Member (user_id, course_id, role) VALUES (1, 2, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (2, 2, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (2, 3, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (3, 3, 0);

SELECT User.name, Member.role, Course.title
FROM User JOIN Member JOIN Course
ON Member.user_id = User.id AND
Member.course_id = Course.id
ORDER BY Course.title, Member.role DESC, User.name