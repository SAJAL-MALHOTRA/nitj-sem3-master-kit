# OOPS Lab Assignment 4: Pointers and Classes

### Task 1 - Void Pointer
Create a student class with rollno, name, age, marks, and grade. Use a void pointer to access and display the age, marks, and grade of a student object using appropriate type casting.

**Ans -**

```cpp
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
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_4\" ; if ($?) { g++ 1.cpp -o 1 } ; if ($?) { .\1 }
=== Student Details via Void Pointer Typecasting ===
Age   : 20
Marks : 88.5
Grade : A
```

---

### Task 2 – Null Pointer
Create a student object and a student* pointer initialized to nullptr. Check the pointer before accessing the object and then assign the object's address to display its details using the -> operator.

**Ans -**

```cpp
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

    void display() {
        cout << "Roll No : " << rollno << endl;
        cout << "Name    : " << name << endl;
        cout << "Age     : " << age << endl;
        cout << "Marks   : " << marks << endl;
        cout << "Grade   : " << grade << endl;
    }
};

int main() {
    Student s(102, "Rohan", 21, 91.0f, 'A');

    // Initializing pointer to nullptr
    Student* ptr = nullptr;

    // Checking the pointer before accessing
    cout << "=== Checking Null Pointer ===" << endl;
    if (ptr == nullptr) {
        cout << "Pointer is currently NULL (nullptr). Cannot access object safely." << endl;
    }

    // Assigning object address to the pointer
    ptr = &s;
    cout << "\nPointer assigned to student object address." << endl;

    if (ptr != nullptr) {
        cout << "\n=== Accessing Student Details via '->' Operator ===" << endl;
        ptr->display();
    }

    return 0;
}
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_4\" ; if ($?) { g++ 2.cpp -o 2 } ; if ($?) { .\2 }
=== Checking Null Pointer ===
Pointer is currently NULL (nullptr). Cannot access object safely.

Pointer assigned to student object address.

=== Accessing Student Details via '->' Operator ===
Roll No : 102
Name    : Rohan
Age     : 21
Marks   : 91
Grade   : A
```

---

### Task 3 – Pointer Arithmetic
Create an array of 5 student objects and use pointer arithmetic to traverse the array. Display each student's rollno, name, and marks, and find the student with the highest marks without using array indexing.

**Ans -**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Student {
public:
    int rollno;
    string name;
    float marks;

    Student() : rollno(0), name(""), marks(0.0f) {}
    Student(int r, string n, float m) : rollno(r), name(n), marks(m) {}
};

int main() {
    Student students[5] = {
        Student(101, "Alice", 82.5f),
        Student(102, "Bob", 95.0f),
        Student(103, "Charlie", 74.0f),
        Student(104, "Diana", 89.5f),
        Student(105, "Ethan", 91.0f)
    };

    Student* ptr = students;
    Student* highest = ptr;

    cout << "=== Student List (Traversed using Pointer Arithmetic) ===" << endl;
    for (int i = 0; i < 5; i++) {
        cout << "Roll No: " << (ptr + i)->rollno 
             << " | Name: " << (ptr + i)->name 
             << " | Marks: " << (ptr + i)->marks << endl;

        if ((ptr + i)->marks > highest->marks) {
            highest = (ptr + i);
        }
    }

    cout << "\n=== Student with Highest Marks (Found without array indexing) ===" << endl;
    cout << "Roll No : " << highest->rollno << endl;
    cout << "Name    : " << highest->name << endl;
    cout << "Marks   : " << highest->marks << endl;

    return 0;
}
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_4\" ; if ($?) { g++ 3.cpp -o 3 } ; if ($?) { .\3 }
=== Student List (Traversed using Pointer Arithmetic) ===
Roll No: 101 | Name: Alice | Marks: 82.5
Roll No: 102 | Name: Bob | Marks: 95
Roll No: 103 | Name: Charlie | Marks: 74
Roll No: 104 | Name: Diana | Marks: 89.5
Roll No: 105 | Name: Ethan | Marks: 91

