#include <iostream>
using namespace std;

// Struct definition
struct StudentStruct {
    int id;
    float marks;
};

// Class definition
class StudentClass {
    int id;
    float marks;
};

/*
In a comment, explain what happened when you tried this on the class version,
and why the struct version behaved differently:

Observation & Explanation:
- In C++, the only fundamental difference between a `struct` and a `class` is their default access specifier.
- For `struct`, members are PUBLIC by default. Therefore, accessing `s.id` and `s.marks` directly
  using the dot operator succeeds without any compilation errors.
- For `class`, members are PRIVATE by default. Attempting to access `c.id` or `c.marks` directly
  from main() results in a compile-time error:
  "error: 'int StudentClass::id' is private within this context".
- To make the program compile cleanly, the direct access to class private members is commented out below,
  demonstrating the access restriction.
*/

int main() {
    // 1. Accessing struct members directly:
    StudentStruct s;
    s.id = 101;
    s.marks = 88.5f;
    cout << "Struct members accessed directly (default public):" << endl;
    cout << "s.id = " << s.id << ", s.marks = " << s.marks << endl;

    // 2. Trying to access class members directly:
    StudentClass c;
    // c.id = 102;      // COMPILE ERROR: 'id' is private in StudentClass
    // c.marks = 92.0f; // COMPILE ERROR: 'marks' is private in StudentClass
    cout << "\nClass members cannot be accessed directly because they are private by default." << endl;
    cout << "(Attempting c.id = 102 generates a compile error)." << endl;

    return 0;
}
