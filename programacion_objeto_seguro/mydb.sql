CREATE DATABASE prueba0210;

CREATE TABLE libro(
    codigo VARCHAR(50) PRIMARY KEY,
    titulo VARCHAR(50),
    autor VARCHAR(50),
    precio INT,
    stock INT
);

CREATE TABLE cliente(
    rut VARCHAR(15) PRIMARY KEY,
    nombre VARCHAR(50),
    email VARCHAR(50),
    telefono VARCHAR(12)
);

CREATE TABLE libreria(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    direccion VARCHAR(50)
);

CREATE TABLE venta(
    id_venta INT AUTO_INCREMENT PRIMARY KEY,
    rut VARCHAR(15),
    codigo VARCHAR(50),
    cantidad INT,
    total INT
    FOREIGN KEY(rut) REFERENCES cliente(rut),
    FOREIGN KEY(codigo) REFERENCES libro(codigo)
);

