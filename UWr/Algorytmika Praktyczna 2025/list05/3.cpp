#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int max_profit(vector<vector<int>> tab, int n){
    vector<int> workers(1 << n, -1);
    workers[0] = 0;

    for (int mask = 0; mask < (1 << n); mask++){
        int i = __builtin_popcount(mask);
        for (int j = 0; j < n; j++){
            if (!(mask & (1 << j))){
                int new_mask = mask | (1 << j); 
                workers[new_mask] = max(workers[new_mask], workers[mask] + tab[i][j]);
            }
        }   
    }
    return workers[(1 << n) - 1];
}

int main(){
    int N;
    cin >> N;
    vector<vector<int>> profit(N, vector<int>(N));
    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){
            cin >> profit[i][j];
        }
    }
    cout << max_profit(profit, N) << '\n';
}
