

import sys

n1 = 0
n2 = 0

menu = """
1.- Sumar
2.- Restar
3.- Multiplicar
4.- Dividir
5.- Potencia
6.- Raiz
9.- Salir
"""

def Sumar():
    print("Ingresa el primer el primer numero para sumar: ")
    n1 = float(input())
    print("Ingresa el segundo numero para sumar: ")
    n2 = float(input())
    print("El resultado es: ", n1 + n2)

def Restar():
    print("Ingresa el numero para restar: ")
    n1 = float(input())
    print("Ingresa el numero para restar: ")
    n2 = float(input())
    print("El resultado es: ", n1 - n2)

def Multiplicar():
    print("Ingresa el primer numero para Multiplicar: ")
    n1 = float(input())
    print("Ingresa el segundo numero para Multiplicar: ")
    n2 = float(input())
    print("El resultado es: ", n1 * n2)

def Dividir():
    print("Ingresa el dividendo: ")
    n1 = float(input())
    print("Ingresa el divisor: ")
    n2 = float(input())
    print("El resultado es: ", n1 / n2)

def Potencia():
    print("Ingresa la base: ")
    n1 = float(input())
    print("Ingrese el exponente: ")
    n2 = float(input())
    print("El resultado es: ",n1 ** n2)

def Raiz():
    print("Ingresa el radicando: ")
    n1 = float(input())
    print("Ingresa el indice: ")
    n2 = float(input())
    print("El resultado es: ", n1 ** (1/n2) )

print("Bienvenido, Calculadora Basica...")
while True:
    print(menu)
    opc = int(input())
    if opc == 1:
        Sumar()
    elif opc == 2:
        Restar()
    elif opc == 3:
        Multiplicar()
    elif opc == 4:
        Dividir()
    elif opc == 5:
        Potencia()
    elif opc == 6:
        Raiz()
    elif opc == 9:
        sys.exit()
    