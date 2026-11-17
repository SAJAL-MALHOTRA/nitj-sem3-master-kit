#include <iostream>
using namespace std;

/*
Comment:
1. Address Change:
   Incrementing the pointer increased the hexadecimal address by exactly 4 bytes (e.g. from 0x61fe14 to 0x61fe18).
   This matches sizeof(int) because pointer arithmetic in C++ advances addresses in units of the pointed-to type's size
   (new_address = old_address + 1 * sizeof(int)).

2. Safety of Dereferencing:
   Since 'x' is a standalone scalar integer and NOT part of an array, dereferencing `ptr` after incrementing
   (*ptr) is UNDEFINED BEHAVIOR and completely unsafe. It accesses arbitrary memory outside of the allocated
   variable 'x', which may lead to reading garbage values, data corruption, or segmentation faults.
*/

int main() {
    int x = 100;
    int* ptr = &x;

    cout << "=== Pointer Increment & Decrement ===" << endl;
    cout << "Original address stored in ptr       : " << ptr << endl;

    ptr++;
    cout << "After incrementing (ptr++)           : " << ptr << " (+ " << sizeof(int) << " bytes)" << endl;

    ptr--;
    cout << "After decrementing back (ptr--)      : " << ptr << endl;
    cout << "Dereferencing safe original value    : " << *ptr << endl;

    return 0;
}
