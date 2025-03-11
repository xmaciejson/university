#include <iostream>
using namespace std;

int wzglednie_pierwsza(int a){

    int counter = a;
    for (int i=2; i*i<=a; i++){
        if (a % i == 0){
            while (a % i == 0) a /= i;
            counter -= counter / i;
        }
    }
    if (a > 1) counter -= counter / a;
    return counter;
}

int main(){
    int n, x;
    cin >> n;
    for (int i=0; i<n; i++){
        cin >> x;
        cout << wzglednie_pierwsza(x) << endl;
    }
    return 0;
}