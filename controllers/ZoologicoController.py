class ZoologicoController:

    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista


    def accion(self, opcion):

        if opcion == 1:
            while True:
                try:
                    id = int(input("ID del animal: "))
                    break  # Salir del bucle si el tipo de datos es correcto
                except ValueError:
                    print("El valor ingresado no es un número entero. Por favor intente nuevamente.")

            verificacion = self.modelo.verificar_animal(id)

            if verificacion == 0:
                animal = self.vista.menu_crearAnimal(id)
                self.modelo.ingresar_animal(animal.id,animal)
                self.modelo.ingresar_habitat(animal.habitat)
            else:
                print("Ya existe un animal ingresado con ese id\n")

        if opcion == 2:
            self.modelo.leer_animal()

        if opcion == 3:
            self.modelo.leer_habitat()
            tipo = input("Digite el habitat al que le quiere asignar las caractericas: ")
            verificacion = self.modelo.verificar(tipo)
            if verificacion == 1:
                habitat = self.vista.menu_habitat(tipo)
                self.modelo.caracteristicas_habitat(tipo, habitat)
            else:
                print("Ese habitat no existe dentro los habitats asignados de oringen de los animales actualmente agregados\n")

        if opcion == 4:

            print("Ingrese uno de las habitat que se ven en pantalla:\n")
            self.modelo.mostrar_habitat()
            print("")
            while True:
                try:
                    pTempA = int(input("Digite el id del animal que quiere ubicar en un habitat: "))
                    break  # Salir del bucle si el tipo de datos es correcto
                except ValueError:
                    print("El valor ingresado no es un número entero. Por favor intente nuevamente.")

            pTempH = input("Ingrese el habitat donde lo quiere ubicar: ")
            pClima = input("Ingrese el clima adecuado: ")
            self.modelo.animal_habitat(pTempA, pTempH, pClima)

        if opcion == 5:
            self.modelo.mostrar_asignados()

        if opcion == 6:
            print("[1] Carnivoro.\n[2] Herbivoro.\n[3] Omnivoro.")
            while True:
                dieta = input("Ingrese el tipo de dieta: ")
                if dieta.isdigit():
                    dieta = int(dieta)
                    if dieta < 0 or dieta > 3:
                        print("Entrada no valida")
                    else:
                        break
                else:
                    print("Digite un numero por favor")

            if dieta == 1:
                dietaSeleccionada = "carnivoro"
            elif dieta == 2:
                dietaSeleccionada = "herbivoro"
            elif dieta == 3:
                dietaSeleccionada = "omnivoro"

            while True:
                alimentos = input("Ingrese un alimento a agregar o escriba 'fin' para finalizar: ")
                if alimentos == 'fin':
                    break
                if alimentos.isdigit():
                    print("Por favor ingrese texto.")
                else:
                    self.modelo.agregar_alimentos(dietaSeleccionada, alimentos)

          #self.modelo.imprimirDiccionario()

        if opcion == 7:

            print("¿Que desea hacer con el animal?")
            print("[1]Jugar\n[2]Dormir\n[3]Comer\n")
            while True:
                accion = input("Ingrese la accion a realizar en palabras: ")
                if accion.isdigit():
                    print("Digite una cadena de texto por favor")
                else:
                    if (accion != "comer" and accion != "dormir" and accion != "jugar"):
                        print("Opcion no existente")
                    else:
                        break

            while True:
                idAnimal = input("Ingrese el id del animal: ")
                if idAnimal.isdigit():
                    idAnimal = int(idAnimal)
                    verificadorId=self.modelo.verificadorId(idAnimal)
                    if verificadorId == True:
                        break
                    else:
                        print("Id no encontrado")
                else:
                    print("Digite un numero por favor")

            if accion == "jugar":
                self.modelo.jugar(idAnimal)

            elif accion == "dormir":
                self.modelo.dormir(idAnimal)

            elif accion == "comer":
                print("Digite el tipo de dieta:\ncarnivoro\nherbivoro\nomnivoro")
                while True:
                    alimentacion = input()
                    if not alimentacion.isdigit():
                        if alimentacion == "carnivoro" or alimentacion == "herbivoro" or alimentacion == "omnivoro":
                            verificarDieta = self.modelo.verificarDieta(idAnimal, alimentacion)
                            if verificarDieta == True:
                                break
                            else:
                                print("La dieta no coincide con la del animal, vuelva a digitarla")
                        else:
                            print("Opcion invalida")
                    else:
                        print("Digite la opcion en texto.")

                self.modelo.comer(idAnimal, alimentacion)
