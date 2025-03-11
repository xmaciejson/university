#include <iostream>
#include <cmath>
using namespace std;

const long long MOD = 1000000000;

long long potega(long long a, long long n)
{
    long long wynik = 1;
    while (n > 0)
    {
        if (n % 2 == 1)
        {
            wynik = (wynik * a) % MOD;
        }
        a = (a * a) % MOD;
        n /= 2;
    }
    return wynik;
}

int main()
{
    long long A, N;
    cin >> A >> N;
    cout << potega(A, N);
    return 0;
}