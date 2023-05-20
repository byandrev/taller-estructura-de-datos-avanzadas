from collections import defaultdict

class Solution:
    def validPath(self, n, edges, start, end):
        graph = defaultdict(list)

        # Construir el grafo utilizando la lista de aristas
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            if node == end:
                return True

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True

            return False

        return dfs(start)


def generar_archivos():
    # Datos de entrada
    n = 6
    edges = [[0, 5], [3, 2], [7, 3], [5, 4],[3,3],[3,3]]
    start = 0
    end = 4

    # Generar archivo de entrada
    with open("in.txt", "w") as archivo_entrada:
        archivo_entrada.write(f"{n}\n")
        for edge in edges:
            archivo_entrada.write(f"{edge[0]} {edge[1]}\n")
        archivo_entrada.write(f"{start} {end}\n")

    # Obtener resultado de la solución
    solution = Solution()
    resultado = solution.validPath(n, edges, start, end)

    # Generar archivo de salida
    with open("out.txt", "w") as archivo_salida:
        archivo_salida.write(str(resultado))


# Ejecutar la función para generar los archivos
generar_archivos()
