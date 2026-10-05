# Practica 3
""""
Calcular el mayor de dos numeros ingresados por teclado usando un operador
ternario
"""

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

mayor = num1 if num1 > num2 else num2

print(f"El mayor de {num1} y {num2} es {mayor}")

""""
Buscar una palabra en una lista ingresada por teclado usando args y un operador
ternario
"""

lista_palabras = []

def crear_lista_palabras(*palabras):
    for p in palabras:
        lista_palabras.append(p)

def buscar_palabra_en_lista(palabra):
    return palabra in lista_palabras

crear_lista_palabras("manzana", "banana", "naranja", "pera", "uva")

palabra_a_buscar = input("Ingrese una palabra para buscar en la lista: ")

encontrar = buscar_palabra_en_lista(palabra_a_buscar)

print(f"La palabra '{palabra_a_buscar}' {'esta' if encontrar else 'no esta'} en la lista.") 

"""
Determinar si un numero es par o impar usando un operador ternario
"""

numero = int(input("Ingrese un numero: "))

es_par = "es par" if numero % 2 == 0 else "es impar"

print(f"El numero {numero} {es_par}.")  

"""
Calcular el promedio de una lista de numeros usando args y un operador ternario
"""

def calcular_promedio(*numeros):
    total = sum(numeros)
    cantidad = len(numeros)
    return total / cantidad if cantidad > 0 else 0

promedio = calcular_promedio(10, 20, 30, 40, 50)
print(f"El promedio es: {promedio}")

"""
Imprimir un mensaje de error si no se pasan suficientes argumentos
"""
def funcion_con_args(*args):
    if len(args) < 2:
        print("Error: Se requieren al menos dos argumentos.")
    else:
        print(f"Se recibieron {len(args)} argumentos.")

funcion_con_args(1)
