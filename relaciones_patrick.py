def es_reflexiva(relacion, conjunto):
    # Verificar que para cada elemento exista al menos un par reflexivo
    for elemento in conjunto:
        tiene_par_reflexivo = any((a, b) in relacion for a, b in relacion if a == elemento and b == elemento)
        if not tiene_par_reflexivo:
            return False

    return True
#no lo se rick parece falso
def verificar_relacion(conjunto, n, relaciones):
    reflexiva = es_reflexiva(relaciones, conjunto)
    simetrica = True
    transitiva = True

    # Verificar propiedad simétrica
    for a, b in relaciones:
        if (b, a) not in relaciones:
            simetrica = False

    # Verificar propiedad transitiva
    for a, b in relaciones:
        for c, d in relaciones:
            if b == c and (a, d) not in relaciones:
                transitiva = False

    # Determinar el tipo de relación
    if reflexiva and simetrica and transitiva:
        return "Equivalencia"
    elif reflexiva:
        return "Reflexiva"
    elif simetrica:
        return "Simétrica"
    elif transitiva:
        return "Transitiva"
    else:
        return "No"

# Ejemplo de uso
entrada = input()
n = int(input())
relaciones = set()

for _ in range(n):
    relacion = input().split(',')
    relaciones.add((relacion[0], relacion[1]))

# Convertir la entrada a lista de elementos y relaciones
conjunto = entrada.split(',')

# Verificar la relación y obtener la salida
resultado = verificar_relacion(conjunto, n, relaciones)
print(resultado)
