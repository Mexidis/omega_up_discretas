def es_reflexiva(conjunto, pares):
    for elemento in conjunto:
        if (elemento, elemento) not in pares:
            return False
    return True

def es_simetrica(pares):
    for par in pares:
        inverso = (par[1], par[0])
        if inverso not in pares:
            return False
    return True

def es_transitiva(pares):
    for par1 in pares:
        for par2 in pares:
            if par1[1] == par2[0]:
                nueva_relacion = (par1[0], par2[1])
                if nueva_relacion not in pares:
                    return False
    return True

# Entrada de datos
conjunto_A = input().split(',')
n = int(input())
pares_relacion = [tuple(input().split(',')) for _ in range(n)]

# Verificar el tipo de relación
reflexiva = es_reflexiva(conjunto_A, pares_relacion)
simetrica = es_simetrica(pares_relacion)
transitiva = es_transitiva(pares_relacion)

# Determinar el resultado
if reflexiva and simetrica and transitiva:
    print("Equivalencia")
elif reflexiva:
    print("Reflexiva")
elif simetrica:
    print("Simétrica")
elif transitiva:
    print("Transitiva")
else:
    print("No")
#será o no?
