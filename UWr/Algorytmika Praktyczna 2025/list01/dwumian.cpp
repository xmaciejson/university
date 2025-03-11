#include <iostream>
using namespace std;

int silnia(int x){
    long long temp = 1;
    for (int i=1; i<=x; i++){
        temp *= i;
    }
    return temp;
}

int dwumian(int a, int b){
    if (a == 0 || b == 0) return 1;

    if (b > a) return 0;

    long long modulo = 10000000007;
    int silnia_A = silnia(a);
    int silnia_B = silnia(b);
    int dwumian = silnia_A/(silnia_B * silnia(a-b));
    return dwumian % modulo;
}

int main(){
    int a, b, n;
    cin >> n;
    for (int j=0; j<n; j++){
        cin >> a >> b;
        cout << dwumian(a, b) << endl;
    }
    return 0;
}