#include <iostream>
using namespace std;

class Calculator {
public:
    // Overloaded add functions
    int add(int a, int b) {
        return a + b;
    }
    double add(double a, double b) {
        return a + b;
    }

    // Overloaded subtract functions
    int subtract(int a, int b) {
        return a - b;
    }
    double subtract(double a, double b) {
        return a - b;
    }

    // Overloaded multiply functions
    int multiply(int a, int b) {
        return a * b;
    }
    double multiply(double a, double b) {
        return a * b;
    }

    // Overloaded divide functions
    double divide(int a, int b) {
        if (b == 0) {
            cout << "Error: Division by zero!" << endl;
            return 0;
        }
        return (double)a / b;
    }
    double divide(double a, double b) {
        if (b == 0.0) {
            cout << "Error: Division by zero!" << endl;
            return 0;
        }
        return a / b;
    }
};

int main() {
    Calculator calc;

    cout << "=== Integer Operations ===" << endl;
    cout << "Add (10, 5)       = " << calc.add(10, 5) << endl;
    cout << "Subtract (10, 5)  = " << calc.subtract(10, 5) << endl;
    cout << "Multiply (10, 5)  = " << calc.multiply(10, 5) << endl;
    cout << "Divide (10, 5)    = " << calc.divide(10, 5) << endl;

    cout << "\n=== Decimal Operations ===" << endl;
    cout << "Add (12.5, 3.5)      = " << calc.add(12.5, 3.5) << endl;
    cout << "Subtract (12.5, 3.5) = " << calc.subtract(12.5, 3.5) << endl;
    cout << "Multiply (12.5, 3.5) = " << calc.multiply(12.5, 3.5) << endl;
    cout << "Divide (12.5, 2.5)   = " << calc.divide(12.5, 2.5) << endl;

    return 0;
}
