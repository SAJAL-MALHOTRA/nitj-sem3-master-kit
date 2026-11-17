#include<bits/stdc++.h>
using namespace std ;

class Student {
public:
    int rollno;
    string name;
    int age;
    float marks;
    char grade;

    Student() : rollno(0), name(""), age(0), marks(0.0f), grade('F') {}
    Student(int r, string n, int a, float m, char g)
        : rollno(r), name(n), age(a), marks(m), grade(g) {}

    void display() const {
        cout << "Roll No: " << rollno << " | Name: " << name
             << " | Age: " << age << " | Marks: " << marks
             << " | Grade: " << grade << endl;
    }
};
void task1() {
  //void is a generic pointer that can hold value of any data type
  //It has no type information, so the compiler doesn't know how many bytes to read or how to interpret them
    cout << "Task 1 - Void Pointer" << endl;
    Student s(1, "malhotra", 20, 85.5, 'A');

    void* vp;

    vp = &s.age;
    cout << "Age   : " << *(static_cast<int*>(vp)) << endl;

    vp = &s.marks;
    cout << "Marks : " << *(static_cast<float*>(vp)) << endl;

    vp = &s.grade;
    cout << "Grade : " << *(static_cast<char*>(vp)) << endl;
}
void task2() {
  // A null pointer points to nothing
  //dereferncing a null is undefined behaviour
  //used to avoid wild pointer issues
    cout << "Task 2 - Null Pointer" << endl;
    Student s(2, "sajal", 21, 91.0, 'A');
    Student* ptr = nullptr;

    if (ptr == nullptr)
        cout << "Pointer is null - cannot access the object yet." << endl;

    ptr = &s;
    if (ptr != nullptr) {
        cout << "Pointer assigned. Details via -> operator:" << endl;
        cout << "Roll No: " << ptr->rollno << ", Name: " << ptr->name
             << ", Age: " << ptr->age << ", Marks: " << ptr->marks
             << ", Grade: " << ptr->grade << endl;
    }
}
void task3() {
  // Pointer arithmetic allows you to navigate through arrays using pointers
    cout << "Task 3 - Pointer Arithmetic" << endl;
    Student arr[5] = {
        Student(1, "sajal",   20, 78.0f, 'B'),
        Student(2, "malhotra", 21, 91.5f, 'A'),
        Student(3, "sam", 19, 66.0f, 'C'),
        Student(4, "sammy",  20, 88.0f, 'A'),
        Student(5, "sahil",   22, 72.5f, 'B')
    };

    Student* p = arr;
    Student* topper = arr;

    for (; p < arr + 5; ++p) {
        cout << "Roll No: " << p->rollno << " | Name: " << p->name
             << " | Marks: " << p->marks << endl;
        if (p->marks > topper->marks)
            topper = p;
    }

    cout << "\nStudent with highest marks:" << endl;
    topper->display();
}
void task4() {
  // An array of pointers is an array where each element is a pointer to a data type
    cout << "Task 4 - Array of Pointers" << endl;
    Student s1(1, "sajal",   20, 78.0f, 'B');
    Student s2(2, "malhotra", 21, 91.5f, 'A');
    Student s3(3, "sam", 19, 66.0f, 'C');
    Student s4(4, "sammy",  20, 88.0f, 'A');
    Student s5(5, "sahil",   22, 72.5f, 'B');

    Student* ptrs[5] = {&s1, &s2, &s3, &s4, &s5};
//sorting pointers is a cheat technique to sort objects without moving the actual objects in memory. Instead, we just rearrange the pointers to point to the objects in the desired order.
    cout << "Before sorting:" << endl;
    for (int i = 0; i < 5; i++) ptrs[i]->display();

    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4 - i; j++) {
            if (ptrs[j]->marks < ptrs[j + 1]->marks) {
                Student* tmp = ptrs[j];
                ptrs[j] = ptrs[j + 1];
                ptrs[j + 1] = tmp;
            }
        }
    }

    cout << "\nAfter sorting (descending by marks):" << endl;
    for (int i = 0; i < 5; i++) ptrs[i]->display();
}
void task5() {
    cout << "Task 5 - Pointer to Array" << endl;
    Student arr[2][3] = {
        { Student(1, "sajal",   20, 78.0f, 'B'),
          Student(2, "malhotra", 21, 91.5f, 'A'),
          Student(3, "sam", 19, 66.0f, 'C') },
        { Student(4, "sammy",  20, 88.0f, 'A'),
          Student(5, "sahil",   22, 72.5f, 'B'),
          Student(6, "farhan", 21, 59.0f, 'D') }
    };

    Student (*rowPtr)[3] = arr;   

    for (int i = 0; i < 2; i++) {
        float total = 0;
        cout << "Row " << i + 1 << ":" << endl;
        for (int j = 0; j < 3; j++) {
            Student* s = *(rowPtr + i) + j;   
            cout << "  " << s->name << " - " << s->marks << endl;
            total += s->marks;
        }
        cout << "  Total marks of row " << i + 1 << " = " << total << endl;
    }
}
void task6() {
    cout << "Task 6 - Pointers and Arrays" << endl;
    Student arr[5] = {
        Student(1, "sajal",   20, 78.0f, 'B'),
        Student(2, "malhotra", 21, 91.5f, 'A'),
        Student(3, "sam", 19, 66.0f, 'C'),
        Student(4, "sammy",  20, 88.0f, 'A'),
        Student(5, "sahil",   22, 72.5f, 'B')
    };

    cout << "Using array notation:" << endl;
    for (int i = 0; i < 5; i++) arr[i].display();

    cout << "\nUsing pointer notation:" << endl;
    Student* p = arr;
    for (int i = 0; i < 5; i++) (p + i)->display();

    (p + 2)->marks = 80.0f;
    (p + 2)->grade = 'A';

    cout << "\nAfter modifying 3rd student via pointer:" << endl;
    for (int i = 0; i < 5; i++) (p + i)->display();
}
void task7() {
    cout << "Task 7 - Constant Pointer" << endl;
    Student s1(1, "sajal",   20, 70.0f, 'B');
    Student s2(2, "malhotra", 21, 90.0f, 'A');

    Student* const cp = &s1;  
    cout << "Before:" << endl;
    cp->display();

    cp->marks = 95.0f; 
    cp->grade = 'A';

    cout << "After modifying through the const pointer:" << endl;
    cp->display();

    cout << "'cp = &s2;' would not compile: the pointer itself is const,\n"
            "so it cannot be redirected to the second object." << endl;
    (void)s2;
}
void task8() {
    cout << "Task 8 - Constant Pointer to Constant" << endl;
    Student s1(1, "sajal", 20, 70.0f, 'B');
    Student s2(2, "malhotra", 21, 90.0f, 'A');

    const Student* const cpc = &s1;

    cout << "Roll No: " << cpc->rollno << endl;
    cout << "Name   : " << cpc->name << endl;
    cout << "Age    : " << cpc->age << endl;
    cout << "Marks  : " << cpc->marks << endl;
    cout << "Grade  : " << cpc->grade << endl;

    cout << "\nNeither 'cpc->marks = 99;' nor 'cpc = &s2;' compiles:\n"
            "the data is const and the pointer is const." << endl;
    (void)s2;
}

int main() {
    task1();
    task2();
    task3();
    task4();
    task5();
    task6();
    task7();
    task8();
    return 0;
} 