=== Student with Highest Marks (Found without array indexing) ===
Roll No : 102
Name    : Bob
Marks   : 95
```

---

### Task 4 – Array of Pointers
Create 5 student objects and an array of student pointers containing their addresses. Use the pointer array to display the students and arrange them in descending order of their marks by rearranging only the pointers.

**Ans -**

```cpp
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
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_4\" ; if ($?) { g++ 4.cpp -o 4 } ; if ($?) { .\4 }
=== Students Before Sorting (Array of Pointers) ===
Roll: 101, Name: Alice, Marks: 82.5
Roll: 102, Name: Bob, Marks: 95
Roll: 103, Name: Charlie, Marks: 74
Roll: 104, Name: Diana, Marks: 89.5
Roll: 105, Name: Ethan, Marks: 91

=== Students Arranged in Descending Order of Marks (Only Pointers Swapped) ===
Rank 1 -> Roll: 102 | Name: Bob | Marks: 95
Rank 2 -> Roll: 105 | Name: Ethan | Marks: 91
Rank 3 -> Roll: 104 | Name: Diana | Marks: 89.5
Rank 4 -> Roll: 101 | Name: Alice | Marks: 82.5
Rank 5 -> Roll: 103 | Name: Charlie | Marks: 74
```

---

### Task 5 – Pointer to Array
Create a 2 × 3 array of student objects and a pointer to an array. Use pointer arithmetic to access each row and calculate the total marks obtained by students in each row.
**What does 2 × 3 mean?**
It means the array has: 2 rows, 3 students in each row and Total = 6 students.

**Ans -**

```cpp
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
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_4\" ; if ($?) { g++ 5.cpp -o 5 } ; if ($?) { .\5 }
=== 2 x 3 Student Matrix Traversal ===

Row 1 Students:
  Student 1: Aarav (Marks: 85)
  Student 2: Bhavya (Marks: 90)
  Student 3: Chetan (Marks: 75)
Total Marks for Row 1 = 250

Row 2 Students:
  Student 1: Divya (Marks: 92)
  Student 2: Esha (Marks: 88)
  Student 3: Farhan (Marks: 81)
Total Marks for Row 2 = 261
```

---

### Task 6 – Pointers and Arrays
Using task 3, display student details using both array notation and pointer notation. Modify the marks of one student using a pointer and display the updated details.

**Ans -**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Student {
public:
    int rollno;
    string name;
    float marks;

    Student() : rollno(0), name(""), marks(0.0f) {}
    Student(int r, string n, float m) : rollno(r), name(n), marks(m) {}
};

int main() {
    Student students[5] = {
        Student(101, "Alice", 82.5f),
        Student(102, "Bob", 78.0f),
        Student(103, "Charlie", 74.0f),
        Student(104, "Diana", 89.5f),
        Student(105, "Ethan", 91.0f)
    };

    Student* ptr = students;

    cout << "=== Displaying Using Array Notation (arr[i]) ===" << endl;
    for (int i = 0; i < 5; i++) {
        cout << "Roll: " << students[i].rollno << ", Name: " << students[i].name 
             << ", Marks: " << students[i].marks << endl;
    }

    cout << "\n=== Displaying Using Pointer Notation (*(ptr + i)) ===" << endl;
    for (int i = 0; i < 5; i++) {
        cout << "Roll: " << (*(ptr + i)).rollno << ", Name: " << (*(ptr + i)).name 
             << ", Marks: " << (*(ptr + i)).marks << endl;
    }

    // Modifying the marks of the 2nd student (Bob, index 1) using pointer
    cout << "\nModifying marks of Bob (index 1) via pointer from " << (ptr + 1)->marks << " to 95.0..." << endl;
    (ptr + 1)->marks = 95.0f;

    cout << "\n=== Updated Student Details (Bob) ===" << endl;
    cout << "Roll: " << (ptr + 1)->rollno 
         << " | Name: " << (ptr + 1)->name 
         << " | Updated Marks: " << (ptr + 1)->marks << endl;

    return 0;
}
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_4\" ; if ($?) { g++ 6.cpp -o 6 } ; if ($?) { .\6 }
=== Displaying Using Array Notation (arr[i]) ===
Roll: 101, Name: Alice, Marks: 82.5
Roll: 102, Name: Bob, Marks: 78
Roll: 103, Name: Charlie, Marks: 74
Roll: 104, Name: Diana, Marks: 89.5
Roll: 105, Name: Ethan, Marks: 91

=== Displaying Using Pointer Notation (*(ptr + i)) ===
Roll: 101, Name: Alice, Marks: 82.5
Roll: 102, Name: Bob, Marks: 78
Roll: 103, Name: Charlie, Marks: 74
Roll: 104, Name: Diana, Marks: 89.5
Roll: 105, Name: Ethan, Marks: 91

Modifying marks of Bob (index 1) via pointer from 78 to 95.0...

=== Updated Student Details (Bob) ===
Roll: 102 | Name: Bob | Updated Marks: 95
```

