def tablaMultiplicar():
    nro = int(input('Nro a Multiplicar: '))
    for i in range(11):
        print(f'{i} * {nro} = {i * nro}')

if __name__ == "__main__":
    tablaMultiplicar()


# Ejercicio de una piramide con *

def piramideAsteriscos():
    filas = int(input("¿Cúantas filas?"))
    for i in range(1, filas + 1):
        print(" * " * i)


if __name__ == "__main__":
    piramideAsteriscos()