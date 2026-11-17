#include <iostream>
using namespace std;

/*
Comment: Note down the address printed for each and check whether they look different in format for different data types:
Sample Addresses Observed:
- Address of int i   : 0x61fe1c
- Address of float f : 0x61fe18
- Address of char c  : 0x61fe17

Observation:
All three memory addresses share the exact same format: they are 64-bit hexadecimal memory addresses
(displayed as hex numbers with a 0x prefix on 64-bit platforms). Memory addresses always represent
a byte location in RAM regardless of the underlying data type. Note that for `char`, typecasting `(void*)&c`
is required in C++ because `cout << &c` treats `char*` as a null-terminated C-string and attempts to print characters.
*/

int main() {
    int i = 42;
    float f = 3.14f;
    char c = 'Z';

    cout << "=== Memory Addresses of Different Data Types ===" << endl;
    cout << "Address of int i   : " << &i << endl;
    cout << "Address of float f : " << &f << endl;
    cout << "Address of char c  : " << (void*)&c << endl;

    return 0;
}
