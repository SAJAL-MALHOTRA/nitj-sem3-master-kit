#include <iostream>
using namespace std;

int main() {
    int num = 25;
    int* ptr = &num;

    cout << "=== Variable and Pointer Exploration ===" << endl;
    // 1. Value of variable directly
    cout << "1. Value of num directly          : " << num << endl;

    // 2. Value through pointer using dereference operator (*)
    cout << "2. Value through pointer (*ptr)   : " << *ptr << endl;

    // 3. Address stored in pointer
    cout << "3. Address stored in pointer (ptr): " << ptr << endl;

    return 0;
}
