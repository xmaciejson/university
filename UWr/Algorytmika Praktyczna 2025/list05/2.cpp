#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> tree;
vector<vector<int>> sko;

void dfs(int node, int parent) {
    sko[node][0] = 0;
    sko[node][1] = 0;

    for (int child : tree[node]) {
        if (child == parent) continue;
        dfs(child, node);

        sko[node][0] += max(sko[child][0], sko[child][1]);
    }

    for (int child : tree[node]) {
        if (child == parent) continue;
        sko[node][1] = max(sko[node][1], 1 + sko[child][0] + (sko[node][0] - max(sko[child][0], sko[child][1])));
    }
}

int main() {
    int N;
    cin >> N;
    tree.resize(N);
    sko.assign(N, vector<int>(2, 0));

    for (int i = 0; i < N - 1; i++) {
        int a, b;
        cin >> a >> b;
        a--, b--;
        tree[a].push_back(b);
        tree[b].push_back(a);
    }

    dfs(0, -1);

    cout << max(sko[0][0], sko[0][1]) << endl;
    return 0;
}
