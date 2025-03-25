#include <iostream>
using namespace std;

int const maxN = 200001;
int const logN = 18;
int log_tab[maxN];
int sparse_table[maxN][logN];

void buildTable(long long nums[], int len){    
    for (int i=0; i < len; i++){ //przedzialy 1-elementowe
        sparse_table[i][0] = nums[i];
    }

    for (int j = 1; (1 << j) <= len; j++){
        for (int i = 0; i + (1 << j) <= len; i++){
            sparse_table[i][j] = min(sparse_table[i][j - 1], sparse_table[i + (1 << (j - 1))][j - 1]);
        }
    }
}

void buildLogTab(int N){
    log_tab[1] = 0;
    for (int l = 2; l <= N; l++){
        log_tab[l] = log_tab[l / 2] + 1;
    }
    
}


int findMin(int left, int right){
    int x = log_tab[right - left + 1];
    return min(sparse_table[left][x], sparse_table[right - (1 << x) + 1][x]);
}

int main(){
    int N, Q;
    cin >> N >> Q;
    long long nums[N];
    for (int i=0; i<N; i++){
        cin >> nums[i];
    }
    
    buildTable(nums, N);
    buildLogTab(N);
    

    while (Q--){
        int a, b;
        cin >> a >> b;
        a--, b--;
        cout << findMin(a, b) << endl;

    }
    return 0;
}