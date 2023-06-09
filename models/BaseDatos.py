import models.Animal as animalModel

class Datos:
    def __init__(self):
        self.animales = {}
        self.habitats = []
        self.habitat_fijo = {}
        self.asignacion = {}
        self.alimentacion = {}

    def ingresar_animal(self,id, animal):
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

    def caracteristicas_habitat(self, habitat, ob_Habi):
        if habitat not in self.habitat_fijo:
            self.habitat_fijo[habitat] = []

        self.habitat_fijo[habitat].append(ob_Habi)
        print("El habitat fue creado existosamente, dentro del zoologico\n")

    def mostrar_habitat(self):
        for tipo, habitats in self.habitat_fijo.items():
            print(f"Hábitats de tipo {tipo}:")
            for habitat in habitats:
                print(f"Clima:{habitat.clima} y Temperatura de: {habitat.temperatura} con una Humedad: {habitat.humedad} de capacidad: {habitat.capacidad} y solo permite animales de alimentacion: {habitat.alimentacion}")


    def verificar(self, tipo):
        for i in range(len(self.habitats)):
            if tipo in self.habitats:
                return 1
            else:
                return 0

    def animal_habitat(self, id, habitat,clima):
        if id in self.animales:
            animal = self.animales[id]
            if habitat in self.habitat_fijo:
                lista = self.habitat_fijo[habitat]
                if any(h.tipo == habitat for h in lista):
                    if any(h.clima == clima for h in lista):
                        if animal.habitat == habitat:
                            if any(alimento in animal.alimentacion for h in lista if
                                   h.tipo == habitat and h.clima == clima for alimento in h.alimentacion):
                                if any(h.capacidad != 0 for h in lista if h.tipo == habitat and h.clima == clima):
                                    for h in lista:
                                        if h.tipo == habitat and h.clima == clima and h.capacidad != 0:
                                            h.capacidad -= 1
                                            if h in self.asignacion:
                                                self.asignacion[h].append(animal)
                                            else:
                                                self.asignacion[h] = [animal]
                                            print("El animal fue asignado exitosamente al habitat\n")
                                            break
                                else:
                                    print("No hay capacidad para ingresar este animal\n")
                            else:
                                print("La dieta de este animal no es optima para este habitat\n")
                        else:
                            print("Ese no es el habitat de origen del animal, podria ser perjudicial para su salud\n")
                    else:
                        print("No coincide el clima con los tipos que hay\n")
                else:
                    print("Ese habitat no esta en lista del mismo tipo\n")
            else:
                print("Ese Habitat no existe\n")
        else:
            print("Ese animal no se encuentra registrado en el Zoologico\n")

    def agregar_alimentos(self, dieta, alimentos):
        if dieta not in self.alimentacion:
            self.alimentacion[dieta] = []

        self.alimentacion[dieta].append(alimentos)

    def mostrar_asignados(self):
        for habitat, animales in self.asignacion.items():
            print( f"Habitat: {habitat.tipo} de Clima:{habitat.clima} y Temperatura de: {habitat.temperatura} con una Humedad: {habitat.humedad}")
            print("Animales agregados: ")
            for animal in animales:
                print(animal.nombre, end=", ")
        print("\n")

    def imprimirDiccionario(self):
        for key in self.alimentacion:
            print(key)
            for i in self.alimentacion[key]:
                print("alimentos:",i)

    def verificadorId(self, animal):
        if animal in self.animales:
            return True
        else:
            return False

    def verificarDieta(self, id, dieta):
        animal = self.animales[id]
        print("La dieta es:",animal.alimentacion)
        if animal.alimentacion == dieta:
            return True
        else:
            return False

    def jugar(self, id):
        animal = self.animales[id]
        if animal.juego == 0:
            print("El animal esta jugando")
            animal.juego = 1
        else:
            print("El animal ya jugo")

    def dormir(self, id):

        animal = self.animales[id]
        while True:
            horasDormir = input("Ingrese la cantidad de horas a dormir: ")
            if horasDormir.isdigit():
                horasDormir = int(horasDormir)
                if animal.horasSueno < horasDormir:
                    print("La cantidad ingresada supera el limite permitido para este animal")
                else:
                    break
            else:
                print("Digite un numero")


        animal.horasSueno -= horasDormir
        print("El animal esta durmiendo, le quedan", animal.horasSueno, "para dormir en otro momento")

    def comer(self, id, dieta):
        alimentos = self.alimentacion.get(dieta, [])
        if not alimentos:
            print("No se encontraron alimentos para la dieta", dieta)
            return

        print("Seleccione uno de los alimentos para el animal:")
        for i, comida in enumerate(alimentos, 1):
            print(i, comida)

        while True:
            comidaSeleccionada = input("Ingrese el número de la comida a seleccionar: ")
            if comidaSeleccionada.isdigit():
                comidaSeleccionada = int(comidaSeleccionada)
                if 1 <= comidaSeleccionada <= len(alimentos):
                    print("El animal está comiendo", alimentos[comidaSeleccionada - 1])
                    break
                else:
                    print("Opción inválida")
            else:
                print("Digite un número válido")











