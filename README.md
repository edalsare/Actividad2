# Actividad2 - instrucciones
Para la ejecucion del dodigo, se debe ejecutar el archivo Grafo.py con el interprete de python
para la correcta ejecucion del codigo se debe tener instalado en el equipo las librerias de "networkx" y "matplotlib" las cuales son las encargadas del funcionamiento del codigo
De las lineas #4 hasta la #29 se realiza el grafo que se utlizo para esta actividad, donde las letras representan las aristas y los numero son el peso de los vertices en las conexiones de cada arista.
En las lineas numero 31 a 35  se grafica dicho grafo
La linea 37 es e eje principal de este ejercicio esta linea encuentra la ruta  mas optima para llegar de un punto a otro, en el ejemplo para llegar desde el punto "A" hasta el punto "J", el componente o libreria "dijkstra" es la encargada de este proceso, para ello en primer lugar se le pasa como parametro el objeto o rutas dispuestas a evaluar en este caso el garfo denominado "G", posteriormente el parametro "source" indica el punto inicial del recorrido y el parametro "target" indica el punto final del recorrido o punto de llegada
 a continuacion se imprime por consola la ruta mas optima optenida por el algoritmo.
En las lineas 42 y 43 se grafica la ruta mas otima obtenida por el algoritmo, para ello se debe escribir la secuencia que se obtuvo  en la linea 37 y que se muestra con la linea 39.
