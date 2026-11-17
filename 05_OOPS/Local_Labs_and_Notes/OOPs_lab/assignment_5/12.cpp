#include <iostream>
#include <string>
using namespace std;

class Student {
private:
    string name;
    double marks;

public:
    void setDetails(string n, double m) {
        name = n;
        marks = m;
    }

    string getName() const { return name; }
    double getMarks() const { return marks; }

    // Friend function to compare two Student objects
    friend Student getTopStudent(Student s1, Student s2);
};

// Friend function definition
Student getTopStudent(Student s1, Student s2) {
    if (s1.marks >= s2.marks) {
        return s1;
    } else {
        return s2;
    }
}

int main() {
    Student s1, s2;
    s1.setDetails("Aman", 88.5);
    s2.setDetails("Riya", 94.0);

    // Creating pointer to Student object
    Student* sptr = &s1;

    cout << "=== Accessing Student Data via Pointer and Arrow Operator (->) ===" << endl;
    cout << "Student 1 Name  : " << sptr->getName() << endl;
    cout << "Student 1 Marks : " << sptr->getMarks() << endl;

    // Passing the pointed-to object (*sptr) into friend comparison function
    Student topper = getTopStudent(*sptr, s2);

    cout << "\n=== Top Student (Determined via Friend Function) ===" << endl;
    cout << "Name  : " << topper.getName() << endl;
    cout << "Marks : " << topper.getMarks() << endl;

    return 0;
}
