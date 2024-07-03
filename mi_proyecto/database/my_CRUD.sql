CREATE TABLE cars (
    id INT AUTO_INCREMENT PRIMARY KEY,
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year YEAR NOT NULL
);


-- CREATE
INSERT INTO cars (make, model, year) VALUES ('Toyota', 'Corolla', 2020);
INSERT INTO cars (make, model, year) VALUES ('Honda', 'Civic', 2019);
INSERT INTO cars (make, model, year) VALUES ('Ford', 'Mustang', 2021);
INSERT INTO cars (make, model, year) VALUES ('Chevrolet', 'Malibu', 2018);
INSERT INTO cars (make, model, year) VALUES ('Nissan', 'Altima', 2022);
