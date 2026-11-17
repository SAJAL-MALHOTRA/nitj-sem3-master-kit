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
        Student(102, "Bob", 78.0f),
        Student(103, "Charlie", 74.0f),
        Student(104, "Diana", 89.5f),
        Student(105, "Ethan", 91.0f)
    };

    Student* ptr = students;

    cout << "=== Displaying Using Array Notation (arr[i]) ===" << endl;
    for (int i = 0; i < 5; i++) {
        cout << "Roll: " << students[i].rollno << ", Name: " << students[i].name 
             << ", Marks: " << students[i].marks << endl;
    }

    cout << "\n=== Displaying Using Pointer Notation (*(ptr + i)) ===" << endl;
    for (int i = 0; i < 5; i++) {
        cout << "Roll: " << (*(ptr + i)).rollno << ", Name: " << (*(ptr + i)).name 
             << ", Marks: " << (*(ptr + i)).marks << endl;
    }

    // Modifying the marks of the 2nd student (Bob, index 1) using pointer
    cout << "\nModifying marks of Bob (index 1) via pointer from " << (ptr + 1)->marks << " to 95.0..." << endl;
    (ptr + 1)->marks = 95.0f;

    cout << "\n=== Updated Student Details (Bob) ===" << endl;
    cout << "Roll: " << (ptr + 1)->rollno 
         << " | Name: " << (ptr + 1)->name 
         << " | Updated Marks: " << (ptr + 1)->marks << endl;

    return 0;
}
