tabla_stats
CREATE SCHEMA MusicStream;
USE MusicStream;


# Tabla_genero (4 generos): 
# id_genero(PK) 
# genero 

	CREATE TABLE Tabla_genero (
    id_genero INT AUTO_INCREMENT PRIMARY KEY,
    genero VARCHAR(20) NOT NULL);


# Tabla_artista (csv track):
# id_artista (PK)
# nombre_artista

	CREATE TABLE Tabla_artista (
    id_artista INT AUTO_INCREMENT PRIMARY KEY,
    id_genero INT,
    nombre_artista VARCHAR(50) NOT NULL,
    album VARCHAR(100) NOT NULL,
    fecha DATE,
    tipo VARCHAR(10) NOT NULL,
    track VARCHAR(100) NOT NULL,
    CONSTRAINT fk_id_genero FOREIGN KEY (id_genero) REFERENCES Tabla_genero(id_genero)
);

# Tabla_stats:
# id_stats(PK)
# oyentes
# reproduccion
# CONSTRAINT
# id_genero (FK)
# nombre_artista (FK)

	CREATE TABLE Tabla_stats (
    id_stats INT AUTO_INCREMENT PRIMARY KEY,
    id_genero INT,
    id_artista INT,
    nombre_artista VARCHAR(50),
    oyentes INT NOT NULL,
    reproduccion INT NOT NULL,
    CONSTRAINT fk_id_genero_stats FOREIGN KEY (id_genero) REFERENCES Tabla_genero(id_genero),
    CONSTRAINT fk_id_artista FOREIGN KEY (id_artista) REFERENCES Tabla_artista(id_artista)
);


# Tabla_similar:
# id_similar (PK)
# artista
# similares
# CONSTRAINT
# id_genero (FK)

    CREATE TABLE Tabla_Similar (
    id_similar INT AUTO_INCREMENT PRIMARY KEY,
    id_genero INT,
    artista VARCHAR(50) NOT NULL,
    similares VARCHAR(50) NOT NULL,
    CONSTRAINT fk_id_genero_similar FOREIGN KEY (id_genero) REFERENCES Tabla_genero(id_genero)
);


# Tabla_bio
# id_bio (PK)
# artist
# bio

    CREATE TABLE Tabla_bio (
    id_bio INT AUTO_INCREMENT PRIMARY KEY,
    artista VARCHAR(50) NOT NULL,
    bio VARCHAR (500) NOT NULL);
    



