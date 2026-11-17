#include<bits/stdc++.h>
using namespace std;

class Student {
private:
    int rollno;
    string name;
    float marks1, marks2, marks3;

public:
    void input(int r, string n, float m1, float m2, float m3) {
        rollno = r;
        name = n;
        marks1 = m1;
        marks2 = m2;
        marks3 = m3;
    }

    float getAverage() const {
        return (marks1 + marks2 + marks3) / 3.0f;
    }

    void display() const {
        cout << "Roll No: " << rollno 
             << " | Name: " << name 
             << " | Marks: [" << marks1 << ", " << marks2 << ", " << marks3 << "]"
             << " | Average: " << getAverage() << endl;
    }

    string getName() { return name; }
};

int main() {
    int N = 5;
    cout << "Enter number of students: " << N << endl;

    // Dynamically allocating memory using new
    Student* students = new Student[N];

    // Initializing student data
    students[0].input(101, "pritansh", 85.0, 90.0, 88.0);  
    students[1].input(102, "sajal", 92.0, 95.0, 96.0);    
    students[2].input(103, "saksh", 78.0, 82.0, 80.0); 
    students[3].input(104, "samar", 89.0, 91.0, 94.0);   
    students[4].input(105, "samridhi", 70.0, 75.0, 72.0);  

    cout << " Details of All Students " << endl;
    for (int i = 0; i < N; i++) {
        students[i].display();
    }

    
    int highestIdx = -1, secondHighestIdx = -1;
    float highestAvg = -1.0, secondHighestAvg = -1.0;

    for (int i = 0; i < N; i++) {
        float avg = students[i].getAverage();
        if (avg > highestAvg) {
            secondHighestAvg = highestAvg;
            secondHighestIdx = highestIdx;
            highestAvg = avg;
            highestIdx = i;
        } else if (avg > secondHighestAvg && avg != highestAvg) {
            secondHighestAvg = avg;
            secondHighestIdx = i;
        }
    }

    cout << " Student with Second-Highest Average " << endl;
    if (secondHighestIdx != -1) {
        students[secondHighestIdx].display();
    } else {
        cout << "No second highest average found." << endl;
    }

    delete[] students;
    students = nullptr;
    cout << "Dynamically allocated memory released successfully." << endl;

    return 0;
}
