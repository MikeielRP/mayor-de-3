class OrdenarTresNumeros:
    def __init__(self, numero1=None, numero2=None, numero3=None):  # Corrección del constructor
        self.numero1 = numero1
        self.numero2 = numero2
        self.numero3 = numero3

    def intercambiar_valores(self, numero1, numero2):
        temporal = numero1
        numero1 = numero2
        numero2 = temporal
        return numero1, numero2

    def ingresar_numeros(self):
        self.numero1 = int(input("Ingresa el primer número: "))
        self.numero2 = int(input("Ingresa el segundo número: "))
        self.numero3 = int(input("Ingresa el tercer número: "))

    def ordenar_numeros(self):
        if self.numero1 > self.numero2:
            self.numero1, self.numero2 = self.intercambiar_valores(self.numero1, self.numero2)

        if self.numero2 > self.numero3:
            self.numero2, self.numero3 = self.intercambiar_valores(self.numero2, self.numero3)

        if self.numero1 > self.numero2:
            self.numero1, self.numero2 = self.intercambiar_valores(self.numero1, self.numero2)

    def imprimir_numeros(self):
        print(f"{self.numero1}, {self.numero2}, {self.numero3}")


if __name__ == "__main__":
    numeros = OrdenarTresNumeros()
    numeros.ingresar_numeros()
    print("\nNúmeros desordenados:")
    numeros.imprimir_numeros()

    print("\nNúmeros ordenados:")
    numeros.ordenar_numeros()
    numeros.imprimir_numeros()

    print("\nEl mayor es:", numeros.numero3)