#include <iostream>
#include <string>
using namespace std;

class Student {
public:
    int rollno;
    string name;
    int age;
    float marks;
    char grade;

    Student(int r, string n, int a, float m, char g) 
        : rollno(r), name(n), age(a), marks(m), grade(g) {}
};

int main() {
    Student s1(101, "Pooja", 20, 89.0f, 'A');
    Student s2(102, "Rohit", 22, 75.0f, 'B');

    // Constant pointer to constant student data
    const Student* const ptr = &s1;

    cout << "=== Displaying All 5 Attributes via const Student* const ptr ===" << endl;
    cout << "Roll No : " << ptr->rollno << endl;
    cout << "Name    : " << ptr->name << endl;
    cout << "Age     : " << ptr->age << endl;
    cout << "Marks   : " << ptr->marks << endl;
    cout << "Grade   : " << ptr->grade << endl;

    // Demonstration of restrictions:
    // 1. Cannot modify student data:
    // ptr->marks = 95.0f; // COMPILE ERROR: assignment of member 'Student::marks' in read-only object
    
    // 2. Cannot redirect pointer address:
    // ptr = &s2;          // COMPILE ERROR: assignment of read-only variable 'ptr'

    cout << "\nDemonstration: Both student data modification (ptr->marks = 95.0) and" << endl;
    cout << "pointer redirection (ptr = &s2) are rejected by the compiler." << endl;

    return 0;
}
