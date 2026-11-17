#include <iostream>
#include <string>
using namespace std;
class Student {
private:
    string name;
    float marks;

public:
    void setDetails(const string& studentName, float studentMarks) {
        name = studentName;
        marks = studentMarks;
    }

    inline bool isPassing() const {
        return marks >= 40;
    }

    void display() const {
        cout << "Student: " << name << "\nMarks: " << marks 
                  << "\nStatus: " << (isPassing() ? "Passed" : "Failed") << endl;
    }
};

int main() {
    Student s;
    s.setDetails("Sajal", 78.5);
    s.display();
    return 0;
}