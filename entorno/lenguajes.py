import itertools

def obtener_prefijos(cadena: str) -> list[str]:
    return [cadena[:i] for i in range(len(cadena) + 1)]

def obtener_sufijos(cadena: str) -> list[str]:
    return [cadena[len(cadena)-i:] for i in range(len(cadena) + 1)]

def obtener_subcadenas(cadena: str) -> list[str]:
    subcadenas = set()
    for i in range(len(cadena) + 1):
        for j in range(i, len(cadena) + 1):
            subcadenas.add(cadena[i:j])
    return sorted(list(subcadenas), key=len)

def estimar_cantidad_cadenas(tamaño_alfabeto: int, n: int, es_positiva: bool = False) -> int:
    if tamaño_alfabeto == 0:
        return 0 if es_positiva else 1
    if tamaño_alfabeto == 1:
        return n if es_positiva else n + 1
    
    # Suma de la serie geométrica: (k^(n+1) - 1) / (k - 1)
    total = (tamaño_alfabeto**(n + 1) - 1) // (tamaño_alfabeto - 1)
    return total - 1 if es_positiva else total

def calcular_cerradura(alfabeto: str, n: int, es_positiva: bool = False) -> list[str]:
    simbolos = list(set(alfabeto.replace(" ", "").replace(",", "")))
    cantidad = estimar_cantidad_cadenas(len(simbolos), n, es_positiva)
    
    if cantidad > 200000:
        raise ValueError(f"Rechazado: La combinación generaría {cantidad:,} cadenas, excediendo el límite de 200,000.")

    resultado = []
    inicio = 1 if es_positiva else 0
    
    for i in range(inicio, n + 1):
        for tupla in itertools.product(simbolos, repeat=i):
            resultado.append("".join(tupla))
    
    return resultado