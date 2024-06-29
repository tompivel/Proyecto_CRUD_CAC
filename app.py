from flask_cors import CORS
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import mysql.connector 
import os
import time
#--------------------------------------------------------------------
app = Flask(__name__)
CORS(app)
#------------------------------CLASS CATALOG--------------------------------------
class Catalog:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
        )
        self.cursor = self.conn.cursor()
        
        try:
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
            else:
                raise err
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS movies (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            genre VARCHAR(255) NOT NULL,
            duration VARCHAR(50) NOT NULL,
            release_year VARCHAR(50) NOT NULL,
            directors VARCHAR(255) NOT NULL,
            image_url VARCHAR(255))''')
            
        self.conn.commit()
        
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)


    def add_movie(self, title, genre, duration, release_year, directors, image):
        sql = "INSERT INTO movies (title, genre, duration, release_year, directors, image_url) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (title, genre, duration, release_year, directors, image)
        self.cursor.execute(sql, values)
        self.conn.commit()
        return self.cursor.lastrowid

    def get_movie(self, id):
        self.cursor.execute(f"SELECT * FROM movies WHERE id = {id}")
        return self.cursor.fetchone()

    def update_movie(self, id, new_title, new_genre, new_duration, new_release_year, new_directors, new_image):
        sql = "UPDATE movies SET title = %s, genre = %s, duration = %s, release_year = %s, directors = %s, image_url = %s WHERE id = %s"
        values = (new_title, new_genre, new_duration, new_release_year, new_directors, new_image, id)
        self.cursor.execute(sql, values)
        self.conn.commit()
        return self.cursor.rowcount > 0

    def list_movies(self):
        self.cursor.execute('SELECT * FROM movies')
        return self.cursor.fetchall()
    
    def display_movie(self, id):
        movie = self.get_movie(id)
        if movie:
            print("-" * 40)
            print(f"ID..............: {movie['id']}")
            print(f"Title...........: {movie['title']}")
            print(f"Genre...........: {movie['genre']}")
            print(f"Duration........: {movie['duration']}")
            print(f"Release Year....: {movie['release_year']}")
            print(f"Directors.......: {movie['directors']}")
            print(f"Image...........: {movie['image_url']}")
            print("-" * 40)
        else:
            print("Movie not found.")

    def delete_movie(self, id):
        self.cursor.execute(f"DELETE FROM movies WHERE id = {id}")
        self.conn.commit()
        return self.cursor.rowcount > 0

# Programa principal

catalog = Catalog(host='proyectocac24171.mysql.pythonanywhere-services.com',
user='proyectocac24171', password='mobivav741', database='proyectocac24171$miapp')
# host: Es el que nos proporcionó el sitio. Lo podemos ver en la pestaña "Databases"
# user: Es el usuario de la base de datos,
# password: Es el password que elegimos para la base de datos
# database: El nombre de la base de datos, generalmente tu_usuario$base_de_datos

'''
# Agregamos películas a la tabla
catalog.add_movie('The Super Mario Bros Movie', 'Animation, Family, Adventure, Fantasy, Comedy', '1h 33m', '2023', ['Aaron Horvath', 'Michael Jelenic'])
catalog.add_movie('Aquaman and the Lost Kingdom', 'Action, Adventure, Fantasy', '2h 30m', '2022', ['James Wan'])
catalog.add_movie('Forrest Gump', 'Drama, Romance', '2h 22m', '1994', ['Robert Zemeckis'])
catalog.add_movie('The Godfather', 'Crime, Drama', '2h 55m', '1972', ['Francis Ford Coppola'])
catalog.add_movie('The Marvels', 'Action, Adventure, Sci-Fi', 'TBD', '2023', ['Nia DaCosta'])
catalog.add_movie('Wonka', 'Adventure, Comedy, Family', 'TBD', '2023', ['Paul King'])

id_pelicula = int(input("Ingrese el código de la pelicula: "))
pelicula = catalog.get_movie(id_pelicula)
if pelicula:
    print(f"Pelicula encontrada: {pelicula['id']} - {pelicula['nombre']}")
else:
    print(f'Pelicula {id_pelicula} no encontrada.')


# Consultamos y mostramos una película
catalog.display_movie(1)
catalog.display_movie(2)
catalog.display_movie(3)
catalog.display_movie(4)
catalog.display_movie(5)
catalog.display_movie(6)

# Eliminamos un producto
catalog.delete_product(2)
productos = catalog.list_products()
for producto in productos:
    print(producto)

# Listamos todas las películas
peliculas = catalog.list_movies()
for pelicula in peliculas:
    print(pelicula)
'''
# Carpeta para guardar las imagenes
destination_path = '/home/proyectocac24171/mysite/static/images/'


""" @app.route('/')
def home():
    return render_template('template.html', title='Home Page',
    heading='Welcome!', items=['Item 1', 'Item 2', 'Item 3']) """

@app.route('/movies', methods=['GET'])
def list_movies():
    movies = catalog.list_movies()
    return jsonify(movies)

@app.route('/movies/<int:id>', methods=['GET'])
def get_movie(id):
    movie = catalog.get_movie(id)
    if movie:
        return jsonify(movie), 201
    else:
        return jsonify({'message': 'Movie not found'}), 404

@app.route('/movies', methods=['POST'])
def add_movie():
    title = request.form['title']
    genre = request.form['genre']
    duration = request.form['duration']
    release_year = request.form['release_year']
    directors = request.form['directors']
    image = request.files['image']
    image_name = ""
    
    image_name = secure_filename(image.filename)
    base_name, extension = os.path.splitext(image_name)
    image_name = f"{base_name}_{int(time.time())}{extension}"
    
    new_id = catalog.add_movie(title, genre, duration, release_year, directors, image_name)
    if new_id:
        image.save(os.path.join(destination_path, image_name))
        return jsonify({"message": "Movie added successfully.", "id": new_id, "image": image_name}), 201
    else:
        return jsonify({"message": "Error adding the movie."}), 500
    
    
@app.route('/movies/<int:id>', methods=['PUT'])
def update_movie(id):
    new_title = request.form.get('title')
    new_genre = request.form.get('genre')
    new_duration = request.form.get('duration')
    new_release_year = request.form.get('release_year')
    new_directors = request.form.get('directors')
    
    if 'image' in request.files:
        image = request.files['image']
        image_name = secure_filename(image.filename)
        base_name, extension = os.path.splitext(image_name)
        image_name = f"{base_name}_{int(time.time())}{extension}"
        image.save(os.path.join(destination_path, image_name))
        
        movie = catalog.get_movie(id)
        if movie:
            old_image = movie["image_url"]
            image_path = os.path.join(destination_path, old_image)
            if os.path.exists(image_path):
                os.remove(image_path)

    else:
        movie = catalog.get_movie(id)
        if movie:
            image_name = movie["image_url"]
    
    if catalog.update_movie(id, new_title, new_genre, new_duration, new_release_year, new_directors, image_name):
        return jsonify({"message": "Movie updated"}), 200
    else:
        return jsonify({"message": "Movie not found"}), 403    


@app.route('/movies/<int:id>', methods=['DELETE'])
def delete_movie(id):
    movie = catalog.get_movie(id)
    if movie:
        image_path = os.path.join(destination_path, movie["image_url"])
        if os.path.exists(image_path):
            os.remove(image_path)
        if catalog.delete_movie(id):
           return jsonify({"message": "Movie deleted"}), 200 
        else:
           return jsonify({"message": "Error deleting the movie"}), 500
    else:
        return jsonify({"message": "Movie not found"}), 404
            
if __name__ == '__main__':
    app.run(debug=True)
