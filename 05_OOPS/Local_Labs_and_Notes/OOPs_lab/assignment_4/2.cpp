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

    Student(int r, string n, int a, float m, char g) {
        rollno = r;
        name = n;
        age = a;
        marks = m;
        grade = g;
    }

    void display() {
        cout << "Roll No : " << rollno << endl;
        cout << "Name    : " << name << endl;
        cout << "Age     : " << age << endl;
        cout << "Marks   : " << marks << endl;
        cout << "Grade   : " << grade << endl;
    }
};

int main() {
    Student s(102, "Rohan", 21, 91.0f, 'A');

    // Initializing pointer to nullptr
    Student* ptr = nullptr;

    // Checking the pointer before accessing
    cout << "=== Checking Null Pointer ===" << endl;
    if (ptr == nullptr) {
        cout << "Pointer is currently NULL (nullptr). Cannot access object safely." << endl;
    }

    // Assigning object address to the pointer
    ptr = &s;
    cout << "\nPointer assigned to student object address." << endl;

    if (ptr != nullptr) {
        cout << "\n=== Accessing Student Details via '->' Operator ===" << endl;
        ptr->display();
    }

    return 0;
}
