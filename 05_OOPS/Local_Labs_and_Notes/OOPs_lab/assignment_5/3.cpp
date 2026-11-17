#include <iostream>
using namespace std;

/*
Comment: Compare this to a reference variable, can a reference be reassigned
to point at a different variable the way a pointer can?

Comparison:
- A pointer is an independent variable that holds a memory address. Its stored address can be freely
  reassigned at any point during program execution to point to different variables (e.g., ptr = &b).
- In contrast, a reference is an immutable alias (an alternative name) bound to an existing variable upon
  initialization. A reference CANNOT be reseated/reassigned to refer to another variable.
  If you write `ref = b;`, it does not rebind the reference to 'b'; instead, it assigns the value of 'b'
  into the original variable that 'ref' is referencing.
*/

int main() {
    int num1 = 15;
    int num2 = 45;

    int* ptr = &num1;
    cout << "Pointer initially pointing to num1: *ptr = " << *ptr << endl;

    // Reassigning pointer to point to num2
    ptr = &num2;
    cout << "Pointer reassigned to num2        : *ptr = " << *ptr << endl;

    return 0;
}
