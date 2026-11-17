#include <iostream>
#include <string>
using namespace std;

class Student {
public:
    string name;
    float marks;

    Student() : name(""), marks(0.0f) {}
    Student(string n, float m) : name(n), marks(m) {}
};

/*
What does 2 x 3 mean?
It means the array has: 2 rows, 3 students in each row, making a total of 2 * 3 = 6 students.
*/

int main() {
    // 2 x 3 array of student objects
    Student students[2][3] = {
        { Student("Aarav", 85.0f), Student("Bhavya", 90.0f), Student("Chetan", 75.0f) },
        { Student("Divya", 92.0f), Student("Esha", 88.0f),   Student("Farhan", 81.0f) }
    };

    // Pointer to an array of 3 students
    Student (*ptr)[3] = students;

    cout << "=== 2 x 3 Student Matrix Traversal ===" << endl;
    for (int i = 0; i < 2; i++) {
        float rowTotal = 0.0f;
        cout << "\nRow " << (i + 1) << " Students:" << endl;
        for (int j = 0; j < 3; j++) {
            // Accessing elements using pointer arithmetic
            Student s = *(*(ptr + i) + j);
            cout << "  Student " << (j + 1) << ": " << s.name << " (Marks: " << s.marks << ")" << endl;
            rowTotal += s.marks;
        }
        cout << "Total Marks for Row " << (i + 1) << " = " << rowTotal << endl;
    }

    return 0;
}
