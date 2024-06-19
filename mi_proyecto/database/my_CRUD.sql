CREATE TABLE autos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    marca VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    anio YEAR NOT NULL
);


-- CREATE
INSERT INTO autos (marca, modelo, anio)
VALUES ('Toyota', 'Corolla', 2022);

-- READ
SELECT * FROM autos;

-- UPDATE
UPDATE autos
SET marca = 'Honda', modelo = 'Accord', anio = 2023
WHERE id = 1;

-- DELETE 
DELETE FROM autos WHERE id = 1;
