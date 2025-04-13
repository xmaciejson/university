#include <iostream>
using namespace std;

int const n = 800000;
long long tree[4 * n];

void build(long long nums[], int node, int left, int right){
    if (left == right){
        tree[node] = nums[left];
        return;
    }
    int mid = (left + right) / 2;
    build(nums, node * 2, left, mid);
    build(nums, node * 2 + 1, mid + 1, right);
    tree[node] = max(tree[node * 2], tree[node * 2 + 1]);
}

void update(int idx, int val, int node, int left, int right){
    if (left == right){
        tree[node] -= val;
        return;
    }
    int mid = (left + right) / 2;
    if (idx <= mid){
        update(idx, val, node * 2, left, mid);
    }
    else {
        update(idx, val, node * 2 + 1, mid + 1, right);
    }
    tree[node] = max(tree[node*2], tree[node*2+1]);
}

int find_hotel(int g, int node, int left, int right){
    if (tree[node] < g) return -1;
    if (left == right) return left;

    int mid = (left + right) / 2;
    if (tree[node * 2] >= g){
        return find_hotel(g, node * 2, left, mid);
    }else{
        return find_hotel(g, node * 2 + 1, mid + 1, right);
    }
}

int main(){
    int N, Q;
    cin >> N >> Q;
    long long hotels[N];
    int groups[Q];
    for (int i = 0; i < N; i++){
        cin >> hotels[i];
    }

    for (int i = 0; i < Q; i++){
        cin >> groups[i];
    }
    build(hotels, 1, 0, N - 1);
    for (int i = 0; i < Q; i++){
        int res = find_hotel(groups[i], 1, 0, N - 1);
        if (res != -1){
            update(res, groups[i], 1, 0, N - 1);
            cout << res + 1 << " ";
        }
        else{
            cout << 0 << " ";
        }
        
    }
    return 0;
}