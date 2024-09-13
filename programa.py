# Programa 
import matplotlib.pyplot as plt
from time import perf_counter
from Clase_decorador import caminosPCB

# Se inicializan listas para guardar los tiempos de ejecución
t_camino_1 = []
t_camino_2 = []

i = 5000 # Tamaño de la grilla i x i

for n in range(1, i):
    
    # Tiempo de ejecución para el método 1
    tiempo_inicio = perf_counter()
    caminos = caminosPCB(n, n) # Inicializamos la clase caminosPCB con uan grilla de n x n
    caminos.elegirMetodo(1)
    tiempo_total = perf_counter() - tiempo_inicio
    t_camino_1.append(tiempo_total) 

   # Tiempo de ejecución para el método 2
    tiempo_inicio = perf_counter()
    caminos = caminosPCB(n, n) # Inicializamos la clase caminosPCB con uan grilla de n x n
    caminos.elegirMetodo(2)
    tiempo_total = perf_counter() - tiempo_inicio
    t_camino_2.append(tiempo_total)  

# Se grafican los tiempos de ejecución
plt.plot(t_camino_1, label='Metodo 1')
plt.plot(t_camino_2, label='Metodo 2')
plt.xlabel("Tamano de la grilla")
plt.ylabel("Tiempo (s)")
plt.title("Tiempo de ejecucion de los metodos")
plt.legend()
plt.savefig(f"tiempo_ejecucion_con_{i}x{i}.svg")
plt.show()