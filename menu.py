from funciones import *

def menu():
    print (f"\n****Elecciones centro de estudiante!!!!! ****")
    while True:
        print("\nMenu de Opciones:\n")
        print("1. Cargar Votos")
        print("2. Calcular promedio")
        print("3. Mostrar participantes")
        print("4. Ordenar y mostrar participantes por promedio")
        print("5. Encontrar y mostrar los peores 3 promedios")
        print("6. Muestrar los participantes que superen el promedio general")
        print("7. Encontrar y mostrar al jurado con los peores promedios dados")
        print("8. Encontrar participante con sumatoria de sus notas a nota ingresada")
        print("9. Encontrar el ganador, en caso de empate los jurados votaran por el ganador")
        print("10. Salir")

        opcion = int(input("\nSeleccione una opción: "))
        
        if opcion == 1:
            cargar_datos()
        elif opcion == 2:
            calcular_promedio(matriz_votos)
        elif opcion == 3:
            mostrar_matriz(matriz_votos)
        elif opcion == 4:
            ordenar_por_promedio(matriz_votos)
        elif opcion == 5:
            encontrar_peores_tres(matriz_votos)
        elif opcion == 6:
            mostrar_mayores_promedios(matriz_votos)
        elif opcion == 7:
            jurado_malo(matriz_votos)
        elif opcion == 8:
            buscar_participantes_por_sumatoria(matriz_votos)
        elif opcion == 9:
            definir_ganador(matriz_votos)
        elif opcion == 10:
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intente nuevamente.")

menu()