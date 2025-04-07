#include <iostream>
using namespace std;

int const n = 1000000;
int tree[4 * n];

void update(int node, int left, int right, int idx){
    if (left == right){
        tree[node]++;
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

int inversion(int node, int left, int right, int l, int r){
    if (right < l || left > r){
        return 0;
    }
    if (l <= left && r >= right){
        return tree[node];
    }
    int mid = (left + right) / 2;
    return inversion(node * 2, left, mid, l, r) + inversion(node * 2 + 1, mid + 1, right, l, r);

}

int main(){
    int N;
    cin >> N;
    int nums[N];
    for (int i = 0; i < N; i++){
        cin >> nums[i];
    }

    long long inv = 0;
    for (int i = N - 1; i >= 0; i--){
        inv += inversion(1, 0, n, 0, nums[i] - 1);
        update(1, 0, n, nums[i]);
    }
    cout << inv << "\n";
    return 0;

}