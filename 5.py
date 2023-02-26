# Haga un programa que lea uno o más años y determine, hasta que el usuario decida que
# no desea continuar, si cada año dado es bisiesto o no. Un año es bisiesto si el múltiplo de
# 4, excepto aquellos años que son múltiplos de 100. En estos casos el calendario
# gregoriano establece que un año que es múltiplo de cien es bisiesto solo si es divisible por
# 100 Y por 400. (Ejemplo, 1988, 1992 y 1996 son bisiestos porque son divisibles entre 4.
# 1600, 2000 y 2400 son bisiestos porque son divisibles por 100 y por 400; 1700, 1800, 1900
# y 2100 no son bisiestos porque son divisibles por 100 pero no por 400).

wants_to_continue = "s"
while wants_to_continue == "s":
    year = int(input("Escriba un año "))
    leap_year = False
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        leap_year = True
    else:
        leap_year = False
    if leap_year:
        print(f"El año {year} es bisiesto ")
    else:
        print(f"El año {year} no es bisiesto ")
    wants_to_continue = input("Desea continuar? (s/n) ").lower()
    
