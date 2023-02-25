# Haga un programa que lea uno o varios números enteros, mientras el número dado por el
# usuario sea un número par. Ejemplos: si los números dados por el usuario son los
# siguientes, el programa se comporta de esta manera:

# Ejemplo 1:
# Por favor escriba un número entero: 2
# Por favor escriba un número entero: 4
# Por favor escriba un número entero: 8
# Por favor escriba un número entero: 7
# Muchas gracias.
# Ejemplo 2:

# Por favor escriba un número entero: 5
# Muchas gracias
number = int(input("Por favor escriba un numero entero: "))
while number % 2 == 0:
    number = int(input("Por favor escriba un numero entero: "))
print("Muchas gracias.")
    