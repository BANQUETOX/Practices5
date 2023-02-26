# (**) Se desea reunir los datos relacionados con la producción de una cantidad N de fábricas
# en cada uno de los meses del año anterior. Para cada fábrica, se sabe el nombre de la
# fábrica y la producción en unidades. Se le solicita, para cada una, los totales anuales de
# producción de cada fábrica, el nombre de la fábrica que más produjo en el año, y la
# cantidad de fábricas que, en el mes de julio, superaron las 3 000 000 de unidades.
# (**) Ejercicio de nivel avanzado.

factories = int(input("Cuantas fabricas se van a analizar? "))
three_million_factories = []

for factory in range(1, factories + 1):
    factory_name = input(f"Cual es el nombre de la fabrica #{factory}? ")
    factory_monthly_production = int(input(f"Cual fue la produccion mensual de la fabrica #{factory}? "))
    factory_total_production = factory_monthly_production * 12
    if factory_monthly_production * 7 > 3000000:
        three_million_factories.append(factory_name)
    print(f"{factory_name} creo {factory_total_production} durante todo el a;o")

print("Las fabricas que llegaron a mas de 3 millones de unidades en julio fueron ")
for factory in three_million_factories:
    print(factory)