---

### Task 7 – Constant Pointer
Create two student objects and declare a constant pointer pointing to the first object. Modify its marks and grade through the pointer, and demonstrate why the pointer cannot be redirected to the second object.

**Ans -**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Student {
public:
    int rollno;
    string name;
    float marks;
    char grade;

    Student(int r, string n, float m, char g) : rollno(r), name(n), marks(m), grade(g) {}
};

int main() {
    Student s1(101, "Aman", 80.0f, 'B');
    Student s2(102, "Kavya", 92.0f, 'A');

    // Constant pointer to Student object (address stored cannot be changed)
    Student* const ptr = &s1;

    cout << "=== Initial Details of s1 ===" << endl;
    cout << "Name: " << ptr->name << ", Marks: " << ptr->marks << ", Grade: " << ptr->grade << endl;

    // Modifying data through the constant pointer is ALLOWED
    ptr->marks = 88.0f;
    ptr->grade = 'A';

    cout << "\n=== Modified Details of s1 via Constant Pointer ===" << endl;
    cout << "Name: " << ptr->name << ", Marks: " << ptr->marks << ", Grade: " << ptr->grade << endl;

    // Attempting to redirect the pointer to s2 is NOT ALLOWED:
    // ptr = &s2; // COMPILE ERROR: assignment of read-only variable 'ptr'
    cout << "\nDemonstration: ptr = &s2 fails at compile time because 'ptr' is a constant pointer." << endl;

    return 0;
}
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_4\" ; if ($?) { g++ 7.cpp -o 7 } ; if ($?) { .\7 }
=== Initial Details of s1 ===
Name: Aman, Marks: 80, Grade: B

=== Modified Details of s1 via Constant Pointer ===
Name: Aman, Marks: 88, Grade: A

Demonstration: ptr = &s2 fails at compile time because 'ptr' is a constant pointer.
```

---

### Task 8 – Constant Pointer to Constant
Create a student object and use a constant pointer to constant student data. Display all five attributes mentioned above in task 1 and demonstrate why neither the student data nor the pointer address can be modified.

**Ans -**

```cpp
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

    Student(int r, string n, int a, float m, char g) 
        : rollno(r), name(n), age(a), marks(m), grade(g) {}
};

int main() {
    Student s1(101, "Pooja", 20, 89.0f, 'A');
    Student s2(102, "Rohit", 22, 75.0f, 'B');

    // Constant pointer to constant student data
    const Student* const ptr = &s1;

    cout << "=== Displaying All 5 Attributes via const Student* const ptr ===" << endl;
    cout << "Roll No : " << ptr->rollno << endl;
    cout << "Name    : " << ptr->name << endl;
    cout << "Age     : " << ptr->age << endl;
    cout << "Marks   : " << ptr->marks << endl;
    cout << "Grade   : " << ptr->grade << endl;

    // Demonstration of restrictions:
    // 1. Cannot modify student data:
    // ptr->marks = 95.0f; // COMPILE ERROR: assignment of member 'Student::marks' in read-only object
    
    // 2. Cannot redirect pointer address:
    // ptr = &s2;          // COMPILE ERROR: assignment of read-only variable 'ptr'

    cout << "\nDemonstration: Both student data modification (ptr->marks = 95.0) and" << endl;
    cout << "pointer redirection (ptr = &s2) are rejected by the compiler." << endl;

    return 0;
}
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_4\" ; if ($?) { g++ 8.cpp -o 8 } ; if ($?) { .\8 }
=== Displaying All 5 Attributes via const Student* const ptr ===
Roll No : 101
Name    : Pooja
Age     : 20
Marks   : 89
Grade   : A

