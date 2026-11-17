#include <bits/stdc++.h>
using namespace std;

void task1() {
    cout << " Task 1 "<<endl;
    int i = 10;
    float f = 3.14;
    char c = 'A';

    cout << "Address of int i   : " << &i << endl;
    cout << "Address of float f : " << &f << endl;
    cout << "Address of char c  : " << (void*)&c << endl; // cast needed, else char* prints as string

}

void task2() {
    cout << " Task 2 "<<endl;
    int var = 25;
    int* ptr = &var;

    cout << "Value of var directly     : " << var << endl;
    cout << "Value through pointer (*p): " << *ptr << endl;
    cout << "Address stored in pointer : " << ptr << endl;
}

void task3() {
    cout << "Task 3 "<<endl;
    int a = 5, b = 15;
    int* ptr = &a;

    cout << "Pointer points to a, *ptr = " << *ptr << endl;
    ptr = &b; 
    cout << "Pointer reassigned to b, *ptr = " << *ptr << endl;

    
}

void task4() {
    cout << "Task 4 "<<endl;
    int x = 100;
    int* ptr = &x;

    cout << "Original address : " << ptr << endl;
    ptr++;
    cout << "After increment  : " << ptr << endl;
    ptr--;
    cout << "After decrement  : " << ptr << endl;

}

void task5() {
    cout << "Task 5"<<endl;
    int arr[5] = {10, 20, 30, 40, 50};
    int* ptr = arr; 

    cout << "Forward traversal using pointer only: ";
    for (int i = 0; i < 5; i++) {
        cout << *ptr << " ";
        ptr++;
    }
    cout << endl;
}

void task6() {
    cout << "Task 6"<<endl;
    int arr[5] = {10, 20, 30, 40, 50};
    int* ptr = arr + 4; 

    cout << "Reverse traversal using pointer only: ";
    for (int i = 0; i < 5; i++) {
        cout << *ptr << " ";
        ptr--;
    }
    cout << endl;
}

void task7() {
    cout << "Task 7";
    int   iarr[3] = {1, 2, 3};
    float farr[3] = {1.1, 2.2, 3.3};
    char  carr[3] = {'a', 'b', 'c'};

    int* ip = iarr;
    float* fp = farr;
    char* cp = carr;

    cout << "int pointer:   " << ip << " -> ";
    ip++;
    cout << ip << endl;

    cout << "float pointer: " << fp << " -> ";
    fp++;
    cout << fp << endl;

    cout << "char pointer:  " << (void*)cp << " -> ";
    cp++;
    cout << (void*)cp << endl;

}

void task8() {
    cout << "Task 8 "<<endl;
    int arr[5] = {10, 20, 30, 40, 50};
    int* ptr = arr;

    ptr = ptr + 2;  
    *ptr = 999;     

    cout << "Array after modifying 3rd element: ";
    for (int i = 0; i < 5; i++) cout << arr[i] << " ";
    cout << endl;
}

class Rectangle {
private:
    double length, width;
public:
    void Dimensions(double l, double w) {
        length = l;
        width = w;
    }
    friend double calculateArea(Rectangle r); 
};

double calculateArea(Rectangle r) {
    return r.length * r.width; 
}

void task9() {
    cout << " Task 9 "<<endl;
    Rectangle rect;
    rect.Dimensions(5.0, 3.0);
    cout << "Area of rectangle: " << calculateArea(rect) << endl;

}

class Box {
private:
    double length, width, height;
public:
    void setDimensions(double l, double w, double h) {
        length = l; width = w; height = h;
    }
    friend bool haveEqualVolume(Box b1, Box b2);
};

bool haveEqualVolume(Box b1, Box b2) {
    double vol1 = b1.length * b1.width * b1.height;
    double vol2 = b2.length * b2.width * b2.height;
    return vol1 == vol2;
}

void task10() {
    cout << "Task 10 "<<endl;
    Box b1, b2;
    b1.setDimensions(2, 3, 4);
    b2.setDimensions(4, 3, 2);
    cout << "Do b1 and b2 have equal volume? " << (haveEqualVolume(b1, b2) ? "Yes" : "No") << endl;
}

class RectangleR {
private:
    double length, width;
public:
    void setDimensions(double l, double w) { length = l; width = w; }
    void display() { cout << "length=" << length << ", width=" << width << endl;
     }
    friend void resetLength(RectangleR &r);
};

void resetLength(RectangleR &r) {
    r.length = 0; 
}

void task11() {
    cout << "Task 11 "<<endl;
    RectangleR r;
    r.setDimensions(8, 4);
    cout << "Before reset: ";
    r.display();
    resetLength(r);
    cout << "After reset:  ";
    r.display();

}

class Student {
private:
    string name;
    double marks;
public:
    void setData(string n, double m) { name = n; marks = m; }
    string getName() { return name; }
    double getMarks() { return marks; }
    friend Student getTopper(Student s1, Student s2);
};

Student getTopper(Student s1, Student s2) {
    return(s1.getMarks()>=s2.getMarks()) ? s1 : s2;
}

void task12() {
    cout << "Task 12 "<<endl;
    Student s1, s2;
    s1.setData("Aman", 85.5);
    s2.setData("Riya", 91.0);

    Student* sp = &s1; 
    cout << "s1 data accessed via pointer -> : " << sp->getName() << ", marks = " << sp->getMarks() << endl;

    Student topper = getTopper(*sp, s2);
    cout << "Topper: " << topper.getName() << " with marks " << topper.getMarks() << endl;
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
    task9();
    task10();
    task11();
    task12();
    return 0;
}