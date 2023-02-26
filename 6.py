# (**) En una fábrica de camisas se tienen N máquinas. En un día de trabajo se producen X
# camisas. Se desea calificar la productividad semanal (en semanas de cinco días laborales)
# de cada máquina de acuerdo con un índice de productividad (IP) dado por el usuario,
# basándose en las siguientes reglas:
# a) Producción semanal > IP, productividad es excelente.
# b) Producción semanal = IP, productividad es buena.
# c) Producción semanal < IP, productividad es mala.
# El programa debe imprimir la productividad de cada máquina al final de la semana,
# además, cuántas máquinas tuvieron productividad excelente en la semana y la producción
# semanal de camisas de toda la fábrica.
# (**) Ejercicio de nivel avanzado.

amount_machines = int(input("Cuantas maquinas hay en la fabrica? "))
ip = int(input("Cual es su porcentaje de indice de productividad? "))
total_shirts = 0
excelent_machines = 0
for machine in range(1, amount_machines + 1):
    shirts_made = int((input(f"Cuantas camisas fabrico la maquina #{machine} ")))
    total_shirts += shirts_made
    machine_productivity = (shirts_made / 5) * 100
    if machine_productivity > ip:
        excelent_machines += 1
        print(f"La maquina #{machine} tuvo una exelente productividad")
    elif machine_productivity == ip:
        print(f"La maquina #{machine} tuvo una productividad media")
    else:
        print(f"La maquina #{machine} tuvo una mala productividad")
print(f"Durante la semana se produjeron {total_shirts} camisas \
    \n y {excelent_machines} maquinas tuvieron una exelente productividad")

        


    
