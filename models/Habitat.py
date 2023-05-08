
class Habitat:
    def __init__(self, tipo, humedad, clima, temperatura):
        self.tipo = tipo
        self.humedad = humedad
        self.clima = clima
        self.temperatura = temperatura

    def mostrarHabitat(self):
        print("habitats: \n", self.tipo, self.humedad, self.clima, self.temperatura)