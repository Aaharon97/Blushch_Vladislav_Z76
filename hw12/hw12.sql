use lesson12;

CREATE TABLE laptop2(
	code INT,
    model VARCHAR(50),
    speed SMALLINT,
    ram SMALLINT,
    hd REAL,
    price FLOAT,
    screen INT
);

INSERT INTO laptop2(code, model, speed, ram, hd, price, screen)
VALUES(1, "Dell", 150, 8, 100, 200, 1080);

INSERT INTO laptop2(code, model, speed, ram, hd, price, screen)
VALUES(2, "shell", 200, 16, 999, 500, 1080);

INSERT INTO laptop2(code, model, speed, ram, hd, price, screen)
VALUES(3, "samsung", 150, 64, 2000, 100, 1080);

INSERT INTO laptop2(code, model, speed, ram, hd, price, screen)
VALUES(4, "Lenovo", 600, 640, 10000, 5000, 10800);

SELECT * FROM laptop2 WHERE price <= 400

SET SQL_SAFE_UPDATES = 0;

SELECT code, model, speed, ram FROM laptop2 WHERE ram BETWEEN 8 and 16;

SELECT price FROM laptop2 WHERE hd < 1000;

-- UPDATE laptop2

SELECT * FROM laptop2 WHERE price >= 400;
UPDATE laptop2 SET price = price * 2;



