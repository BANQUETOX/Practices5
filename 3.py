# Haga un programa que dado el número de capítulos de un libro leídos por día, imprima el
# total de capítulos leídos y el número de días en que terminó el libro. El programa debe leer
# el número de capítulos leídos por día hasta que el usuario termine el libro. Ejemplo: si los
# datos dados por el usuario son los siguientes, el programa se comporta de esta manera:

# ¿Cuántos capítulos leyó hoy? 2
# ¿Terminó el libro? N
# ¿Cuántos capítulos leyó hoy? 4
# ¿Terminó el libro? N
# ¿Cuántos capítulos leyó hoy? 6
# ¿Terminó el libro? S
# Felicidades, usted leyó un libro de 12 capítulos en 3 días
finish = ""
chapters = 0
days = 1
while finish != "S":
    chapters = int(input("¿Cuántos capítulos leyó hoy? "))
    finish = input("¿Terminó el libro?(S/N) ").upper()
    if finish == "S":
        print(f"Felicidades, usted leyó un libro de {chapters} capítulos en {days} días")
    else:
        days += 1

