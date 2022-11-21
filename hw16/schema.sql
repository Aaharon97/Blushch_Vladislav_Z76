DROP TABLE IF EXISTS unames;

CREATE TABLE unames (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    registration_date DATE
);
