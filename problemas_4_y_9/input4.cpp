#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

// Estructura para representar una arista
struct Edge {
    int u, v;

    Edge(int u, int v) : u(u), v(v) {}
};

// Función para generar un caso de árbol aleatorio
vector<Edge> generarArbol(int n) {
    vector<Edge> edges;

    // Generar árbol aleatorio
    for (int i = 1; i < n; i++) {
        int v = rand() % i;
        edges.push_back(Edge(v, i));
    }

    return edges;
}

int main() {
    // Semilla aleatoria
    srand(time(nullptr));

    int casos = 100;

    ofstream archivo("casos4.txt"); // Abre el archivo en modo de escritura

    if (archivo.is_open()) {
        for (int i = 0; i < casos; i++) {
            int n = rand() % 100 + 1; // Tamaño aleatorio entre 1 y 100

            // Generar un caso de árbol aleatorio
            vector<Edge> edges = generarArbol(n);

            // Escribir el caso en el archivo
            archivo << n << endl;
            for (int j = 0; j < edges.size(); j++) {
                archivo << edges[j].u << " " << edges[j].v << " ";
            }
            archivo << endl;
            
        }

        archivo.close(); // Cierra el archivo
    }
    else {
        cout << "No se pudo abrir el archivo." << endl;
    }

    return 0;
}
