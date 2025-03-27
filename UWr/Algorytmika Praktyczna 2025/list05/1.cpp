#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> tree;
vector<int> depth;

void dfs(int h, int node, int parent, int &maxNode){
    depth[node] = h;
    if (h > depth[maxNode]) maxNode = node;

    for (int u: tree[node]){
        if (u != parent){
            dfs(h + 1, u, node, maxNode);
        }
    }
}

int find(int n){
    int maxNode = 1;
    depth.assign(n + 1, 0);
    dfs(0, 1, 0, maxNode);

    depth.assign(n + 1, 0);
    dfs(0, maxNode, 0, maxNode);
    
    return depth[maxNode];
}




int main(){
    int N;
    cin >> N;
    tree.resize(N + 1);
    for (int i=0; i<N; i++){
        int a, b;
        cin >> a >> b;
        tree[a].push_back(b);
        tree[b].push_back(a);
    }

    cout << find(N) << '\n';
    return 0;
}