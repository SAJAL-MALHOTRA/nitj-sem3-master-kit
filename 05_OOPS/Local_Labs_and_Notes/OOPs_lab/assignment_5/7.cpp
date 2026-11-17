#include <iostream>
using namespace std;

/*
Comment: Record how many bytes the address moved, and explain what have you observed:
Recorded Address Shifts:
- int pointer   : moved by 4 bytes (sizeof(int)   = 4)
- float pointer : moved by 4 bytes (sizeof(float) = 4)
- char pointer  : moved by 1 byte  (sizeof(char)  = 1)

Observation:
When a pointer of type `T*` is incremented by 1 (ptr++), the compiler scales the memory address
by `sizeof(T)` bytes. Pointer arithmetic operates in terms of element offsets, ensuring that incrementing
a pointer cleanly steps to the next contiguous element in memory regardless of data type.
*/

int main() {
    int   iarr[3] = {10, 20, 30};
    float farr[3] = {1.5f, 2.5f, 3.5f};
    char  carr[3] = {'X', 'Y', 'Z'};

    int*   ip = iarr;
    float* fp = farr;
    char*  cp = carr;

    cout << "=== Pointer Increment Across Different Data Types ===" << endl;

    cout << "int pointer   : " << ip;
    ip++;
    cout << " -> " << ip << " (moved by " << sizeof(int) << " bytes)" << endl;

    cout << "float pointer : " << fp;
    fp++;
    cout << " -> " << fp << " (moved by " << sizeof(float) << " bytes)" << endl;

    cout << "char pointer  : " << (void*)cp;
    cp++;
    cout << " -> " << (void*)cp << " (moved by " << sizeof(char) << " byte)" << endl;

    return 0;
}
