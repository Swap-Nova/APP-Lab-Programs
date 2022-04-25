-- creating a table

CREATE TABLE movie (

    Movie_ID INTEGER PRIMARY KEY,
    Movie_Name TEXT NOT NULL,
    Genre TEXT NOT NULL,
    Language TEXT NOT NULL,
    Rating DOUBLE NOT NULL
);

-- inserting the values

INSERT INTO movie VALUES ('101','The Arrival','Sci-fi','English','3.8');
INSERT INTO movie VALUES ('102','Dune','Sci-fi','English','4.8');
INSERT INTO movie VALUES ('103','Crazy Stupid Love','Relationship','English','4.0');
INSERT INTO movie VALUES ('104','The 40 Year Old Virgin','Comedy','English','3.9');
INSERT INTO movie VALUES ('105','RIPD','Comedy','English','2.5');

-- fetching the values

SELECT * FROM movie;

-- using various conditions in our table

UPDATE movie SET Rating=Rating+0.1;
DELETE FROM movie WHERE Movie_ID='102';
SELECT * FROM movie WHERE Rating>3;