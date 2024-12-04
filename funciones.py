import random

def inicializar_matriz(cantidad_filas:int,cantidad_columnas:int)-> list:
    matriz = []
    
    for _ in range(cantidad_filas):
        fila = [0] * cantidad_columnas
        matriz += [fila]
    return matriz

matriz_votos = inicializar_matriz(5,5)

def cargar_datos()-> None:
    """
    Esta funcion se encarga de pidir datos para despues cargarlos en la matriz inicializada anteriormente
    """

    for i in range(len(matriz_votos)):
        for j in range(len(matriz_votos[i])):
            if j == 0:
                numero = int(input("Ingrese el numero del participante: "))
                while numero > 5  or numero < 1:
                    numero = int(input("Porfavor ingrese un particiapante valido: "))
            else:
                while True:
                    if j == 1:
                        numero = int(input("Ingrese el voto del jurado 1: "))
                        while numero > 100 or numero < 1:
                            numero = int(input("Porfavor reingrese un numero del 1 al 100: "))
                    elif j == 2:
                        numero = int(input("Ingrese el voto del jurado 2: "))
                        while numero > 100 or numero < 1:
                            numero = int(input("Porfavor reingrese un numero del 1 al 100: "))
                    elif j == 3:
                        numero = int(input("Ingrese el voto del jurado 3: "))
                        while numero > 100 or numero < 1:
                            numero = int(input("Porfavor reingrese un numero del 1 al 100: "))
                    if numero > 0:
                        break
                    else:
                        print("No se permiten votos negativos.")
            matriz_votos[i][j] = numero

def mostrar_matriz(matriz:list)-> None:
    """
    Esta funcion te muestra la matriz con un formato lindo con los datos ingresados
    """

    for i in range(len(matriz)):
        print(f"\nParticipante: {matriz[i][0]}\n------------------------\nVoto Jurado 1: {matriz[i][1]}\n------------------------\nVoto Jurado 2: {matriz[i][2]}\n------------------------\nVoto Jurado 3: {matriz[i][3]}\n------------------------\nPromedio votos: {matriz[i][4]} ")

def calcular_promedio(matriz:list)-> None:
    """
    Esta funcion se encarga de calcular los promedios de cada participante
    """

    for i in range(len(matriz)):
        total = 0
        for j in range(1, 4):
            total = total + matriz[i][j]

        promedio = total / 3
        matriz[i][4] = round(promedio, 2)

def ordenar_por_promedio(matriz:list)-> None:
    """
    Esta funcion se encarga de comparar todas las matrices y ordenarlas de forma que se muestren de mayor a menor por orden los promedios
    """
    
    for i in range(len(matriz)):
        for j in range(i + 1, len(matriz)):
            if matriz[i][4] < matriz[j][4]:
                for k in range(len(matriz[0])):
                    aux = matriz[i][k]
                    matriz[i][k] = matriz[j][k]
                    matriz[j][k] = aux
    for i in range(len(matriz)):
        print(f"\nParticipante: {matriz[i][0]}\n------------------------\nVoto Jurado 1: {matriz[i][1]}\n------------------------\nVoto Jurado 2: {matriz[i][2]}\n------------------------\nVoto Jurado 3: {matriz[i][3]}\n------------------------\nPromedio votos: {matriz[i][4]} ")

def encontrar_peores_tres(matriz:list)-> None:
    """
    Esta funcion se encarga de comparar todas las matrices, encontrar y mostrar las 3 matrices con peores promedios
    """
    contador = 0

    for i in range(len(matriz)):
        for j in range(i + 1, len(matriz)):
            if matriz[i][4] > matriz[j][4]:
                for k in range(len(matriz[0])):
                    aux = matriz[i][k]
                    matriz[i][k] = matriz[j][k]
                    matriz[j][k] = aux
    print(f"\nLos 3 participantes con los peores promedios\n------------------------")

    for i in range(len(matriz)):
        if contador == 3:
            break
        contador = contador + 1
        print(f"\nParticipante: {matriz[i][0]}\n------------------------\nVoto Jurado 1: {matriz[i][1]}\n------------------------\nVoto Jurado 2: {matriz[i][2]}\n------------------------\nVoto Jurado 3: {matriz[i][3]}\n------------------------\nPromedio votos: {matriz[i][4]} ")

def mostrar_mayores_promedios(matriz:list)-> None:
    """
    Esta funcion se encarga de buscar entre el promedio de todas las matrices y mostrar aquellas que superen el promedio general
    """

    promedio_total = 0
    for i in range(len(matriz)):
        promedio_total = promedio_total + matriz[i][4]
    promedio_general = promedio_total / len(matriz)
    print(f"\nPromedio general de todos los participantes: {promedio_general:.2f}")

    print(f"\nParticipantes que superan el promedio general\n------------------------")
    for i in range(len(matriz)):
        if matriz[i][4] > promedio_general:
            print(f"\nParticipante: {matriz[i][0]}\n------------------------\nVoto Jurado 1: {matriz[i][1]}\n------------------------\nVoto Jurado 2: {matriz[i][2]}\n------------------------\nVoto Jurado 3: {matriz[i][3]}\n------------------------\nPromedio votos: {matriz[i][4]} ")

