#include <iostream>
using namespace std;

const int MOD = 1000000007;
const int MAX_N = 1000000;

long long silnia[MAX_N + 1], odwrotnosc_silni[MAX_N + 1];

// Szybkie potęgowanie (a^b mod m)
long long potegowanie_modulo(long long a, long long b, long long m) {
    long long wynik = 1;
    while (b > 0) {
        if (b % 2 == 1) wynik = (wynik * a) % m;
        a = (a * a) % m;
        b /= 2;
    }
    return wynik;
}

// Precompute silnie i odwrotności modulo MOD
void precompute() {
    silnia[0] = 1;
    for (int i = 1; i <= MAX_N; i++) {
        silnia[i] = (silnia[i - 1] * i) % MOD;
    }

    odwrotnosc_silni[MAX_N] = potegowanie_modulo(silnia[MAX_N], MOD - 2, MOD);
    for (int i = MAX_N - 1; i >= 0; i--) {
        odwrotnosc_silni[i] = (odwrotnosc_silni[i + 1] * (i + 1)) % MOD;
    }
}

// Dwumian Newtona (a nad b) % MOD
long long dwumian(int a, int b) {
    if (b > a || b < 0) return 0;
    return (silnia[a] * odwrotnosc_silni[b] % MOD) * odwrotnosc_silni[a - b] % MOD;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    precompute();

    int n, a, b;
    cin >> n;
    while (n--) {
        cin >> a >> b;
        cout << dwumian(a, b) << '\n';
    }

    return 0;
}
