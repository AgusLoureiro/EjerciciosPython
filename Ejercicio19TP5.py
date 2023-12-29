
#Utilizando for

def procesar_lista_personas_for(cantidad_personas):
    for _ in range(cantidad_personas):
        sueldo = float(input("Ingrese el sueldo: "))
        impuestos = float(input("Ingrese monto destinado a impuestos: "))
        comida = float(input("Ingrese monto destinado a comida: "))
        colegio = float(input("Ingrese monto destinado al colegio: "))

        porc_impuestos = porcentaje_impuestos(sueldo, impuestos)
        porc_comida = porcentaje_comida(sueldo, comida)
        porc_colegio = porcentaje_colegio(sueldo, colegio)

        print(f"Porcentaje de sueldo destinado a impuestos: {porc_impuestos}%")
        print(f"Porcentaje de sueldo destinado a comida: {porc_comida}%")
        print(f"Porcentaje de sueldo destinado al colegio: {porc_colegio}%")
        print("----------")

cantidad_personas = 50
procesar_lista_personas_for(cantidad_personas)
