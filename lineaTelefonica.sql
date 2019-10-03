CREATE DATABASE lineaTelefonica;
USE lineaTelefonica;

CREATE TABLE persona (
perId INT PRIMARY KEY NOT NULL,
perNombre VARCHAR(50),
perApellido VARCHAR(50),
perTelefonoFijo VARCHAR(20),
perFechaNacimiento DATE,
perCedula VARCHAR(20)
);

CREATE TABLE linea (
liNumeroLinea VARCHAR(30) PRIMARY KEY NOT NULL,
perId INT,
linEstado VARCHAR(20),
FOREIGN KEY (perId) REFERENCES persona(perId)
);

CREATE TABLE equipo(
equSerial INT(11) PRIMARY KEY NOT NULL,
liNumeroLinea VARCHAR(30),
equMarca VARCHAR(50),
equDescripcion VARCHAR(50),
equEstado VARCHAR(50),
FOREIGN KEY (liNumeroLinea) REFERENCES linea(liNumeroLinea)
);

CREATE TABLE factura(
facNumero INT(11) PRIMARY KEY NOT NULL,
liNumeroLinea VARCHAR(30),
facFechaEmision DATE,
facValor DECIMAL,
FOREIGN KEY (liNumeroLinea) REFERENCES linea(liNumeroLinea)
);