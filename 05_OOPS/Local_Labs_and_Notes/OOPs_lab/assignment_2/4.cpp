#include <iostream>
using namespace std;

// In a comment, explain why the original variables in `main()` do or do not change:
// The function swapNumbers uses pass-by-value. When arguments 'a' and 'b' are passed,
// the function creates local copies of their values on the stack/registers.
// The swapping logic only modifies these local copies. Even when the function is inlined,
// C++ preserves pass-by-value semantics by working on temporary variables rather than
// the caller's memory locations. Therefore, the original variables in main() do not change.
inline void swapNumbers(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
    cout << "Inside swapNumbers: a = " << a << ", b = " << b << endl;
}

int main() {
    int num1 = 10, num2 = 20;

    cout << "Before function call: num1 = " << num1 << ", num2 = " << num2 << endl;
    swapNumbers(num1, num2);
    cout << "After function call:  num1 = " << num1 << ", num2 = " << num2 << endl;

    return 0;
}
