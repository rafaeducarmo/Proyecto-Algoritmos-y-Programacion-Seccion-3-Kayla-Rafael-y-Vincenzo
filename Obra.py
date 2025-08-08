import Utils as u

class Obra:
    def __init__(self, id, titulo, tipo, anio_creacion, imagen_url, artista, departamento):
        """
        Inicializa una instancia de Obra.

        Parámetros:
            id (int): Identificador único de la obra.
            titulo (str): Título de la obra.
            tipo (str): Tipo o categoría de la obra (ej. pintura, escultura).
            anio_creacion (str o int): Año en que fue creada la obra.
            imagen_url (str): URL de una imagen representativa de la obra.
            artista (Artista): Objeto Artista asociado a la obra.
            departamento (str): nombre del departamento al que pertenece la obra.
        """
        self.id = id
        self.titulo = titulo
        self.tipo = tipo
        self.anio_creacion = anio_creacion
        self.imagen_url = imagen_url
        self.artista = artista
        self.departamento = departamento

    def mostrar(self):
        """
        Devuelve un resumen de la obra con ID, título y nombre del artista.
        Returns:
            str: Cadena con los datos principales de la obra.
        """
        return f"ID: {self.id} | Título: {self.titulo} | Artista: {self.artista.nombre}"

    def mostrar_detalles(self):
        """
        Devuelve todos los datos de la obra, excepto el departamento.
        Incluye ID, título, tipo, año de creación, URL de imagen y datos completos del artista.

        Returns:
            str: Cadena con los datos detallados de la obra.
        """
        detalles_artista = self.artista.mostrar()
        return f'''
ID: {self.id}
Título: {self.titulo}
Tipo: {self.tipo}
Año de creación: {self.anio_creacion}
Artista: {detalles_artista}
'''
            
    
    def mostrar_imagen(self):
        if self.imagen_url:
            u.mostrar_imagen(self.imagen_url)
        else:
            print('No contiene imágenes para mostrar')