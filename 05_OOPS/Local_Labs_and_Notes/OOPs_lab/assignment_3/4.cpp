#include <iostream>
using namespace std;

// Global variable
int count = 100;

void showVariables() {
    // Local variable with the exact same name
    int count = 25;

    // Access local variable directly, access global variable using scope resolution (::)
    cout << "Inside showVariables():" << endl;
    cout << "Local variable count  = " << count << endl;
    cout << "Global variable ::count = " << ::count << endl;
}

int main() {
    cout << "Before calling function, Global count = " << count << endl;
    showVariables();
    cout << "After calling function, Global count  = " << count << endl;

    return 0;
}
