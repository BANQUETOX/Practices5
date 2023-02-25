# Haga un programa que determine si un número dado por el usuario es primo o no. Un
# número es primo si es divisible entre sí mismo y la unidad.

number = int(input("Escriba su numero: "))
cube_root = number**(1/3)
odd_list = [2]

if number <= 1:
    print("Solo se aceptan numeros mayores a 1")
else:
    counter = 0
    while counter <= cube_root.__round__():
        if  counter % 2 != 0:
            odd_list.append(counter)
        counter += 1
    odd_list.remove(1)
    for i in odd_list:
        if number % i == 0:
            is_prime = False
            break
        else:
            is_prime = True
    
    if number in odd_list:
        is_prime = True

    if is_prime:
        print("Es primo")
    else:
        print("No es primo")

