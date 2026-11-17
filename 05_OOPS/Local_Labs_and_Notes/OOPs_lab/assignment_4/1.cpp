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
};

int main() {
    Student s(101, "Aarav", 20, 88.5f, 'A');

    // Using a void pointer to hold the address of the student object
    void* vptr = &s;

    // Typecasting void pointer to Student* to access and display age, marks, and grade
    cout << "=== Student Details via Void Pointer Typecasting ===" << endl;
    cout << "Age   : " << static_cast<Student*>(vptr)->age << endl;
    cout << "Marks : " << static_cast<Student*>(vptr)->marks << endl;
    cout << "Grade : " << static_cast<Student*>(vptr)->grade << endl;

    return 0;
}
