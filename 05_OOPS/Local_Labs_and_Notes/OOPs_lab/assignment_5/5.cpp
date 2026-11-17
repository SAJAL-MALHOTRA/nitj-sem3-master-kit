#include <iostream>
using namespace std;

int main() {
    int arr[5] = {10, 20, 30, 40, 50};
    int* ptr = arr; // points to the first element

    cout << "=== Array Traversal using Pointer and Dereferencing ===" << endl;
    cout << "Elements: ";
    for (int i = 0; i < 5; i++) {
        cout << *ptr << " ";
        ptr++; // advance pointer to next element
    }
    cout << endl;

    return 0;
}
