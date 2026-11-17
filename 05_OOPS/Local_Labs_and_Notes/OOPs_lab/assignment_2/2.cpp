#include <iostream>
using namespace std;

// Inline function to check if a number is even
inline bool isEven(int n) {
    return (n % 2 == 0);
}

// Inline function to check if a number is positive
inline bool isPositive(int n) {
    return (n > 0);
}

// In a comment above your palindrome function, note whether it still makes sense to mark it inline, given that it needs a loop, and why:
// Although this function is marked with the 'inline' keyword, it contains a while loop.
// Functions containing loops or complex control structures are generally poor candidates
// for inlining because the execution time of the loop far exceeds the minor overhead of a
// function call. Furthermore, inlining duplicates the entire loop body at every call site,
// potentially leading to code bloat and cache penalties. In practice, modern C++ compilers
// will usually treat 'inline' only as a suggestion and decline to inline loop-heavy functions.
inline bool isPalindrome(int num) {
    if (num < 0) return false;
    int original = num, rev = 0;
    while (num > 0) {
        rev = rev * 10 + (num % 10);
        num = num / 10;
    }
    return original == rev;
}

int main() {
    cout << "=== Checking Even / Odd ===" << endl;
    cout << "Is 4 even? " << (isEven(4) ? "Yes" : "No") << endl;
    cout << "Is 7 even? " << (isEven(7) ? "Yes" : "No") << endl;

    cout << "\n=== Checking Positive / Non-Positive ===" << endl;
    cout << "Is 15 positive? " << (isPositive(15) ? "Yes" : "No") << endl;
    cout << "Is -8 positive? " << (isPositive(-8) ? "Yes" : "No") << endl;

    cout << "\n=== Checking Palindrome ===" << endl;
    cout << "Is 121 a palindrome? " << (isPalindrome(121) ? "Yes" : "No") << endl;
    cout << "Is 123 a palindrome? " << (isPalindrome(123) ? "Yes" : "No") << endl;

    return 0;
}
