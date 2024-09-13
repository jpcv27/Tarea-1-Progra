# Tarea-1-Progra
## Teoricas: 
### P1: ¿Qué es un paradigma de programación?

Un paradigma de programación es una forma de clasificar ciertas características de los lenguajes de programación. Estos definen la organización, estructura y el razonamiento de los programas para resolver tareas específicas. En el caso de Python, tiene un paradigma orientado a objetos.

### P2: ¿En qué se basa la programación orientada a objetos?

La programación  en objetos (POO) es uno de los paradigmas  más utilizados dentro de la programación y está basado principalmente en las clases, campos y métodos, y como estos interactúan entre sí para modelar y dar soluciones tanto a problemas triviales como complejos. Los objetos son instancias de la clase y modelan objetos del mundo real, conceptos abstractos y procesos. Por otro lado, las clases se definen como plantillas que crean los objetos, asignan sus atributos, acciones y propiedades. Además. este tipo de paradigma posee herencia, lo cual permite crear nuevas clases  a partir de otras existentes, ofreciendo  la posibilidad de reutilizar código ya existente y modificarlo.

### P3: ¿Cuál es la diferencia entre recursividad e iteración, y cómo se relaciona esto con la notación big 𝑂?

La principal diferencia entre recursividad e iteración es el como se ejecutan los bucles para realizar  las repeticiones. En el caso de la recursividad, es una función que se llama a sí misma (directa o indirectamente), descomponiendo el problema en subproblemas hasta llegar a un caso base. Por otro lado, la iteración es un bucle (generalmente usando for o while) que se repite hasta cumplir cierta condición  (dependiendo de que se busca). La notación big O se utiliza para determinar el rendimiento de los algoritmos, y dependiendo de si se ocupa recursividad o iteración, la eficiencia de los algoritmos puede variar. 

### P4: Explicar la diferencia de rendimiento entre 𝑂(1) y 𝑂(𝑛)

El rendimiento de O(1) implica un tiempo constante, es decir que el tiempo que tomará en realizar el algoritmo es independiente al tamaño de entrada, es decir, no importa cuantos datos se agreguen o quiten, el algoritmo siempre dará el mismo valor. Por otro lado, el rendimiento O(n) implica un tiempo lineal, es decir que el tiempo que le tomará al algoritmo dependerá directamente del tamaño de la entrada.

### P5: ¿Cómo se calcula el orden en un programa que funciona por etapas?

El cálculo de la complejidad de un programa que funciona por etapas se realiza evaluando cada parte de este por separado, para finalmente combinarlo y obtener la complejidad final del programa. Para ello, se debe ir tomando cada bloque que tenga complejidad y analizarlo dentro del programa, en ese sentid, pueden existir distintos casos, por ejemplo si existe un bucle dentro de otro, se multiplican sus complejidades.

### P6: ¿Cómo se puede determinar la complejidad temporal de un algoritmo recursivo?

En algoritmos recursivos, una manera de determinar su complejidad es utilizando el teorema maestro, el cual tiene la fórmula de T(n) = aT(n/b) + f(n), en donde T(n) es el tiempo total, n es el tamaño del problema a resolver, (n/b) es el tamaño de cada subproblema, a es el número de subproblemas de la recursión y f(n) es el costo de trabajo fuera de las llamadas recursivas.




