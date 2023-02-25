# Haga un programa que lea todos los retiros que un usuario quiere hacer de su cuenta
# bancaria, hasta que la cuenta llegue a cero o se quiera hacer un retiro mayor al saldo de la
# cuenta. Para esto usted debe leer del usuario el saldo inicial de la cuenta y cada uno de los
# retiros que el usuario quiera hacer, hasta que se cumpla la condición mencionada. Ejemplo:
# si el saldo inicial y los retiros del usuario son los siguientes, el programa se comporta de
# esta manera:

# Por favor escriba el saldo inicial: 55600
# Por favor escriba su retiro: 5600
# Por favor escriba su retiro: 21000
# Por favor escriba su retiro: 12000
# Por favor escriba su retiro: 2500
# Por favor escriba su retiro: 4500
# Por favor escriba su retiro: 10000
# Se terminaron sus fondos.

funds = int(input("Por favor escriba el saldo inicial: "))

while funds > 0:
    withdraw = int(input("Por favor escriba su retiro: "))
    if withdraw > funds:
        print("Se terminaron sus fondos")
    else:
        funds -= withdraw
        if withdraw > funds:
            print("Se terminaron sus fondos")