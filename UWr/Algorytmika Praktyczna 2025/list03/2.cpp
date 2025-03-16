#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

const int MAX_N = 200000;
const int SQRT_MAX = 450; 
long long precomputed[MAX_N][SQRT_MAX];

int main() {
    
    int N, Q;
    cin >> N;
    vector<int> nums(N);

    for (int i = 0; i < N; i++) {
        cin >> nums[i];
    }

    int sqrtN = sqrt(N);

   //jezeli b jest mniejsze niz sqrt(n) to obliczamy wartosci
    for (int b = 1; b <= sqrtN; b++) {
        for (int a = N - 1; a >= 0; a--) {
            if (a + b < N) {
                precomputed[a][b] = nums[a] + precomputed[a + b][b];
            } else {
                precomputed[a][b] = nums[a];
            }
        }
    }

    cin >> Q;
    while (Q--) {
        int a, b;
        cin >> a >> b;
        a--; //zeby indeksy sie zgadzaly

        long long total = 0;
        if (b <= sqrtN) {
            total = precomputed[a][b];
        } else {
            while (a < N) {
                total += nums[a];
                a += b;
            }
        }

        cout << total << endl;
    }

    return 0;
}
