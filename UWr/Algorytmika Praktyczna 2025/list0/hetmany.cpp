#include <iostream>
#include <cmath>
using namespace std;

bool czy_poprawne(int w, int k, int **tab, int n) {
    for (int i = 0; i < w; i++) {
        if (tab[i][k] == 1) {  // Sprawdzanie kolumny
            return false;
        }
        // Sprawdzanie przekątnych
        if (k - (w - i) >= 0 && tab[i][k - (w - i)] == 1) {
            return false;
        }
        if (k + (w - i) < n && tab[i][k + (w - i)] == 1) {
            return false;
        }
    }
    return true;
}

void hetmany(int **tab, int n, int w, int &counter) {
    if (w == n) {
        counter++;
        return;
    }

    for (int k = 0; k < n; k++) {
        if (czy_poprawne(w, k, tab, n)) {
            tab[w][k] = 1;
            hetmany(tab, n, w + 1, counter);
            tab[w][k] = 0;
        }
    }
}

int main() {
    int n;
    cin >> n;
    int **tab = new int *[n];

    for (int i = 0; i < n; i++) {
        tab[i] = new int[n]();
    }

    int counter = 0;
    hetmany(tab, n, 0, counter);
    cout << counter << endl;

    for (int i = 0; i < n; i++) {
        delete[] tab[i];
    }
    delete[] tab;

    return 0;
}
