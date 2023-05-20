# EJERCICIO 1 FIND IF PATH EXISTS IN GRAPH

Este proyecto contiene una solución en Python para resolver un problema de determinar si hay un camino válido en un grafo desde un nodo de inicio hasta un nodo final. El algoritmo implementado utiliza la búsqueda en profundidad (DFS).

## Archivos

- `main.py`: Contiene la implementación de la clase `Solution` y el método `validPath` que resuelve el problema.
- `in.txt`: Archivo de entrada que contiene los datos de entrada para el problema.
- `out.txt`: Archivo de salida que contiene el resultado de la solución.

## Uso

1. Asegúrate de tener Python 3 instalado en tu sistema.
2. Ejecuta el archivo `main.py` para generar los archivos de entrada y salida.
3. Revisa el archivo `in.txt` para verificar los datos de entrada generados.
4. Ejecuta el archivo `main.py` para obtener el resultado del problema.
5. Revisa el archivo `out.txt` para ver el resultado de la solución.

## Datos de Entrada

Los datos de entrada se encuentran en el archivo `in.txt` y siguen el siguiente formato:

n
u1 v1
u2 v2

- `n` es el número de nodos en el grafo.
- Cada línea siguiente representa una arista en el grafo, donde `u` y `v` son los nodos conectados por la arista.
- La última línea contiene los nodos de inicio y final del camino que se debe verificar.

## Datos de Salida

El resultado de la solución se encuentra en el archivo `out.txt`. El archivo contiene un único número que indica si existe un camino válido desde el nodo de inicio hasta el nodo final en el grafo. Un resultado de `1` indica que hay un camino válido, mientras que un resultado de `0` indica que no hay un camino válido.

# EJERCICIO 2 C HEAP SOLUTIONS.

Este proyecto contiene un programa en Python que realiza operaciones en una estructura de datos llamada "heap". El programa lee una serie de operaciones desde la entrada estándar, las ejecuta en el heap y genera un archivo de salida con el resultado de las operaciones.

## Archivos

- `main.py`: Contiene el código principal del programa.
- `datos_entrada.txt`: Archivo de entrada que contiene los datos de entrada para el programa.
- `datos_salida.txt`: Archivo de salida que contiene el resultado de las operaciones.

## Uso

1. Asegúrate de tener Python 3 instalado en tu sistema.
2. Ejecuta el archivo `main.py` para ingresar los datos de entrada y generar los archivos de entrada y salida.
3. Revisa el archivo `datos_entrada.txt` para verificar los datos de entrada generados.
4. Ejecuta el archivo `main.py` para ejecutar las operaciones en el heap y generar el resultado.
5. Revisa el archivo `datos_salida.txt` para ver el resultado de las operaciones.

## Generar Archivos de Entrada y Salida

El programa incluye la función `generar_archivos()` que permite al usuario ingresar los datos de entrada y generar los archivos de entrada y salida. Para generar los archivos, sigue estos pasos:

1. Ejecuta el programa `main.py`.
2. Se te solicitará ingresar el número de registros.
3. A continuación, ingresa los registros uno por uno según el formato solicitado.
4. El programa generará los archivos `datos_entrada.txt` y `datos_salida.txt` con los datos y resultados correspondientes.

## Formato de Datos de Entrada

Los datos de entrada se ingresan en el archivo `datos_entrada.txt` y siguen el siguiente formato:

n
operacion1
operacion2

- `n` es el número de registros u operaciones a realizar.
- Cada línea siguiente representa una operación y se compone de una palabra clave seguida de uno o más argumentos separados por espacios.

El programa admite las siguientes operaciones:

- `insert x`: Inserta el elemento `x` en el heap.
- `getMin x`: Verifica si el elemento `x` es el mínimo en el heap. Si no es el mínimo, se realiza la operación `removeMin` y se inserta `x` en el heap.
- `removeMin`: Elimina el elemento mínimo del heap.

## Formato de Datos de Salida

El resultado de las operaciones se guarda en el archivo `datos_salida.txt` y sigue el siguiente formato:

m
operacion1
operacion2

- `m` es el número de operaciones realizadas.
- Cada línea siguiente representa una operación realizada, con la misma estructura que las operaciones de entrada.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún error o tienes alguna mejora, puedes abrir un "Issue" o enviar un "Pull Request" para discutir y colaborar en el proyecto.

¡Gracias!
