-- Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS miapp;
-- Usar la base de datos
USE miapp;
-- Crear la tabla de Productos si no existe
CREATE TABLE IF NOT EXISTS peliculas (
    codigo INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    genero VARCHAR(255) NOT NULL,
    duracion VARCHAR(10) NOT NULL,
    fecha_estreno DATE NOT NULL,
    directores TEXT NOT NULL
);