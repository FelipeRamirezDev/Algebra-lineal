from algoritmos import distancia_euclidiana, determinante_matriz_2x2

class Particula:
    def __init__(self, id = 0, origen_x = 0, origen_y = 0, destino_x = 0, destino_y = 0, velocidad = 0, red = 0, green = 0, blue = 0):
        self.__id = id
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__distancia = round( distancia_euclidiana( origen_x, origen_y, destino_x, destino_y ), 2 )# Se redondea a 2 decimales
        self.__determinante = self.calcular_determinante()
        
        
    def calcular_determinante(self):
        """
        Calcula el determinante de la matriz formada por las coordenadas de origen y destino de la partícula.
        
        Returns:
            float: El valor del determinante de la matriz 2x2 formada por las coordenadas de origen y destino.
        """
        matriz = [[self.__origen_x, self.__origen_y], [self.__destino_x, self.__destino_y]]
        return determinante_matriz_2x2(matriz)
    
    def __str__(self):
        return(
            'ID: ' + str( self.__id ) + '\n' 
            'Origen x: ' + str( self.__origen_x ) + '\n'
            'Origen y: ' + str( self.__origen_y ) + '\n'
            'Destino x: ' + str( self.__destino_x ) + '\n'
            'Destino y: ' + str( self.__destino_y ) + '\n'
            'Velocidad: ' + str( self.__velocidad ) + '\n'
            'Red: ' + str( self.__red ) + '\n'
            'Green: ' + str( self.__green ) + '\n'
            'Blue: ' + str( self.__blue ) + '\n'
            'Distancia: ' + str( self.__distancia ) + '\n'
            'Determinante: ' + str(self.__determinante) + '\n'
        )
        
    def to_dict(self):
        return {
            "id": self.__id,
            "origen_x": self.__origen_x,
            "origen_y": self.__origen_y,
            "destino_x": self.__destino_x,
            "destino_y": self.__destino_y,
            "velocidad": self.__velocidad,
            "red": self.__red,
            "green": self.__green,
            "blue": self.__blue
        }
        
    @property
    def id(self):
        return self.__id
    
    @property
    def origen_x(self):
        return self.__origen_x
    
    @property
    def origen_y(self):
        return self.__origen_y
    
    @property
    def destino_x(self):
        return self.__destino_x
    
    @property
    def destino_y(self):
        return self.__destino_y
    
    @property
    def velocidad(self):
        return self.__velocidad
    
    @property
    def red(self):
        return self.__red
    
    @property
    def green(self):
        return self.__green
    
    @property
    def blue(self):
        return self.__blue
    
    @property
    def distancia(self):
        return self.__distancia
    
    @property
    def determinante(self):
        return self.__determinante
