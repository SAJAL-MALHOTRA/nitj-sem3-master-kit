#include <iostream>
using namespace std;

// In a comment, discuss whether this function is really a good candidate for the `inline` keyword:
// This function is NOT a good candidate for the 'inline' keyword.
// 1. The loop's length depends directly on input 'n'. As 'n' increases, the time spent executing
//    the loop dominates, rendering the minor savings of eliminating a function call insignificant.
// 2. If called many times with different/large inputs, inlining duplicates the entire loop body
//    at each call site, causing substantial binary code bloat and reducing CPU instruction cache efficiency.
// Compilers generally reject inlining requests for functions containing iterative loops.
inline long long factorial(int n) {
    if (n < 0) return 0;
    long long fact = 1;
    for (int i = 1; i <= n; i++) {
        fact *= i;
    }
    return fact;
}

int main() {
    int val1 = 5, val2 = 8;

    cout << "Factorial of " << val1 << " = " << factorial(val1) << endl;
    cout << "Factorial of " << val2 << " = " << factorial(val2) << endl;

    return 0;
}
