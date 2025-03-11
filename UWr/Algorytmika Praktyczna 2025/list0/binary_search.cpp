#include <iostream>
#include <vector>
using namespace std;

int binary_search(int n, int tab[], int szukana)
{
    int l = 0, p = n - 1;
    
    while (l <= p)
    {
        int mid = (l + p) / 2;

        if (tab[mid] == szukana)
        {
            return mid + 1;
        }
        else if (tab[mid] < szukana)
        {
            l = mid + 1;
        }
        else
        {
            p = mid - 1;
        }
    }
    return -1;
}

int main()
{
    long N, M;
    cin >> N;

    int* tablica = new int[N];

    for (int i = 0; i < N; i++)
    {
        cin >> tablica[i];
    }


    cin >> M;
    for (int j = 0; j < M; j++)
    {
        int zapytanie;
        cin >> zapytanie;
        cout << binary_search(N, tablica, zapytanie) << endl;
    }

    return 0;
}