#include <iostream>
using namespace std;

int main() {
    int arr[5] = {10, 20, 30, 40, 50};
    int* ptr = arr;

    cout << "=== Original Array ===" << endl;
    for (int i = 0; i < 5; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    // Moving pointer to the 3rd element (index 2) using pointer arithmetic
    ptr = ptr + 2;

    // Dereferencing and assigning a new value
    *ptr = 999;

    cout << "\n=== Array After Modifying 3rd Element via Pointer ===" << endl;
    for (int i = 0; i < 5; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}
