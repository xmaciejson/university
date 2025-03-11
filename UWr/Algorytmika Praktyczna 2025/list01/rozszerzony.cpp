#include <iostream>
using namespace std;

void euklides(int a, int b, int &x, int &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return;
    }
    int x1, y1;
    euklides(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
}

int main() {
    int n;
    cin >> n;
    
    for (int i = 0; i < n; i++) {
        int a, b, x, y;
        cin >> a >> b;
        euklides(a, b, x, y);
        cout << x << ' ' << y << ' ' << a * x + b * y << endl;
    }

    return 0;
}
