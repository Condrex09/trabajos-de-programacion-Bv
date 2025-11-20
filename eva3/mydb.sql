CREATE DATABASE veterinaria_poo_Gomez;

CREATE TABLE consulta(
    id_consulta INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE,
    motivo VARCHAR(255),
    id_mascota INT,
    id_veterinario INT,
    observaciones VARCHAR(255),
    FOREIGN KEY(id_mascota) REFERENCES mascota(id_mascota),
    FOREIGN KEY(id_veterinario) REFERENCES veterinario(id_veterinario)
);
CREATE TABLE dueno(
    id_dueno INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(50),
    telefono VARCHAR(50),
    correo VARCHAR(100)
);
CREATE TABLE mascota(
    id_mascota INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    especie VARCHAR(50),
    raza VARCHAR(50)
    id_dueno INT,
    FOREIGN KEY(id_dueno) REFERENCES dueno(id_dueno)
);
CREATE TABLE usuario(
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(50),
    contrasena VARCHAR(255),
    rol VARCHAR(20)
);
CREATE TABLE veterinario(
    id_veterinario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    especialidad VARCHAR(100)
);