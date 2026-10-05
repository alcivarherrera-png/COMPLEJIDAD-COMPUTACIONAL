def busqueda_binaria(lista, objetivo):
    """Busca un valor en una lista ordenada usando búsqueda binaria.

    Args:
        lista: Lista ordenada de números.
        objetivo: Valor a buscar.

    Returns:
        El índice del valor si existe; de lo contrario, -1.
    """
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if lista[medio] == objetivo:
            return medio                 # T(n) = O(log n), es esta complejidad por que en
                                         # cada iteracion se reduce a la mitad el tamaño de la lista, 
                                         # siempre se hace menos pasos que n
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1


# Ejemplo de uso
numeros = [1, 3, 5, 7, 9, 11, 13, 15]
resultado = busqueda_binaria(numeros, 9)

if resultado != -1:
    print(f"El numero 9 se encontro en el indice {resultado}")
else:
    print("El numero no se encontro")
