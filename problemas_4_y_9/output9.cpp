#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

int main() {
    // Nombre del archivo de salida
    std::string nombreArchivo = "resultado.txt";

    // Crear un objeto de archivo de salida
    std::ofstream archivo(nombreArchivo);

    if (!archivo) {
        std::cout << "No se pudo abrir el archivo de salida." << std::endl;
        return 1;
    }

    int n, x;
    std::cin >> n; // lee N
    std::vector<int> p; // crea vector para almacenar los enteros

    while (n--) { // recorre N, leyendo los ni, agregándolos al vector
        std::cin >> x;
        p.push_back(x);
    }

    std::sort(p.begin(), p.end()); // ordena el vector

    // elimina elementos repetidos
    p.erase(std::unique(p.begin(), p.end()), p.end());

    archivo << p.size() << std::endl; // guarda el tamaño final en el archivo

    archivo.close();
    std::cout << "El resultado se ha guardado exitosamente en el archivo: " << nombreArchivo << std::endl;

    return 0;
}
