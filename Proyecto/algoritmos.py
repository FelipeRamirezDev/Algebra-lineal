import math

#Formula de distancia entre dos puntos d = √((x2 - x1)² + (y2 - y1)²)
def distancia_euclidiana(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def puntos_mas_cercanos(puntos_list):
    resultado = []
    for punto_i in puntos_list:
        x1 = punto_i[0]
        y1 = punto_i[1]
        min = 1000
        cercano = (0, 0)
        for punto_j in puntos_list:
            if punto_i != punto_j:
                x2 = punto_j[0]
                y2 = punto_j[1]
                d = distancia_euclidiana(x1, y1, x2, y2)
                if d < min:
                    min = d
                    cercano = (x2, y2)
        
        resultado.append((punto_i, cercano))
    
    return resultado

def determinante_matriz_2x2(matriz):
    """
    Calcula el determinante de una matriz 2x2.

    Args:
        matriz (list): Una lista que representa una matriz 2x2 en forma de [[a, b], [c, d]].
    """
    a, b = matriz[0]
    c, d = matriz[1]
    return (a * d) - (b * c)


