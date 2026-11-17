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
