#include <iostream>
#include <sstream>
#include <algorithm>
#include <string>
#include <fstream>
#define fastIO ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)

using namespace std;
/*
 * Se añadieron ciertas verificaciones para evitar un posible error a la hora de leer 
 * los datos de entrada. Además, en caso de que el dinero de peter no tuviera una suma exacta
 * se añadio un if y else para imprimr, "no se encontro una solucion"
*/
int main()
{
    fastIO;
    std::string linea;
    while (std::getline(std::cin >> std::ws, linea))
    {
        std::stringstream ss(linea);
        int n, m;
        ss >> n;
        int *p = new int[n];
        for (int i = 0; i < n; i++)
        {
            if (!(std::cin >> p[i]))
            {
                // Error de entrada
                delete[] p;
                std::cerr << "Error de entrada.\n";
                return 1;
            }
        }
        if (!(std::cin >> m))
        {
            // Error de entrada
            delete[] p;
            std::cerr << "Error de entrada.\n";
            return 1;
        }

        int minDiff = 1000002, l = -1, r = -1;

        std::sort(p, p + n);

        for (int i = 0; i < n; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                if (p[i] + p[j] == m)
                {
                    if (p[j] - p[i] < minDiff)
                    {
                        minDiff = p[j] - p[i];
                        l = i;
                        r = j;
                    }
                }
            }
        }

        if (l != -1 && r != -1)
        {
            std::cout << "Peter should buy books whose prices are " << p[l] << " and " << p[r] << "." << "\n";
        }
        else
        {
            std::cout << "No se encontró una solución.\n";
        }

        std::cout << "\n";

        delete[] p;
    }

    return 0;
}
