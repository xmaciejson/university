#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> tree;
vector<vector<int>> sko;

void dfs(int node, int parent) {
    sko[node][0] = 0;  // Jeśli node nie jest w skojarzeniu
    sko[node][1] = 0;  // Jeśli node jest w skojarzeniu

    for (int child : tree[node]) {  
        if (child == parent) continue;  // Pomijamy rodzica, żeby nie wrócić w górę drzewa
        dfs(child, node);  // Rekurencyjne wywołanie dla dziecka

        sko[node][0] += sko[child][1];  // Jeśli node nie jest w skojarzeniu, dziecko może być

        sko[node][1] = max(sko[node][1], 1 + sko[child][0]);  // Jeśli node jest w skojarzeniu, dziecko nie może
    }
}

int main() {
    int N;
    cin >> N;
    tree.resize(N);
    for (int i = 0; i < N - 1; i++) {  // W drzewie jest N-1 krawędzi
        int a, b;
        cin >> a >> b;
        a--, b--;  // Przechodzimy na indeksowanie od zera
        tree[a].push_back(b);
        tree[b].push_back(a);
    }

    int root = 0;  // Możesz ustawić root na 0 (pierwszy wierzchołek)
    dfs(root, -1);  // Wywołanie DFS z korzenia

    cout << max(sko[root][0], sko[root][1]);  // Wynik to maksymalne skojarzenie dla korzenia
    return 0;
}
