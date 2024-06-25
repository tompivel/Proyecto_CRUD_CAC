import mysql.connector
class Catalogo:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
        self.cursor = self.conn.cursor(dictionary=True)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS peliculas (
            codigo INT AUTO_INCREMENT PRIMARY KEY,
            titulo VARCHAR(255) NOT NULL,
            genero VARCHAR(255) NOT NULL,
            duracion VARCHAR(10) NOT NULL,
            fecha_estreno DATE NOT NULL,
            directores TEXT NOT NULL);''')
    def agregar_pelicula(self, titulo, genero, duracion, fecha_estreno, directores):
        sql = "INSERT INTO peliculas (titulo, genero, duracion, fecha_estreno, directores) VALUES (%s, %s, %s, %s, %s)"
        valores = (titulo, genero, duracion, fecha_estreno, directores)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.lastrowid
    def obtener_peliculas(self):
        self.cursor.execute("SELECT * FROM peliculas")
        for pelicula in self.cursor.fetchall():
            print(pelicula)
    def consultar_pelicula(self, codigo):
        # Consultamos una película a partir de su código
        self.cursor.execute(f"SELECT * FROM peliculas WHERE codigo = {codigo}")
        return self.cursor.fetchone()
    def modificar_pelicula(self, codigo, nuevo_titulo, nuevo_genero, nueva_duracion, nueva_fecha_estreno, nuevo_director):
        sql = "UPDATE peliculas SET titulo = %s, genero = %s, duracion = %s, fecha_estreno = %s, directores = %s WHERE codigo = %s"
        valores = (nuevo_titulo, nuevo_genero, nueva_duracion, nueva_fecha_estreno, nuevo_director, codigo)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0
    def mostrar_pelicula(self, codigo):
        # Mostramos los datos de una película a partir de su código
        pelicula = self.consultar_pelicula(codigo)
        if pelicula:
            print("-" * 40)
            print(f"Código........: {pelicula['codigo']}")
            print(f"Título........: {pelicula['titulo']}")
            print(f"Género........: {pelicula['genero']}")
            print(f"Duración......: {pelicula['duracion']}")
            print(f"Fecha Estreno.: {pelicula['fecha_estreno']}")
            print(f"Directores....: {pelicula['directores']}")
            print("-" * 40)
        else:
            print("Película no encontrada.")
    def listar_peliculas(self):
        self.cursor.execute("SELECT * FROM peliculas")
        peliculas = self.cursor.fetchall()
        return peliculas
    def eliminar_pelicula(self, codigo):
        # Eliminamos una película de la tabla a partir de su código
        self.cursor.execute("DELETE FROM peliculas WHERE codigo = %s", (codigo,))
        self.conn.commit()
        return self.cursor.rowcount > 0
    
#----------------------Código para testear------------------------------------
