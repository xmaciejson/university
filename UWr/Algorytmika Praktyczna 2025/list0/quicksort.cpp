#include <iostream>
using namespace std;

void swap(int &a, int &b) { 
    int temp = a;
    a = b;
    b = temp;
}

void quicksort(int *tab, int lewy, int prawy) {
    if (prawy <= lewy)
        return;

    int i = lewy - 1, j = prawy + 1;
    int pivot = tab[(lewy + prawy) / 2];

    while (true) { 
        do {
            i++;
        } while (tab[i] < pivot);

        do {
            j--;
        } while (tab[j] > pivot);

        if (i >= j)
            break;

        swap(tab[i], tab[j]); 
    }

    
    quicksort(tab, lewy, j);
    quicksort(tab, j + 1, prawy);
}

int main() {
    int n;
    cin >> n;

    int *tab = new int[n]; 

    for (int i = 0; i < n; i++) {
        cin >> tab[i];
    }

    quicksort(tab, 0, n - 1);

    for (int j = 0; j < n; j++) {
        cout << tab[j] << " ";
    }

    delete[] tab; 

    return 0;
}
