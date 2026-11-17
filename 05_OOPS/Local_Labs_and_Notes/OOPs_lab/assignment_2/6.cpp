#include <iostream>
using namespace std;

// In a comment, discuss whether this remains a good use of `inline`, given how often the loop calls it:
// Although isPrime is called frequently inside the loop (50 times here), it remains a poor use of 'inline'.
// The function contains an internal loop whose execution time (O(sqrt(n))) far exceeds the tiny function
// call overhead. Inlining a loop-containing function inside another outer loop increases code bloat and
// strains instruction cache memory without providing measurable performance gains.
// Modern compilers typically ignore the inline hint for loop-containing functions.
inline bool isPrime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int main() {
    cout << "Prime numbers between 1 and 50 are:" << endl;
    for (int i = 1; i <= 50; i++) {
        if (isPrime(i)) {
            cout << i << " ";
        }
    }
    cout << endl;

    return 0;
}
