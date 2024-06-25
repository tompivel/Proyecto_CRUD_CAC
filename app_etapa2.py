class Catalogo:
    def __init__(self):
        self.películas = []

    def agregar_pelicula(self, codigo, titulo, genero, duracion, fecha_estreno, directores):
        if self.consultar_pelicula(codigo):
            return False
        
        nueva_pelicula = {
            'codigo': codigo,
            'titulo': titulo,
            'genero': genero,
            'duracion': duracion,
            'fecha_estreno': fecha_estreno,
            'directores': directores
        }
        
        self.películas.append(nueva_pelicula)
        return True

    def consultar_pelicula(self, codigo):
        for pelicula in self.películas:
            if pelicula['codigo'] == codigo:
                return pelicula
        return False

    def modificar_pelicula(self, codigo, nuevo_titulo, nuevo_genero, nueva_duracion, nueva_fecha_estreno, nuevos_directores):
        for pelicula in self.películas:
            if pelicula['codigo'] == codigo:
                pelicula['titulo'] = nuevo_titulo
                pelicula['genero'] = nuevo_genero
                pelicula['duracion'] = nueva_duracion
                pelicula['fecha_estreno'] = nueva_fecha_estreno
                pelicula['directores'] = nuevos_directores
                return True
        return False

    def listar_peliculas(self):
        print("-" * 50)
        for pelicula in self.películas:
            print(f"Código........: {pelicula['codigo']}")
            print(f"Título........: {pelicula['titulo']}")
            print(f"Género........: {pelicula['genero']}")
            print(f'Duración......: {pelicula["duracion"]}')
            print(f'Fecha Estreno.: {pelicula["fecha_estreno"]}')
            print(f'Directores....: {", ".join(pelicula["directores"])}')
            print("-" * 50)

    def eliminar_pelicula(self, codigo):
        for pelicula in self.películas:
            if pelicula['codigo'] == codigo:
                self.películas.remove(pelicula)
                return True
        return False

# Ejemplo de uso de la clase Catalogo

# Crear una instancia de Catalogo
catalogo_peliculas = Catalogo()

# Agregar películas al catálogo
catalogo_peliculas.agregar_pelicula(1, 'The Super Mario Bros Movie', 'Animation, Family, Adventure, Fantasy, Comedy', '1h 33m', '04/05/2023', ['Aaron Horvath', 'Michael Jelenic'])
catalogo_peliculas.agregar_pelicula(2, 'Aquaman and the Lost Kingdom', 'Action, Adventure, Fantasy', '2h 30m', '16/12/2022', ['James Wan'])
catalogo_peliculas.agregar_pelicula(3, 'Forrest Gump', 'Drama, Romance', '2h 22m', '06/07/1994', ['Robert Zemeckis'])
catalogo_peliculas.agregar_pelicula(4, 'The Godfather', 'Crime, Drama', '2h 55m', '24/03/1972', ['Francis Ford Coppola'])
catalogo_peliculas.agregar_pelicula(5, 'The Marvels', 'Action, Adventure, Sci-Fi', 'TBD', '17/02/2023', ['Nia DaCosta'])
catalogo_peliculas.agregar_pelicula(6, 'Wonka', 'Adventure, Comedy, Family', 'TBD', '17/03/2023', ['Paul King'])

# Listar películas en el catálogo
print("Listado de películas:")
catalogo_peliculas.listar_peliculas()

# Modificar una película en el catálogo (ejemplo modificando 'The Godfather')
print("\nModificando la película 'The Godfather'...")
catalogo_peliculas.modificar_pelicula(4, 'The Godfather (Modificado)', 'Crime, Drama', '2h 55m', '24/03/1972', ['Francis Ford Coppola'])

# Listar películas actualizadas
print("\nListado de películas actualizado:")
catalogo_peliculas.listar_peliculas()

# Eliminar una película del catálogo (ejemplo eliminando 'The Godfather')
print("\nEliminando la película 'The Godfather'...")
catalogo_peliculas.eliminar_pelicula(4)

# Listar películas después de eliminar
print("\nListado de películas después de eliminar:")
catalogo_peliculas.listar_peliculas()

'''Este código es una implementación de una clase llamada "Catalogo" en Python. Esta clase tiene métodos para agregar, consultar, modificar, listar y eliminar películas en un catálogo.

El método __init__ es el constructor de la clase y se encarga de inicializar la lista de películas.

El método agregar_pelicula recibe los datos de una película (código, título, género, duración, fecha de estreno y directores) y los agrega a la lista de películas, siempre y cuando no exista ya una película con el mismo código.

El método consultar_pelicula recibe un código de película y busca si existe una película con ese código en la lista. Si la encuentra, devuelve los datos de la película, de lo contrario devuelve False.

El método modificar_pelicula recibe un código de película y los nuevos datos para modificarlos en la lista, si encuentra la película con ese código la modifica y devuelve True, si no la encuentra devuelve False.

El método listar_peliculas imprime en pantalla los datos de todas las películas en la lista.

El método eliminar_pelicula recibe un código de película y busca si existe una película con ese código en la lista, si la encuentra la elimina de la lista y devuelve True.

Es importante notar que hay un error en el último método, donde se intenta retornar "Tr" en lugar de "True".'''
self.conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)