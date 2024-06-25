# Definimos una lista de diccionarios para almacenar las películas
peliculas = []

# Función para agregar una película
def agregar_pelicula(codigo, titulo, genero, duracion, fecha_estreno, directores):
    if consultar_pelicula(codigo):
        return False
    
    nueva_pelicula = {
        'codigo': codigo,
        'titulo': titulo,
        'genero': genero,
        'duracion': duracion,
        'fecha_estreno': fecha_estreno,
        'directores': directores
    }
    
    peliculas.append(nueva_pelicula)
    return True

# Función para consultar una película por su código
def consultar_pelicula(codigo):
    for pelicula in peliculas:
        if pelicula['codigo'] == codigo:
            return pelicula
    return False

# Función para modificar una película
def modificar_pelicula(codigo, nuevo_titulo, nuevo_genero, nueva_duracion, nueva_fecha_estreno, nuevos_directores):
    for pelicula in peliculas:
        if pelicula['codigo'] == codigo:
            pelicula['titulo'] = nuevo_titulo
            pelicula['genero'] = nuevo_genero
            pelicula['duracion'] = nueva_duracion
            pelicula['fecha_estreno'] = nueva_fecha_estreno
            pelicula['directores'] = nuevos_directores
            return True
    return False

# Función para listar todas las películas
def listar_peliculas():
    print("-"*50)
    for pelicula in peliculas:
        print(f'Código........: {pelicula["codigo"]}')
        print(f'Título........: {pelicula["titulo"]}')
        print(f'Género........: {pelicula["genero"]}')
        print(f'Duración......: {pelicula["duracion"]}')
        print(f'Fecha Estreno.: {pelicula["fecha_estreno"]}')
        print(f'Directores....: {", ".join(pelicula["directores"])}')
        print("-"*50)

# Función para eliminar una película
def eliminar_pelicula(codigo):
    for pelicula in peliculas:
        if pelicula['codigo'] == codigo:
            peliculas.remove(pelicula)
            return True
    return False


# Programa principal

# AGREGAR PELÍCULAS (adaptado desde las películas proporcionadas)
agregar_pelicula(1, 'The Super Mario Bros Movie', 'Animation, Family, Adventure, Fantasy, Comedy', '1h 33m', '04/05/2023', ['Aaron Horvath', 'Michael Jelenic'])
agregar_pelicula(2, 'Aquaman and the Lost Kingdom', 'Action, Adventure, Fantasy', '2h 30m', '16/12/2022', ['James Wan'])
agregar_pelicula(3, 'Forrest Gump', 'Drama, Romance', '2h 22m', '06/07/1994', ['Robert Zemeckis'])
agregar_pelicula(4, 'The Godfather', 'Crime, Drama', '2h 55m', '24/03/1972', ['Francis Ford Coppola'])
agregar_pelicula(5, 'The Marvels', 'Action, Adventure, Sci-Fi', 'TBD', '17/02/2023', ['Nia DaCosta'])
agregar_pelicula(6, 'Wonka', 'Adventure, Comedy, Family', 'TBD', '17/03/2023', ['Paul King'])

# Listar las películas
listar_peliculas()

# Eliminar una película (ejemplo eliminando "The Godfather")
print("Eliminando la película 'The Godfather'....")
eliminar_pelicula(4)

listar_peliculas()


'''Este código en Python define una serie de funciones para manejar una lista de películas almacenadas en forma de diccionarios. Las funciones incluyen:

- agregar_pelicula: Agrega una nueva película a la lista, verificando que no exista previamente.
- consultar_pelicula: Consulta una película por su código y devuelve la información si existe, de lo contrario devuelve False.
- modificar_pelicula: Modifica la información de una película existente, identificada por su código.
- listar_peliculas: Muestra en pantalla la información de todas las películas almacenadas en la lista.
- eliminar_pelicula: Elimina una película de la lista, identificada por su código.

Además, el código define una lista vacía llamada "peliculas" que se utiliza para almacenar los diccionarios que representan las películas. Cada diccionario contiene información como el código, título, género, duración, fecha de estreno y directores de la película.

El código también incluye un comentario "# Prog" al final, que parece ser un indicador para continuar con el desarrollo del programa.'''