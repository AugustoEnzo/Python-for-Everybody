CREATE TABLE Users (
    name VARCHAR(128),
    email VARCHAR(128)
)

INSERT INTO Users(name, email) VALUES ('Kristin', 'kf@umich.edu')

DELETE FROM Users WHERE email='ted@umich.edu'

UPDATE Users SET name='Charles' WHERE email='csev@umich.edu'

SELECT * FROM Users WHERE email='csev@umich.edu'

SELECT * FROM Users ORDER BY email

INSERT INTO Track (title, rating, len, count, album_id, genre_id) VALUES ('Black Dog', 5, 297, 0, 2, 1);
INSERT INTO Track (title, rating, len, count, album_id, genre_id) VALUES ('Stairway', 5, 482, 0, 2, 1);
INSERT INTO Track (title, rating, len, count, album_id, genre_id) VALUES ('About to Rock', 5, 313, 0, 1, 2);
INSERT INTO Track (title, rating, len, count, album_id, genre_id) VALUES ('Who Made Who', 5, 207, 0, 1, 2);

SELECT Album.title, Artist.name FROM Album JOIN Artist ON Album.artist_id = Artist.id

SELECT Track.title, Genre.name FROM Track JOIN Genre ON Track.genre_id = Genre.id

SELECT Track.title, Track.genre_id, Genre.id, Genre.name FROM Track JOIN Genre

SELECT Track.title, Artist.name, Album.title, Genre.name FROM Track JOIN Genre JOIN Album JOIN Artist ON Track.genre_id = Genre.id AND
Track.album_id = Album.id AND Album.artist_id = Artist.id