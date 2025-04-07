#include <iostream>
#include <vector>
using namespace std;

int const n = 800000;
vector<long long> tree(n);

void build(vector<long long>& nums, int v, int left, int right){
    if (left == right){
        tree[v] = nums[left];
    }
    else{
       int mid = (left + right) / 2;
       build(nums, v*2, left, mid);
       build(nums, v*2+1, mid + 1, right);
       tree[v] = max(tree[v * 2], tree[v * 2 + 1]);
    }
}

int getMax(int a, int b, int left, int right, int v){
    if (a > b){
        return -INT_MAX;
    }
    if (left <= a && b <= right){
        return tree[v];
    }
    int mid = (left + right) / 2;
    return max(getMax(a, b, left, mid, v * 2), getMax(a, b, mid + 1, right, v * 2 + 1));
}


int main(){
    int N, Q;
    cin >> N >> Q;
    vector<long long> nums(N);
    for (int i=0; i<N; i++){
        cin >> nums[i];
    }

    build(nums, 1, 0, N - 1);
    while(Q--){
        int a, b, z;
        cin >> z >> a >> b;
        a--, b--;
        if (z == 1){
            nums[b] = a;
        }
        else{
            cout << getMax(a, b, 0, N - 1, 1);
        }
    }
    return 0;
}