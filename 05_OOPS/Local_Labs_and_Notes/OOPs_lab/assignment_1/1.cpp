#include <iostream>
using namespace std;

int main() {
    float marks[5], total = 0, percentage;
    char grade;

    cout << "Enter marks of 5 subjects: ";

    for (int i = 0; i < 5; i++) {
        cin >> marks[i];
        total += marks[i];
    }

    percentage = total / 5;

    // Nested if-else
    if (percentage >= 90) {
        grade = 'A';
    }
    else {
        if (percentage >= 80)
            grade = 'B';
        else {
            if (percentage >= 70)
                grade = 'C';
            else {
                if (percentage >= 60)
                    grade = 'D';
                else
                    grade = 'F';
            }
        }
    }

    cout << "Total Marks = " << total << endl;
    cout << "Percentage = " << percentage << "%" << endl;
    cout << "Grade = " << grade << endl;

    return 0;
}