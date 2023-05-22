#include <iostream>
#include <fstream>
#include <vector>
#include <queue>

using namespace std;

vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
    vector<vector<int>> graph(n);
    vector<int> indegree(n, 0), ans;

    for (auto& e : edges) {
        graph[e[0]].push_back(e[1]);
        graph[e[1]].push_back(e[0]);
        indegree[e[0]]++;
        indegree[e[1]]++;
    }

    queue<int> q;
    for (int i = 0; i < n; i++) {
        if (indegree[i] == 1)
            q.push(i), indegree[i]--;
    }

    while (!q.empty()) {
        int s = q.size();
        ans.clear();
        for (int i = 0; i < s; i++) {
            int curr = q.front();
            q.pop();
            ans.push_back(curr);
            for (auto child : graph[curr]) {
                indegree[child]--;
                if (indegree[child] == 1)
                    q.push(child);
            }
        }
    }
    if (n == 1)
        ans.push_back(0);
    return ans;
}

int main() {
    int n, aux;
    cin >> n;
    vector<vector<int>> edges;
    for (int i = 0; i < n - 1; i++) {
        vector<int> v;
        for (int j = 0; j < 2; j++) {
            cin >> aux;
            v.push_back(aux);
        }
        edges.push_back(v);
    }
    vector<int> ans = findMinHeightTrees(n, edges);

    // Guardar el resultado en el archivo de texto
    ofstream archivo("resultado4.txt");
    if (archivo.is_open()) {
        archivo << "[";
        for (int i = 0; i < ans.size(); i++) {
            archivo << ans[i];
            if (i < ans.size() - 1) {
                archivo << ",";
            }
        }
        archivo << "]";
        archivo.close();
        cout << "El resultado se ha guardado en el archivo 'resultado4.txt'" << endl;
    } else {
        cout << "No se pudo abrir el archivo para escribir el resultado." << endl;
    }

    return 0;
}
