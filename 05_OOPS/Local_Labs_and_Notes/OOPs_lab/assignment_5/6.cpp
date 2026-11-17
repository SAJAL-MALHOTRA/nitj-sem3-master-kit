#include <iostream>
using namespace std;

int main() {
    int arr[5] = {10, 20, 30, 40, 50};

    // Point to the last element of the array
    int* ptr = arr + 4;

    cout << "=== Reverse Array Traversal using Pointer Decrement ===" << endl;
    cout << "Elements in reverse: ";
    for (int i = 0; i < 5; i++) {
        cout << *ptr << " ";
        ptr--; // move backwards
    }
    cout << endl;

    return 0;
}
