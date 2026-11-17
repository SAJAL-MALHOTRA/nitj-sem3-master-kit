#include <iostream>
#include <string>
using namespace std;

class Student {
private:
    string name;
    float marks;

public:
    // Public member function to set values
    void setDetails(string studentName, float studentMarks) {
        name = studentName;
        marks = studentMarks;
    }

    // Inline function defined inside the class body
    inline bool isPassing() const {
        return marks >= 40.0f;
    }

    // Public member function to display values
    void display() const {
        cout << "Student Name : " << name << endl;
        cout << "Marks        : " << marks << endl;
        cout << "Result       : " << (isPassing() ? "Passed" : "Failed") << endl;
    }
};

int main() {
    Student s1, s2;

    s1.setDetails("Aarav", 78.5f);
    s2.setDetails("Rohan", 32.0f);

    cout << "--- Student 1 Details ---" << endl;
    s1.display();

    cout << "\n--- Student 2 Details ---" << endl;
    s2.display();

    return 0;
}