Demonstration: Both student data modification (ptr->marks = 95.0) and
pointer redirection (ptr = &s2) are rejected by the compiler.
```

---

### Task 9 – Pointer to Constant
Write a function that accepts a pointer to constant student and displays all five attributes mentioned in task 1. Demonstrate that the student's data can be read but cannot be modified through the pointer.

**Ans -**

```cpp
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

    Student(int r, string n, int a, float m, char g) 
        : rollno(r), name(n), age(a), marks(m), grade(g) {}
};

// Function accepting a pointer to constant student
void displayStudent(const Student* s) {
    cout << "=== Student Attributes (Read via const Student*) ===" << endl;
    cout << "Roll No : " << s->rollno << endl;
    cout << "Name    : " << s->name << endl;
    cout << "Age     : " << s->age << endl;
    cout << "Marks   : " << s->marks << endl;
    cout << "Grade   : " << s->grade << endl;

    // Demonstration that data cannot be modified through the pointer:
    // s->marks = 99.0f; // COMPILE ERROR: assignment of member in read-only object
}

int main() {
    Student s(105, "Meera", 19, 93.5f, 'A');

    displayStudent(&s);

    cout << "\nDemonstration: Inside displayStudent(), any attempt to modify data" << endl;
    cout << "such as (s->marks = 99.0f) produces a compile-time error." << endl;

    return 0;
}
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_4\" ; if ($?) { g++ 9.cpp -o 9 } ; if ($?) { .\9 }
=== Student Attributes (Read via const Student*) ===
Roll No : 105
Name    : Meera
Age     : 19
Marks   : 93.5
Grade   : A

Demonstration: Inside displayStudent(), any attempt to modify data
such as (s->marks = 99.0f) produces a compile-time error.
```

---

### Task 10 - Pointer to Pointer
Create a student object, a pointer to the object, and a pointer to pointer. Use the student** pointer to access and modify the student's marks and grade, then display the updated details.

**Ans -**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Student {
public:
    int rollno;
    string name;
    float marks;
    char grade;

    Student(int r, string n, float m, char g) 
        : rollno(r), name(n), marks(m), grade(g) {}
};

int main() {
    // 1. Create student object
    Student s(110, "Siddharth", 76.0f, 'C');

    // 2. Create pointer to the object
    Student* ptr = &s;

    // 3. Create pointer to pointer
    Student** pptr = &ptr;

    cout << "=== Initial Student Details ===" << endl;
    cout << "Name  : " << (*pptr)->name << endl;
    cout << "Marks : " << (*pptr)->marks << endl;
    cout << "Grade : " << (*pptr)->grade << endl;

    // Modifying student marks and grade using pointer to pointer (**pptr)
    (*pptr)->marks = 89.5f;
    (*pptr)->grade = 'A';

    cout << "\n=== Updated Student Details (Modified via Student** pptr) ===" << endl;
    cout << "Name          : " << (*pptr)->name << endl;
    cout << "Updated Marks : " << (*pptr)->marks << endl;
    cout << "Updated Grade : " << (*pptr)->grade << endl;

    return 0;
}
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_4\" ; if ($?) { g++ 10.cpp -o 10 } ; if ($?) { .\10 }
=== Initial Student Details ===
Name  : Siddharth
Marks : 76
Grade : C

=== Updated Student Details (Modified via Student** pptr) ===
Name          : Siddharth
Updated Marks : 89.5
Updated Grade : A
```