def jurado_malo(matriz: list) -> None:
    """
    Esta funcion se encaga de buscar entre todas las matrices para encontrar al jurado que en promedio a las notas que dio fue el peor
    """

    total_jurado_1 = 0
    total_jurado_2 = 0
    total_jurado_3 = 0

    for i in range(len(matriz)):
        total_jurado_1 = total_jurado_1 + matriz[i][1]
        total_jurado_2 = total_jurado_2 + matriz[i][2]
        total_jurado_3 = total_jurado_3 + matriz[i][3]

    promedio_jurado_1 = total_jurado_1 / len(matriz)
    promedio_jurado_2 = total_jurado_2 / len(matriz)
    promedio_jurado_3 = total_jurado_3 / len(matriz)

    peor_promedio = promedio_jurado_1
    if promedio_jurado_2 < peor_promedio:
        peor_promedio = promedio_jurado_2
    if promedio_jurado_3 < peor_promedio:
        peor_promedio = promedio_jurado_3
    
    print(f"\nEl jurado con el peor promedio dado\n------------------------")
    
    if promedio_jurado_1 == peor_promedio:
        print(f"jurado 1 con promedio de {promedio_jurado_1:.2f}")
    if promedio_jurado_2 == peor_promedio:
        print(f"jurado 2 con promedio de {promedio_jurado_2:.2f}")
    if promedio_jurado_3 == peor_promedio:
        print(f"jurado 3 con promedio de {promedio_jurado_3:.2f}")

def buscar_participantes_por_sumatoria(matriz: list) -> None:

    numero = int(input("Ingrese un número entre 3 y 300: "))
    while numero < 3 or numero > 300:
        numero = int(input("Por favor, ingrese un número válido (entre 3 y 300): "))

    encontrados = False
    
    for i in range(len(matriz)):
        suma_notas = matriz[i][1] + matriz[i][2] + matriz[i][3]
        if suma_notas == numero:
            print(f"\nLos participantes encontrados fueron\n------------------------\nParticipante {matriz[i][0]}: {matriz[i][1]} + {matriz[i][2]} + {matriz[i][3]} = {numero}")
            encontrados = True
    if encontrados == False:
        print(f"No se encontro un participante que la suma de sus notas sea {numero}")

def definir_ganador(matriz: list) -> None:
    """
    Esta funcion se encarga de buscar el ganador del concurso por el promedio, en caso de empate se va a una estancia aparte para que los jurados voten por 1, si vuelve a haber empate se elijira de manera random
    """
    mayor_promedio = matriz[0][4]
    for i in range(1, len(matriz)):
        if matriz[i][4] > mayor_promedio:
            mayor_promedio = matriz[i][4]
    
    posibles_ganadores = [0] * len(matriz)
    votos_jurados = [0] * len(matriz)
    cantidad_ganadores = 0

    for i in range(len(matriz)):
        if matriz[i][4] == mayor_promedio:
            posibles_ganadores[cantidad_ganadores] = matriz[i][0]
            cantidad_ganadores = cantidad_ganadores + 1
    
    if cantidad_ganadores == 1:
        return print(f"El ganador es el participante {posibles_ganadores[0]} con un promedio de {mayor_promedio:.2f}")
    else:
        for i in range(1, 4):
            print(f"\nJurado {i}, eleji al participante ganador:")
            while True:
                voto_jurado = int(input("Escriba el número del participante: "))
                for k in range(cantidad_ganadores):
                    if posibles_ganadores[k] == voto_jurado:
                        votos_jurados[k] += 1
                        break

    max_votos = votos_jurados[0]
    cantidad_empate = 1
    ganadores_por_votos = [posibles_ganadores[0]]

    for i in range(1, cantidad_ganadores):
        if votos_jurados[i] > max_votos:
            max_votos = votos_jurados[i]
            ganadores_por_votos = [posibles_ganadores[i]]
            cantidad_empate = 1
        elif votos_jurados[i] == max_votos:
            ganadores_por_votos = ganadores_por_votos + [posibles_ganadores[i]]
            cantidad_empate = cantidad_empate + 1
    
    if cantidad_empate == 1:
        print(f"\nEl ganador por elejido por los jurados es el participante {ganadores_por_votos[0]}.")
    else:
        ganador_final = ganadores_por_votos[random.randint(0, cantidad_empate - 1)]
        print(f"\nlos jurados no llegaron a un acuerdo en el desempate y el ganado va a ser aleatorio\nEl ganador es el participante {ganador_final}")