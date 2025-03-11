#include <iostream>
#include <vector>

using namespace std;

const int MAX_N = 200000;
vector<int> graph[MAX_N + 1];
vector<int> subtree_size(MAX_N + 1, 0);

void dfs(int node) {
    subtree_size[node] = 0;
    for (int child : graph[node]) {
        dfs(child);
        subtree_size[node] += (subtree_size[child] + 1);
    }
}

int main() {
    int n;
    cin >> n;
    
    for (int i = 2; i <= n; i++) {
        int parent;
        cin >> parent;
        graph[parent].push_back(i);
    }

    dfs(1);

    for (int i = 1; i <= n; i++) {
        cout << subtree_size[i] << " ";
    }
    cout << endl;

    return 0;
}
