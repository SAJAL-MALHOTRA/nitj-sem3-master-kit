#include <iostream>
#include <string>
using namespace std;

class Student {
public:
    int rollno;
    string name;
    float marks;

    Student(int r, string n, float m) : rollno(r), name(n), marks(m) {}
};

int main() {
    Student s1(101, "Alice", 82.5f);
    Student s2(102, "Bob", 95.0f);
    Student s3(103, "Charlie", 74.0f);
    Student s4(104, "Diana", 89.5f);
    Student s5(105, "Ethan", 91.0f);

    // Array of pointers to students
    Student* ptrs[5] = { &s1, &s2, &s3, &s4, &s5 };

    cout << "=== Students Before Sorting (Array of Pointers) ===" << endl;
    for (int i = 0; i < 5; i++) {
        cout << "Roll: " << ptrs[i]->rollno << ", Name: " << ptrs[i]->name 
             << ", Marks: " << ptrs[i]->marks << endl;
    }

    // Rearranging only the pointers in descending order of marks
    for (int i = 0; i < 5 - 1; i++) {
        for (int j = 0; j < 5 - i - 1; j++) {
            if (ptrs[j]->marks < ptrs[j + 1]->marks) {
                Student* temp = ptrs[j];
                ptrs[j] = ptrs[j + 1];
                ptrs[j + 1] = temp;
            }
        }
    }

    cout << "\n=== Students Arranged in Descending Order of Marks (Only Pointers Swapped) ===" << endl;
    for (int i = 0; i < 5; i++) {
        cout << "Rank " << (i + 1) << " -> Roll: " << ptrs[i]->rollno 
             << " | Name: " << ptrs[i]->name 
             << " | Marks: " << ptrs[i]->marks << endl;
    }

    return 0;
}
