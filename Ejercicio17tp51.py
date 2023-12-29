#17 PARTE A:


def guarda_numeros():
    numeros = []
    datoIngresado = 1  # Iniciar con un valor distinto de cero
    
    while datoIngresado != 0:
        datoIngresado = int(input("Ingrese un número (ingrese 0 para terminar): "))
        if datoIngresado != 0:
            numeros.append(datoIngresado)
    
    return numeros

def promediar(numeros):
    return sum(numeros) / len(numeros) if numeros else 0

def sumar_lista(lista):
    return sum(lista)

def numero_maximo(numeros):
    return max(numeros) if numeros else None

def numero_minimo(numeros):
    return min(numeros) if numeros else None

def porcentaje():
    print("Calculador de porcentaje:")
    total = int(input("Ingrese el precio anterior del producto: "))
    valor = int(input("Ingrese el precio actual del producto: "))
    cuenta = ((valor - total) / total) * 100
    return f"El porcentaje de aumento es: {cuenta}%"

def cantidad_numeros(numeros):
    return len(numeros)

menuPrincipal = ''
numeros = []

while menuPrincipal != 7:
    menuPrincipal = int(input("Ingrese una opción del menú...\n 1- Promedio de los números \n 2- Suma de los numeros \n 3- Cantidad de numeros \n 4- Número máximo \n 5- Número mínimo \n 6- Porcentaje \n 7- Salir \n "))
    
    if menuPrincipal == 1:
        numeros = guarda_numeros()
        print(f"El promedio es: {promediar(numeros)}")
    elif menuPrincipal == 2:
        numeros = guarda_numeros()
        print(f"La suma es: {sumar_lista(numeros)}")
    elif menuPrincipal == 3:
        numeros = guarda_numeros()
        print(f"La cantidad de números es: {cantidad_numeros(numeros)}")
    elif menuPrincipal == 4:
        numeros = guarda_numeros()
        print(f"El número máximo es: {numero_maximo(numeros)}")
    elif menuPrincipal == 5:
        numeros = guarda_numeros()
        print(f"El número mínimo es: {numero_minimo(numeros)}")
    elif menuPrincipal == 6:
        print(porcentaje())
    elif menuPrincipal != 7:
        print("Ingrese una opción válida")

print("Saliendo del programa...")


#17 PARTE B 


def promediar(numeros):
    return sum(numeros) / len(numeros) if numeros else 0

def sumar_lista(lista):
    return sum(lista)

def numero_maximo(numeros):
    max_num = float('-inf')
    for num in numeros:
        if num > max_num:
            max_num = num
    return max_num if numeros else None

def numero_minimo(numeros):
    min_num = float('inf')
    for num in numeros:
        if num < min_num:
            min_num = num
    return min_num if numeros else None

def porcentaje(total, valor):
    cuenta = ((valor - total) / total) * 100 if total != 0 else 0
    return f"El porcentaje de cambio es: {cuenta}%"

