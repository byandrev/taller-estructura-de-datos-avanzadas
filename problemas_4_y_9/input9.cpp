#include <iostream>
#include <fstream>
#include <random>

int main() {
    // Generador de números aleatorios
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int> dist(1, 1000);  // Rango de enteros positivos

    // Nombre del archivo de salida
    std::string nombreArchivo = "casos.txt";

    // Crear un objeto de archivo de salida
    std::ofstream archivo(nombreArchivo);

    if (!archivo) {
        std::cout << "No se pudo abrir el archivo de salida." << std::endl;
        return 1;
    }

    // Generar 100 casos de arreglos
    const int numCasos = 100;

    for (int i = 0; i < numCasos; ++i) {
        // Generar tamaño del arreglo entre 5 y 50
        std::uniform_int_distribution<int> tamDist(5, 50);
        int tamArreglo = tamDist(gen);

        // Escribir el tamaño del arreglo en el archivo
        archivo << tamArreglo << std::endl;

        // Generar un caso de arreglo
        for (int j = 0; j < tamArreglo; ++j) {
            int numero = dist(gen);
            archivo << numero << " ";
        }
        archivo << std::endl << std::endl;  // Separador de casos (dos nuevas líneas)
    }

    archivo.close();
    std::cout << "Se generaron exitosamente los casos en el archivo: " << nombreArchivo << std::endl;

    return 0;
}