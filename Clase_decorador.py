from math import comb
from time import perf_counter

# Definimos decorador para medir el tiempo de ejecución de los métodos
def tiempoEjecucion(func):  
    
    def tiempoPCB(self, *args, **kwargs):
        tiempo_ini = perf_counter() # Inicio del tiempo de ejecución
        resultado = func(self, *args, **kwargs) # Ejecución del método
        tiempo_fin = perf_counter() # Fin del tiempo de ejecución
        tiempo_total = tiempo_fin - tiempo_ini   
        return resultado, tiempo_total
    
    return tiempoPCB

# Definimos la clase caminosPCB
class caminosPCB:
    def __init__(self, ancho ,largo): 
        self.n = ancho # Definimos el ancho de la grilla
        self.m = largo # Definimos el largo de la grilla
        self.grilla = [[1 for i in range(self.m)] for j in range(self.n)] # Inicializamos la grilla con 1 en todas las posiciones
 
    # Definimos posibles caminos recursivos utilizando fuerza bruta
    def posiblesCaminos_1(self): 
        for i in range(1, self.n):
            for j in range(1, self.m): 
                self.grilla[i][j] = self.grilla[i-1][j] + self.grilla[i][j-1] # Calculamos el número de caminos posibles para llegar a la celda i,j
        return self.grilla[self.n-1][self.m-1] # Retornamos el número de caminos posibles para llegar a la celda inferior derecha
    
    # Definimos el camino utilizando la combinatoria
    def posiblesCaminos_2(self):
        combinatoria = comb(self.n + self.m - 2, self.n - 1) # Calculamos el número de caminos posibles utilizando la combinatoria
        return int(combinatoria)
    
    # Utilizamos el decorador en método para cambiar la forma en que se calcula la solución
    @tiempoEjecucion
    def elegirMetodo(self, metodo):
        if metodo == 1:
            return self.posiblesCaminos_1()
        elif metodo == 2:
            return self.posiblesCaminos_2()
        else:
            raise ValueError("Metodo no valido")   