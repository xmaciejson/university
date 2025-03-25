#include <iostream>
#include <vector>
using namespace std;

int const n = 800000;
long long tree[n];

void build(long long nums[], int v, int left, int right){
    if (left == right){
        tree[v] = nums[left];
    } else {
        int mid = (left + right) / 2;
        build(nums, v*2, left, mid);
        build(nums, v*2+1, mid + 1, right);
        tree[v] = min(tree[v*2], tree[v*2 + 1]);
    }
}

int get_min(int v, int left, int right, int a, int b){
    if (a > b){
        return 10000000000;
    }
    if (a <= left && right <= b){
        return tree[v];
    }

    int mid = (left + right) / 2;
    return min(get_min(v*2, left, mid, a, min(b, mid)), 
    get_min(v*2+1, mid+1, right, max(a, mid+1), b));
 
}   

int main(){
    int N, Q;
    cin >> N >> Q;
    long long nums[N];
    for (int i=0; i<N; i++){
        cin >> nums[i];
    }
    build(nums, 1, 0, N - 1);

    while(Q--){
        int a, b;
        cin >> a >> b;
        a--, b--;
        cout << get_min(1, 0, N - 1, a, b) << endl;
    }
    return 0;
}