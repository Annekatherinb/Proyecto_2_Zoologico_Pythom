import models.Animal as animalModel

class Datos:
    def __init__(self):
        self.animales = {}
        self.habitats = []
        self.habitat_fijo = {}
        self.asignacion = {}
        self.alimentacion = {}

    def ingresar_animal(self, id, animal):
        self.animales[id] = animal

    def verificar_animal(self, id):
        if self.animales.get(id) is not None:
            return 1
        else:
            return 0

    def leer_animal(self):
        print("Animales ingresados al zoologico:\n")
        for key in self.animales:
            animal = self.animales[key]
            animal.mostrarAnimal()

    def ingresar_habitat(self, habitat):
        if habitat in self.habitats:
            print("Ya se encuentra agregado ese Habitat al zoologico\n")
        else:
            self.habitats.append(habitat)

    def leer_habitat(self):
        print("Los habitats ingresados hasta el momento son: ")
        for i in range(len(self.habitats)):
            print(self.habitats[i])

    def caracteristicas_habitat(self, habitat, ob_habitat):
        self.habitat_fijo[habitat] = ob_habitat
        print("El habitat fue creado existosamente, dentro del zoologico\n")


    def verificar(self, tipo):
        for i in range(len(self.habitats)):
            if tipo in self.habitats:
                return 1
            else:
                return 0

    def animal_habitat(self, id, habitat):
        if id in self.animales:
            animal = self.animales[id]
            if habitat in self.habitat_fijo:
                habitat = self.habitat_fijo[habitat]
                if animal.habitat == habitat.tipo:
                    if habitat in self.asignacion:
                        self.asignacion[habitat].append(animal)
                    else:
                        self.asignacion[habitat] = [animal]
                else:
                    print("Ese no es el habitat de origen del animal, podria ser pejudicial para su salud")
            else:
                print("Ese Habitat no existe\n")
        else:
            print("Ese animal no se encuentra registrado en el Zoologico\n")

    def mostrar_asignados(self):
        for habitat, animales in self.asignacion.items():
            print( f"Habitat: {habitat.tipo} de Clima:{habitat.clima} y Temperatura de: {habitat.temperatura} con una Humedad: {habitat.humedad}")
            print("Animales agregados: ")
            for animal in animales:
                print(animal.nombre, end=", ")
        print("\n")