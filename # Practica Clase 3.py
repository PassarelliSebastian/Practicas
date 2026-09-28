# Practica Clase 3

"""
Escribe un programa que intente dividir dos números. Si el segundo número es cero,
captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.
"""

def dividir_numeros(numerador, denominador):
    try:
        resultado = numerador / denominador
        print(f"El resultado de la división es: {resultado}")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")

print("Programa de división de números")
dividir_numeros(10, 0) # Esto generará una excepción ZeroDivisionError


"""
Escribe un programa que intente sumar un número y una cadena. Si se produce un error
de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.
"""

def sumar_numero_cadena(numero, cadena):
    try:
        resultado = numero + cadena
        print(f"El resultado de la suma es: {resultado}")
    except TypeError:
        print("Error: No se puede sumar un número y una cadena.")

print("Programa de suma de número y cadena")
sumar_numero_cadena(5, "hola")  # Esto generará una excepción TypeError

"""
Escribe un programa que intente acceder a una clave que no existe en un
diccionario. Si se produce una excepción KeyError, captura la excepción y la muestra
"""

def acceder_clave_diccionario(diccionario, clave):
    try:
        valor = diccionario[clave]
        print(f"El valor de la clave '{clave}' es: {valor}")
    except KeyError as e:
        print(f"Error: La clave {e} no existe en el diccionario.")

print("Programa de acceso a clave en diccionario")
acceder_clave_diccionario({"a": 1, "b": 2}, "c")  # Esto generará una excepción KeyError

"""
Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción
FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin
embargo, también intenta crear el archivo si no existe
"""

def abrir_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe. Creando el archivo...")
        with open(nombre_archivo, 'w') as archivo:
            archivo.write("Este es un nuevo archivo.")
        print(f"Archivo '{nombre_archivo}' creado exitosamente.")

abrir_archivo("archivo.txt")  # Esto generará una excepción FileNotFoundError y luego creará el archivo

"""
Escribe un programa que intente dividir dos números. Si el segundo número es cero,
captura la excepción ZeroDivisionError. Si el primer número es un número no válido,
captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario.
"""

def dividir_numeros (numerador, denominador):
    try:
        resultado = float(numerador) / float(denominador)
        print(f"El resultado de la división es: {resultado}")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except ValueError:
        print("Error: El valor proporcionado no es un número válido.")

print("Programa de división de números")
dividir_numeros(10, 0)  # Esto generará una excepción ZeroDivisionError
dividir_numeros("cinco", 2) # Esto generará una excepción ValueError


