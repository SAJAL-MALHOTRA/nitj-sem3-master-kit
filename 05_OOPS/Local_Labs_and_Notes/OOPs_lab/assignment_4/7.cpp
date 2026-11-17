#include <iostream>
#include <string>
using namespace std;

class Student {
public:
    int rollno;
    string name;
    float marks;
    char grade;

    Student(int r, string n, float m, char g) : rollno(r), name(n), marks(m), grade(g) {}
};

int main() {
    Student s1(101, "Aman", 80.0f, 'B');
    Student s2(102, "Kavya", 92.0f, 'A');

    // Constant pointer to Student object (address stored cannot be changed)
    Student* const ptr = &s1;

    cout << "=== Initial Details of s1 ===" << endl;
    cout << "Name: " << ptr->name << ", Marks: " << ptr->marks << ", Grade: " << ptr->grade << endl;

    // Modifying data through the constant pointer is ALLOWED
    ptr->marks = 88.0f;
    ptr->grade = 'A';

    cout << "\n=== Modified Details of s1 via Constant Pointer ===" << endl;
    cout << "Name: " << ptr->name << ", Marks: " << ptr->marks << ", Grade: " << ptr->grade << endl;

    // Attempting to redirect the pointer to s2 is NOT ALLOWED:
    // ptr = &s2; // COMPILE ERROR: assignment of read-only variable 'ptr'
    cout << "\nDemonstration: ptr = &s2 fails at compile time because 'ptr' is a constant pointer." << endl;

    return 0;
}
