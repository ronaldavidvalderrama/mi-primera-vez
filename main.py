# Función para calcular la nota que necesita el alumno en el tercer certamen
def calcular_nota_necesaria():
    # Pedimos al usuario las notas de los dos primeros certámenes y la nota de laboratorio
    C1 = float(input("Ingrese la nota del primer certamen (C1): "))
    C2 = float(input("Ingrese la nota del segundo certamen (C2): "))
    NL = float(input("Ingrese la nota de laboratorio (NL): "))

    # Establecemos la nota final mínima para aprobar
    NF_deseada = 60

    # Calculamos el promedio de los certámenes sin considerar C3
    # Sabemos que NF = NC * 0.7 + NL * 0.3
    # Para encontrar la nota necesaria en C3, resolvemos la ecuación para C3
    # NF_deseada = ((C1 + C2 + C3) / 3) * 0.7 + NL * 0.3
    
    # Aislamos NC:
    NC_deseada = (NF_deseada - (NL * 0.3)) / 0.7
    
    # Ahora, NC_deseada = (C1 + C2 + C3) / 3, por lo tanto:
    C3_necesaria = NC_deseada * 3 - C1 - C2

    # Mostramos la nota necesaria en el tercer certamen
    print(f"Para obtener una nota final de {NF_deseada}, necesitas una nota de {C3_necesaria} en el tercer certamen.")
    
# Llamamos a la función para ejecutar el programa
calcular_nota_necesaria()
