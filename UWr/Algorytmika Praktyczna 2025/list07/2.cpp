#include <iostream>
using namespace std;

int const n = 800000;
long long tree[4 * n];

void build(int node, int left, int right){
    if (left == right){
        tree[node] = 1;
        return;
    }
    int mid = (left + right) / 2;
    build(node * 2, left, mid);
    build(node * 2 + 1, mid + 1, right);
    tree[node] = tree[node * 2] + tree[node * 2 + 1];
}

void update(int node, int left, int right, int idx){
    if (left == right){
        tree[node] = 0;
        return;
    }

    int mid = (left + right) / 2;
    if (idx <= mid){
        update(node * 2, left, mid, idx);
    }
    else{
        update(node * 2 + 1, mid + 1, right, idx);
    }
    tree[node] = tree[node * 2] + tree[node * 2 + 1];
}

int query(int node, int left, int right, int k){
    if (left == right){
        return left;
    }

    int mid = (left + right) / 2;
    if (tree[node * 2] >= k){
        return query(node * 2, left, mid, k);
    }
    else {
       return query(node * 2 + 1, mid + 1, right, k - tree[node * 2]);
    }
}

int main(){
    int N;
    cin >> N;
    long long nums[N];
    int remove[N];
    
    for (int i = 0; i < N; i++){
        cin >> nums[i];
    }

    for (int i = 0; i < N; i++){
        cin >> remove[i];
    }

    build(1, 0, N - 1);
    for (int i = 0; i < N; i++){
        int pos = remove[i];
        int idx = query(1, 0, N - 1, pos);
        cout << nums[idx] << " ";
        update(1, 0, N - 1, idx);
    }
    return 0;
}
