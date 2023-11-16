def verificar_inyectividad(pares_seleccionados, conjunto1, conjunto2):
    valores_conjunto1 = [par.split(',')[0] for par in pares_seleccionados]
    valores_conjunto2 = [par.split(',')[1] for par in pares_seleccionados]

    primeros_elementos_validos = all(valor in conjunto1 for valor in valores_conjunto1)
    print(primeros_elementos_validos)
    segundos_elementos_validos = all(valor in conjunto2 for valor in valores_conjunto2)
    print(segundos_elementos_validos)
    
    asignaciones_validas = all(valores_conjunto1.count(valor) == 1 for valor in conjunto1)
    print(asignaciones_validas)

    return asignaciones_validas and primeros_elementos_validos and segundos_elementos_validos


def verificar_suprayectividad(conjunto1, pares_seleccionados):
    valores_conjunto1 = [par.split(',')[0] for par in pares_seleccionados]
    valores_conjunto2 = [par.split(',')[1] for par in pares_seleccionados]

    if set(valores_conjunto1) == set(conjunto1):
        if all(any(par.split(',')[1] == valor for par in pares_seleccionados) for valor in valores_conjunto2):
            return True

    return False


def verificar_biyectividad(pares_seleccionados, conjunto1, conjunto2):
    resultado_inyectividad = verificar_inyectividad(pares_seleccionados, conjunto1, conjunto2)
    resultado_suprayectividad = verificar_suprayectividad(conjunto1, pares_seleccionados)

    if resultado_inyectividad and resultado_suprayectividad:
        print("Biyectiva")
    elif resultado_inyectividad:
        print("Inyectiva")
    elif resultado_suprayectividad:
        print("Suprayectiva")
    else:
        print("No")


# Ejemplo de uso
conjunto1 = set(input("Ingrese elementos del primer conjunto separados por comas: ").split(','))
conjunto2 = set(input("Ingrese elementos del segundo conjunto separados por comas: ").split(','))

num_pares = int(input("Ingrese la cantidad de pares a seleccionar: "))
pares_seleccionados = [input(f"Ingrese el par {i+1} separado por comas: ") for i in range(num_pares)]

verificar_biyectividad(pares_seleccionados, conjunto1, conjunto2)
