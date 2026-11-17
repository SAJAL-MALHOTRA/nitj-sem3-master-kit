# OOP Lab Assignment 2: Inline Functions

### 1. Write a program with three small inline functions: one that computes the square of a number, one that computes the cube of a number, and one that computes the area of a circle given its radius. Call each function with at least 3 different inputs and display the results.

**Ans -**

```cpp
#include <iostream>
using namespace std;

// Inline function to calculate square of a number
inline double square(double n) {
    return n * n;
}

// Inline function to calculate cube of a number
inline double cube(double n) {
    return n * n * n;
}

// Inline function to calculate area of a circle
inline double areaCircle(double r) {
    return 3.14159 * r * r;
}

int main() {
    cout << "=== Square of Numbers ===" << endl;
    cout << "Square of 3: " << square(3) << endl;
    cout << "Square of 5: " << square(5) << endl;
    cout << "Square of 7.5: " << square(7.5) << endl;

    cout << "\n=== Cube of Numbers ===" << endl;
    cout << "Cube of 2: " << cube(2) << endl;
    cout << "Cube of 4: " << cube(4) << endl;
    cout << "Cube of 5: " << cube(5) << endl;

    cout << "\n=== Area of Circles ===" << endl;
    cout << "Area of circle with radius 2.5: " << areaCircle(2.5) << endl;
    cout << "Area of circle with radius 5.0: " << areaCircle(5.0) << endl;
    cout << "Area of circle with radius 7.0: " << areaCircle(7.0) << endl;

    return 0;
}
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_2\" ; if ($?) { g++ 1.cpp -o 1 } ; if ($?) { .\1 }
=== Square of Numbers ===
Square of 3: 9
Square of 5: 25
Square of 7.5: 56.25

=== Cube of Numbers ===
Cube of 2: 8
Cube of 4: 64
Cube of 5: 125

=== Area of Circles ===
Area of circle with radius 2.5: 19.6349
Area of circle with radius 5.0: 78.5397
Area of circle with radius 7.0: 153.938
```

---

### 2. Write three inline functions, each returning a boolean result: one that checks if a number is even, one that checks if a number is positive, and one that checks if a number is a palindrome. Test each with at least one true case and one false case, printing "Yes"/"No" based on the result.
In a comment above your palindrome function, note whether it still makes sense to mark it inline, given that it needs a loop, and why.

**Ans -**

```cpp
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
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_2\" ; if ($?) { g++ 2.cpp -o 2 } ; if ($?) { .\2 }
=== Checking Even / Odd ===
Is 4 even? Yes
Is 7 even? No

=== Checking Positive / Non-Positive ===
Is 15 positive? Yes
Is -8 positive? No

=== Checking Palindrome ===
Is 121 a palindrome? Yes
Is 123 a palindrome? No
```

---

### 3. Write inline functions to find the maximum and minimum of two numbers. Then write a third inline function that finds the maximum of three numbers — it should internally reuse your two-number maximum function.

**Ans -**

```cpp
#include <iostream>
using namespace std;

// Inline function to find the maximum of two numbers
inline int maxTwo(int a, int b) {
    return (a > b) ? a : b;
}

// Inline function to find the minimum of two numbers
inline int minTwo(int a, int b) {
    return (a < b) ? a : b;
}

// Inline function to find the maximum of three numbers
// Internally reuses the two-number maximum function
inline int maxThree(int a, int b, int c) {
    return maxTwo(maxTwo(a, b), c);
}

int main() {
    int x = 25, y = 40, z = 35;

    cout << "Numbers: " << x << ", " << y << ", " << z << endl;
    cout << "Maximum of (" << x << ", " << y << "): " << maxTwo(x, y) << endl;
    cout << "Minimum of (" << x << ", " << y << "): " << minTwo(x, y) << endl;
    cout << "Maximum of (" << x << ", " << y << ", " << z << "): " << maxThree(x, y, z) << endl;

    return 0;
}
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_2\" ; if ($?) { g++ 3.cpp -o 3 } ; if ($?) { .\3 }
Numbers: 25, 40, 35
Maximum of (25, 40): 40
Minimum of (25, 40): 25
Maximum of (25, 40, 35): 40
```

---

### 4. Write an inline function that attempts to swap two integers using a temporary variable, printing the swapped values inside the function. Call it from main() with two variables, printing them before and after the call.
In a comment, explain why the original variables in `main()` do or do not change.

**Ans -**

```cpp
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
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_2\" ; if ($?) { g++ 4.cpp -o 4 } ; if ($?) { .\4 }
Before function call: num1 = 10, num2 = 20
Inside swapNumbers: a = 20, b = 10
After function call:  num1 = 10, num2 = 20
```

---

### 5. Write an inline function to calculate the factorial of a number using a loop (not recursion). Test it for two different values.
In a comment, discuss whether this function is really a good candidate for the `inline` keyword — consider how the loop's length depends on the input, and what happens if it's called many times with a large input.

**Ans -**

```cpp
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
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_2\" ; if ($?) { g++ 5.cpp -o 5 } ; if ($?) { .\5 }
Factorial of 5 = 120
Factorial of 8 = 40320
```

---

### 6. Take your prime-number-checking logic from Lab 1 and rewrite it as an inline function that returns a Boolean. Use it inside a loop to print all prime numbers between 1 and 50.
In a comment, discuss whether this remains a good use of `inline`, given how often the loop calls it.

**Ans -**

```cpp
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
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_2\" ; if ($?) { g++ 6.cpp -o 6 } ; if ($?) { .\6 }
Prime numbers between 1 and 50 are:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 
```
