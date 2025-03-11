#include <iostream>
using namespace std;

int zlicz(int a){
    if (a == 0) return 0;

    int counter = 0;
    for (int i=1; i*i<=a; i++){
        if (a % i == 0){
            counter++;
            if (i != a/i) counter++;
        }

    }
    return counter;
}

int main(){
    int n, x;
    cin >> n;
    for (int i=0; i<n; i++){
        cin >> x;
        cout << zlicz(x) << endl;
    }
    return 0;
}