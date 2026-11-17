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
