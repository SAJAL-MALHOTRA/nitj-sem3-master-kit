#include <iostream>
#include <string>
using namespace std;

class Student {
public:
    int rollno;
    string name;
    float marks;
    char grade;

    Student(int r, string n, float m, char g) 
        : rollno(r), name(n), marks(m), grade(g) {}
};

int main() {
    // 1. Create student object
    Student s(110, "Siddharth", 76.0f, 'C');

    // 2. Create pointer to the object
    Student* ptr = &s;

    // 3. Create pointer to pointer
    Student** pptr = &ptr;

    cout << "=== Initial Student Details ===" << endl;
    cout << "Name  : " << (*pptr)->name << endl;
    cout << "Marks : " << (*pptr)->marks << endl;
    cout << "Grade : " << (*pptr)->grade << endl;

    // Modifying student marks and grade using pointer to pointer (**pptr)
    (*pptr)->marks = 89.5f;
    (*pptr)->grade = 'A';

    cout << "\n=== Updated Student Details (Modified via Student** pptr) ===" << endl;
    cout << "Name          : " << (*pptr)->name << endl;
    cout << "Updated Marks : " << (*pptr)->marks << endl;
    cout << "Updated Grade : " << (*pptr)->grade << endl;

    return 0;
}
