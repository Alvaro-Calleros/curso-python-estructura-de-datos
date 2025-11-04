class Perro_alvaro:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau Guau!")

    def sentarse(self):
        print(f"{self.nombre} está sentado.")


    def caminar(self):
        print(f"{self.nombre} está caminando.")



firulais = Perro_alvaro("Firulais", 3, "Labrador")