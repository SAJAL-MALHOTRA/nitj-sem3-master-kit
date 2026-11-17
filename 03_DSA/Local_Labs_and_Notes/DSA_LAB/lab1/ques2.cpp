#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cout << "Enter number of elements: ";
    cin >> n;

    int arr[100]; //assuming a array of a big size

    cout << "Enter elements: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int position, element;

    cout << "Enter position: ";
    cin >> position;

    cout << "Enter element: ";
    cin >> element;

    if (position < 0 || position > n) {
        cout << "Invalid position";
    }
    else {
        for (int i = n; i > position; i--) {
            arr[i] = arr[i - 1];
        }

        arr[position] = element;
        n++;

        cout << "Array after insertion: ";

        for (int i = 0; i < n; i++) {
            cout << arr[i] << " ";
        }
    }

    return 0;
}