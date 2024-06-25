from etapa3 import Catalogo  # Assuming your class is named CatalogoPeliculas


catalogo = Catalogo('localhost', 'root', 'password', 'miapp')

nuevo_codigo = catalogo.agregar_pelicula('Inception', 'Sci-Fi', '2h 28m', '2010-07-16', 'Christopher Nolan')
print(f'Nuevo código de película agregada: {nuevo_codigo}')
catalogo.obtener_peliculas()

cod_pelicula = int(input("Ingrese el código de la película: "))
pelicula = catalogo.consultar_pelicula(cod_pelicula)
if pelicula:
    print(f"Película encontrada: {pelicula['codigo']} - {pelicula['titulo']}")
else:
    print(f'Película {cod_pelicula} no encontrada.')
    
# Modificamos una película y la mostramos
catalogo.mostrar_pelicula(1)
catalogo.modificar_pelicula(1, 'Interstellar', 'Sci-Fi', '2h 49m', '2014-11-07', 'Christopher Nolan')
catalogo.mostrar_pelicula(1)

# Eliminamos una película
catalogo.eliminar_pelicula(2)
peliculas = catalogo.listar_peliculas()
for pelicula in peliculas:
    print(pelicula)
