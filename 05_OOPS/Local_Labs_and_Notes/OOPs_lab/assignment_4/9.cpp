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

// Function accepting a pointer to constant student
void displayStudent(const Student* s) {
    cout << "=== Student Attributes (Read via const Student*) ===" << endl;
    cout << "Roll No : " << s->rollno << endl;
    cout << "Name    : " << s->name << endl;
    cout << "Age     : " << s->age << endl;
    cout << "Marks   : " << s->marks << endl;
    cout << "Grade   : " << s->grade << endl;

    // Demonstration that data cannot be modified through the pointer:
    // s->marks = 99.0f; // COMPILE ERROR: assignment of member in read-only object
}

int main() {
    Student s(105, "Meera", 19, 93.5f, 'A');

    displayStudent(&s);

    cout << "\nDemonstration: Inside displayStudent(), any attempt to modify data" << endl;
    cout << "such as (s->marks = 99.0f) produces a compile-time error." << endl;

    return 0;
}
