#include <iostream>
#include <string>
using namespace std;

class Student {
public:
    int rollno;
    string name;
    float marks;

    Student() : rollno(0), name(""), marks(0.0f) {}
    Student(int r, string n, float m) : rollno(r), name(n), marks(m) {}
};

int main() {
    Student students[5] = {
        Student(101, "Alice", 82.5f),
        Student(102, "Bob", 95.0f),
        Student(103, "Charlie", 74.0f),
        Student(104, "Diana", 89.5f),
        Student(105, "Ethan", 91.0f)
    };

    Student* ptr = students;
    Student* highest = ptr;

    cout << "=== Student List (Traversed using Pointer Arithmetic) ===" << endl;
    for (int i = 0; i < 5; i++) {
        cout << "Roll No: " << (ptr + i)->rollno 
             << " | Name: " << (ptr + i)->name 
             << " | Marks: " << (ptr + i)->marks << endl;

        if ((ptr + i)->marks > highest->marks) {
            highest = (ptr + i);
        }
    }

    cout << "\n=== Student with Highest Marks (Found without array indexing) ===" << endl;
    cout << "Roll No : " << highest->rollno << endl;
    cout << "Name    : " << highest->name << endl;
    cout << "Marks   : " << highest->marks << endl;

    return 0;
}
