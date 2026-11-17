#include <bits/stdc++.h>
using namespace std;

inline int max(int num1, int num2) {
    if (num1 > num2) {
        return num1;
    }
    else {
        return num2;
    }
}

inline int min(int num1, int num2) {
    if (num1 < num2) {
        return num1;
    }
    else {
        return num2;
    }
}

// Reuseing the two number max() function
inline int max(int num1, int num2, int num3) {
    return max(max(num1, num2), num3);
}

int main() {
    cout << max(10, 20) << endl;
    cout << min(10, 20) << endl;
    cout << max(10, 20, 15) << endl;

    return 0;
}
#include <bits/stdc++.h>
using namespace std;

// Pass-by-value: num1 and num2 are copies of the original variables
// Therefore swapping them does not change the variables in main()
inline void swapNumbers(int num1, int num2) {
    int temp = num1;
    num1 = num2;
    num2 = temp;

    cout << "Inside function after swap: "<< num1 << " " << num2 << endl;
}

int main() {
    int a = 10, b = 20;

    cout << "Before function call: "
         << a << " " << b << endl;

    swapNumbers(a, b);

    // The original variables do not change because the function
    // received copies of a and b, not the original variables.
    cout << "After function call: "
         << a << " " << b << endl;

    return 0;
}