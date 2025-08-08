class Departamento:
    def __init__(self, id, nombre):
        """
        Inicializa una instancia de Departamento.

        Parámetros:
            id (int): Identificador numérico del departamento.
            nombre (str): Nombre del departamento.
        """
        self.id = id
        self.nombre = nombre

    def mostrar(self):
        """
        Devuelve una cadena con los datos del departamento.

        Returns:
            str: Cadena con los datos del departamento
        """
        return f"Departamento ID: {self.id} | Nombre: {self.nombre}"