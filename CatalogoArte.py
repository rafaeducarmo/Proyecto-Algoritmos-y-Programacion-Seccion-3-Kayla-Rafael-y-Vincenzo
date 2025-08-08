from Obra import Obra
from Artista import Artista
from Departamento import Departamento

import requests


class CatalogoArte:
    def __init__(self):
        self.departamentos = []
        self.obras = []

    def cargar_datos(self):
        """
        Carga la lista de departamentos desde la API del Met Museum.

        Solicita la URL de departamentos, extrae los datos mínimos y devuelve
        una lista de objetos Departamento.
        """
        url = 'https://collectionapi.metmuseum.org/public/collection/v1/departments'
        respuesta = requests.get(url)
        data = respuesta.json()['departments']
        for d in data:
            dept = Departamento(d['departmentId'], d['displayName'])
            self.departamentos.append(dept)



    def buscar_obra(self, id):
        """
        Obtiene los datos de una obra por su ID desde la API del Met Museum.

        Parámetros:
            id (int): Identificador de la obra a buscar.

        Returns:
            Obra: Una instancia de la clase Obra con los datos recuperados.
            None: Si ocurre un error durante la petición o si no se obtiene un resultado válido.
        """

        api = f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{id}'
        try:
            obra = requests.get(api).json()
        except Exception as e:
            print('Ocurrió un error')
            return None
        
        obra_id = obra['objectID']
        titulo = obra['title']
        anio_creacion = obra['objectDate']
        tipo = obra['classification']
        departamento = obra['department']
        imagen_url = obra['primaryImage']

        artista_nombre = "-" if obra['artistDisplayName'] == "" else obra['artistDisplayName']
        artista_nacionalidad= "-" if obra['artistNationality'] == "" else obra['artistNationality']
        artista_nacimiento = "-" if obra['artistBeginDate'] == "" else obra['artistBeginDate']
        artista_muerte = "-" if obra['artistEndDate'] == "" else obra['artistEndDate']

        artista = Artista(artista_nombre,artista_nacionalidad,artista_nacimiento,artista_muerte)

        obra = Obra(obra_id,titulo,tipo,anio_creacion,imagen_url,artista,departamento)

        return obra

    def buscar_por_departamento(self):
        """
        Permite al usuario seleccionar un departamento y traer obras de ese departamento.
        Muestra las obras encontradas.
        """
        print("\nLista de Departamentos:")
        for dep in self.departamentos:
            print(dep.mostrar())

        opcion = input("Ingrese el ID del departamento: ")

        while not opcion.isnumeric():
            opcion = input("Ingrese un ID válido del departamento: ")

        encontrado = None
        for dep in self.departamentos:
            if dep.id == int(opcion):
                encontrado = dep
                break

        if encontrado:
            print(f"Seleccionó: {encontrado.nombre}")

            respuesta = requests.get(f'https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds={encontrado.id}').json()
            print(f'Hay {respuesta['total']} obras en el departamento: {encontrado.nombre}')

            indice = 0
            obras_encontradas = []
            while True:
                cantidad = input('Cuántas obras quiere traer (máximo 15): ')
                while not cantidad.isnumeric() or (int(cantidad) not in range(1,16)):
                    print('Ingrese un número válido entre el 1 y 15')
                    cantidad = input('Cuántas obras quiere traer (máximo 15): ')

                cantidad = int(cantidad)

                while cantidad > 0 or indice >= len(respuesta['objectIDs']):
                    obra_encontrada = self.buscar_obra(respuesta['objectIDs'][indice])

                    if obra_encontrada:
                        print('La obra fue encontrada.')
                        obras_encontradas.append(obra_encontrada)
                        cantidad -=1
                    
                    indice +=1
                
                if indice >= len(respuesta['objectIDs']):
                    break

                opcion = input(f'\nSe guardaron {len(obras_encontradas)} obras.\nSi desea añadir más obras, ingrese 1: ')
                if opcion != '1':
                    break
            
            print('Obras encontradas:')
            if len(obras_encontradas) == 0:
                print('Lo lamentamos, no hay obras que cumplan con su coincidencia.')
                return
            for obra in obras_encontradas:
                print(obra.mostrar())


        else:
            print("Departamento no encontrado")

    def buscar_por_nacionalidad(self):
        pass

    def buscar_por_artista(self):
        pass


    def inicio(self):
        """
        Funcion de inicio del programa que contiene el menú principal
        """
        self.cargar_datos()

        while True:
            print("\n--- Menú Principal ---")
            print("1. Búsqueda de obras por departamentos")
            print("2. Búsqueda de obras por nacionalidad del artista")
            print("3. Búsqueda de obras por nombre del artista")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.buscar_por_departamento()
            elif opcion =='2':
                self.buscar_por_nacionalidad()
            elif opcion == '3':
                self.buscar_por_artista()
            elif opcion == '4':
                print('Adios')
                break