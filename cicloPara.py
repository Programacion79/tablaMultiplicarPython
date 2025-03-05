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


# ========== Mostrar los numeros pares ==========#

def mostrarNumeroPares():
    for i in range(1, 21 ):
        if i % 2 == 0:
            print(i)


if __name__ == "__main__": 
    mostrarNumeroPares()   


# ========== verificar los números primos ==========#    
def vrifNumPrimos():
    Nro = int(input("Ingrese un número: "))

    es_primo = True
    for i in range(2, Nro):
        if Nro % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f'{Nro} es un numero primo')
    else:
        print(f'{Nro} no es número primo')            

if __name__ == "__main__":  
    vrifNumPrimos()  