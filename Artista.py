class Artista:
    def __init__(self, nombre, nacionalidad, nacimiento, muerte):
        """Inicializa una instancia de Artista.

        Parámetros:
            nombre (str): Nombre completo del artista.
            nacionalidad (str): Nacionalidad del artista.
            nacimiento (str): Año de nacimiento del artista.
            muerte (str): Año de fallecimiento del artista.
        """
        
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.nacimiento = nacimiento
        self.muerte = muerte

    def mostrar(self):
        """
        Incluye nombre, nacionalidad, año de nacimiento y año de fallecimiento (si aplica).
        Returns:
            str: Cadena con los datos principales del artista.
        """
        
        
        return f'''Nombre: {self.nombre} | Nacionalidad: {self.nacionalidad} | 
                fNacimiento: {self.nacimiento} | Fallecimiento: {self.muerte}'''