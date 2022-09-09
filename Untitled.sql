CREATE TABLE `usuarios` (
  `id` integer PRIMARY KEY,
  `nombre` varchar(255),
  `edad` integer,
  `genero` varchar(20),
  `tel` integer
);


# seleccionar uno en esepcial
SELECT * FROM usuarios WHERE id=1;

# Seleccionar todos 
SELECT * FROM usuarios;

# actualizar una columna

UPDATE usuarios set nombre = "Alvaro" WHERE id = 3;

# muchos
UPDATE usuarios set nombre = "Avaro", edad = 19, genero = "Binario", tel = 1321321 WHERE id = 3;

#Eliminar un registro

DELETE FROM usuarios WHERE nombre = "Kevin"; #o puede ser id = 1;