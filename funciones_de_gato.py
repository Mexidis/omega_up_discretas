def verificar_inyectividad(pares_seleccionados, conjunto1, conjunto2):
    valores_conjunto1 = [par.split(',')[0] for par in pares_seleccionados]
    valores_conjunto2 = [par.split(',')[1] for par in pares_seleccionados]

    # Verificar que todos los primeros elementos de los pares estén en conjunto1
    primeros_elementos_validos = all(valor in conjunto1 for valor in valores_conjunto1)

    # Verificar que cada elemento en conjunto2 reciba exactamente un elemento de conjunto1
    asignaciones_validas = len(set(valores_conjunto2)) == len(valores_conjunto2)

    return primeros_elementos_validos and asignaciones_validas


def verificar_suprayectividad(pares_seleccionados, conjunto1, conjunto2):
    valores_conjunto2 = [par.split(',')[1] for par in pares_seleccionados]

    return set(valores_conjunto2) == conjunto2


def verificar_biyectividad(pares_seleccionados, conjunto1, conjunto2):
    resultado_inyectividad = verificar_inyectividad(pares_seleccionados, conjunto1, conjunto2)
    resultado_suprayectividad = verificar_suprayectividad(pares_seleccionados, conjunto1, conjunto2)

    # Imprimir información sobre la inyectividad
    if resultado_inyectividad and resultado_suprayectividad:
        print("Biyectiva")
    elif resultado_inyectividad:
        print("Inyectiva")
    elif resultado_suprayectividad:
        print("Suprayectiva")
    else:
        print("No")


# Ejemplo de uso
conjunto1 = set(input().split(','))
conjunto2 = set(input().split(','))

num_pares = int(input())
#pares_seleccionados = [input(f"Ingrese el par {i+1} separado por comas: ") for i in range(num_pares)]
pares_seleccionados = [input() for _ in range(num_pares)]

verificar_biyectividad(pares_seleccionados, conjunto1, conjunto2)
#ah caray, se subió el commit?
