# Lab Assignment 5: Friend Function & Introduction to Pointers

### Task 1. Declare an integer variable and print its address using the & operator (without using any pointer). Do the same for a float and a char variable.
In a comment, note down the address printed for each and check whether they look different in format for different data types.

**Ans -**

```cpp
#include <iostream>
using namespace std;

/*
Comment: Note down the address printed for each and check whether they look different in format for different data types:
Sample Addresses Observed:
- Address of int i   : 0x5197bff92c
- Address of float f : 0x5197bff928
- Address of char c  : 0x5197bff927

Observation:
All three memory addresses share the exact same format: they are 64-bit hexadecimal memory addresses
(displayed as hex numbers with a 0x prefix on 64-bit platforms). Memory addresses always represent
a byte location in RAM regardless of the underlying data type. Note that for `char`, typecasting `(void*)&c`
is required in C++ because `cout << &c` treats `char*` as a null-terminated C-string and attempts to print characters.
*/

int main() {
    int i = 42;
    float f = 3.14f;
    char c = 'Z';

    cout << "=== Memory Addresses of Different Data Types ===" << endl;
    cout << "Address of int i   : " << &i << endl;
    cout << "Address of float f : " << &f << endl;
    cout << "Address of char c  : " << (void*)&c << endl;

    return 0;
}
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_5\" ; if ($?) { g++ 1.cpp -o 1 } ; if ($?) { .\1 }
=== Memory Addresses of Different Data Types ===
Address of int i   : 0x5197bff92c
Address of float f : 0x5197bff928
Address of char c  : 0x5197bff927
```

---

### Task 2. Declare a pointer variable and make it point to an integer variable using &. Print three things: the value of the variable directly, the value through the pointer (using *), and the address stored in the pointer.

**Ans -**

```cpp
#include <iostream>
using namespace std;

int main() {
    int num = 25;
    int* ptr = &num;

    cout << "=== Variable and Pointer Exploration ===" << endl;
    // 1. Value of variable directly
    cout << "1. Value of num directly          : " << num << endl;

    // 2. Value through pointer using dereference operator (*)
    cout << "2. Value through pointer (*ptr)   : " << *ptr << endl;

    // 3. Address stored in pointer
    cout << "3. Address stored in pointer (ptr): " << ptr << endl;

    return 0;
}
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_5\" ; if ($?) { g++ 2.cpp -o 2 } ; if ($?) { .\2 }
=== Variable and Pointer Exploration ===
1. Value of num directly          : 25
2. Value through pointer (*ptr)   : 25
3. Address stored in pointer (ptr): 0x9b8edffe24
```

---

### Task 3. Declare two integer variables and one pointer. First point the pointer at the first variable and print the dereferenced value, then reassign the pointer to point at the second variable and print again.
In a comment, compare this to a reference variable, can a reference be reassigned to point at a different variable the way a pointer can?

**Ans -**

```cpp
#include <iostream>
using namespace std;

/*
Comment: Compare this to a reference variable, can a reference be reassigned
to point at a different variable the way a pointer can?

Comparison:
- A pointer is an independent variable that holds a memory address. Its stored address can be freely
  reassigned at any point during program execution to point to different variables (e.g., ptr = &b).
- In contrast, a reference is an immutable alias (an alternative name) bound to an existing variable upon
  initialization. A reference CANNOT be reseated/reassigned to refer to another variable.
  If you write `ref = b;`, it does not rebind the reference to 'b'; instead, it assigns the value of 'b'
  into the original variable that 'ref' is referencing.
*/

int main() {
    int num1 = 15;
    int num2 = 45;

    int* ptr = &num1;
    cout << "Pointer initially pointing to num1: *ptr = " << *ptr << endl;

    // Reassigning pointer to point to num2
    ptr = &num2;
    cout << "Pointer reassigned to num2        : *ptr = " << *ptr << endl;

    return 0;
}
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_5\" ; if ($?) { g++ 3.cpp -o 3 } ; if ($?) { .\3 }
Pointer initially pointing to num1: *ptr = 15
Pointer reassigned to num2        : *ptr = 45
```

---

### Task 4. Declare a single (non-array) integer variable and a pointer pointing to it. Print the pointer's address, then increment the pointer and print the address again, then decrement it back and print once more.
In a comment, note by how many bytes the address changed with one increment, and explain why that number matches sizeof(int). Also note: since this pointer isn't pointing into an array, is it safe or meaningful to dereference it after incrementing? Why or why not?

**Ans -**

```cpp
#include <iostream>
using namespace std;

/*
Comment:
1. Address Change:
   Incrementing the pointer increased the hexadecimal address by exactly 4 bytes (e.g. from 0x39e8bffb44 to 0x39e8bffb48).
   This matches sizeof(int) because pointer arithmetic in C++ advances addresses in units of the pointed-to type's size
   (new_address = old_address + 1 * sizeof(int)).

2. Safety of Dereferencing:
   Since 'x' is a standalone scalar integer and NOT part of an array, dereferencing `ptr` after incrementing
   (*ptr) is UNDEFINED BEHAVIOR and completely unsafe. It accesses arbitrary memory outside of the allocated
   variable 'x', which may lead to reading garbage values, data corruption, or segmentation faults.
*/

int main() {
    int x = 100;
    int* ptr = &x;

    cout << "=== Pointer Increment & Decrement ===" << endl;
    cout << "Original address stored in ptr       : " << ptr << endl;

    ptr++;
    cout << "After incrementing (ptr++)           : " << ptr << " (+ " << sizeof(int) << " bytes)" << endl;

    ptr--;
    cout << "After decrementing back (ptr--)      : " << ptr << endl;
    cout << "Dereferencing safe original value    : " << *ptr << endl;

    return 0;
}
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_5\" ; if ($?) { g++ 4.cpp -o 4 } ; if ($?) { .\4 }
=== Pointer Increment & Decrement ===
Original address stored in ptr       : 0x39e8bffb44
After incrementing (ptr++)           : 0x39e8bffb48 (+ 4 bytes)
After decrementing back (ptr--)      : 0x39e8bffb44
Dereferencing safe original value    : 100
```

---

### Task 5. Declare an array of integers and a pointer that points to its first element. Using a loop, traverse and print *every element of the array using only pointer and dereferencing, do not use array indexing (arr[i]) anywhere in the loop.

**Ans -**

```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[5] = {10, 20, 30, 40, 50};
    int* ptr = arr; // points to the first element

    cout << "=== Array Traversal using Pointer and Dereferencing ===" << endl;
    cout << "Elements: ";
    for (int i = 0; i < 5; i++) {
        cout << *ptr << " ";
        ptr++; // advance pointer to next element
    }
    cout << endl;

    return 0;
}
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_5\" ; if ($?) { g++ 5.cpp -o 5 } ; if ($?) { .\5 }
=== Array Traversal using Pointer and Dereferencing ===
Elements: 10 20 30 40 50 
```

---

### Task 6. Using the same array from Task 5, now traverse and print the elements in reverse order, starting by pointing to the last element and using pointer decrement each step, again without using array indexing.

**Ans -**

```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[5] = {10, 20, 30, 40, 50};

    // Point to the last element of the array
    int* ptr = arr + 4;

    cout << "=== Reverse Array Traversal using Pointer Decrement ===" << endl;
    cout << "Elements in reverse: ";
    for (int i = 0; i < 5; i++) {
        cout << *ptr << " ";
        ptr--; // move backwards
    }
    cout << endl;

    return 0;
}
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_5\" ; if ($?) { g++ 6.cpp -o 6 } ; if ($?) { .\6 }
=== Reverse Array Traversal using Pointer Decrement ===
Elements in reverse: 50 40 30 20 10 
```

---

### Task 7. Declare three arrays of different types- int, float, and char, each with a few elements. For each array, point a pointer to the first element, print its address, then increment the pointer once and print the new address.
In a comment, record how many bytes the address moved, and explain what have you observed?

**Ans -**

```cpp
#include <iostream>
using namespace std;

/*
Comment: Record how many bytes the address moved, and explain what have you observed:
Recorded Address Shifts:
- int pointer   : moved by 4 bytes (sizeof(int)   = 4)
- float pointer : moved by 4 bytes (sizeof(float) = 4)
- char pointer  : moved by 1 byte  (sizeof(char)  = 1)

Observation:
When a pointer of type `T*` is incremented by 1 (ptr++), the compiler scales the memory address
by `sizeof(T)` bytes. Pointer arithmetic operates in terms of element offsets, ensuring that incrementing
a pointer cleanly steps to the next contiguous element in memory regardless of data type.
*/

int main() {
    int   iarr[3] = {10, 20, 30};
    float farr[3] = {1.5f, 2.5f, 3.5f};
    char  carr[3] = {'X', 'Y', 'Z'};

    int*   ip = iarr;
    float* fp = farr;
    char*  cp = carr;

    cout << "=== Pointer Increment Across Different Data Types ===" << endl;

    cout << "int pointer   : " << ip;
    ip++;
    cout << " -> " << ip << " (moved by " << sizeof(int) << " bytes)" << endl;

    cout << "float pointer : " << fp;
    fp++;
    cout << " -> " << fp << " (moved by " << sizeof(float) << " bytes)" << endl;

    cout << "char pointer  : " << (void*)cp;
    cp++;
    cout << " -> " << (void*)cp << " (moved by " << sizeof(char) << " byte)" << endl;

    return 0;
}
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_5\" ; if ($?) { g++ 7.cpp -o 7 } ; if ($?) { .\7 }
=== Pointer Increment Across Different Data Types ===
int pointer   : 0xb9a1ffbdc -> 0xb9a1ffbe0 (moved by 4 bytes)
float pointer : 0xb9a1ffbd0 -> 0xb9a1ffbd4 (moved by 4 bytes)
char pointer  : 0xb9a1ffbcd -> 0xb9a1ffbce (moved by 1 byte)
```

---

### Task 8. Declare an integer array. Using a pointer, modify the value of the third element by first moving the pointer to that position using pointer arithmetic, then dereferencing and assigning a new value. Print the whole array afterward (using normal indexing).

**Ans -**

```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[5] = {10, 20, 30, 40, 50};
    int* ptr = arr;

    cout << "=== Original Array ===" << endl;
    for (int i = 0; i < 5; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    // Moving pointer to the 3rd element (index 2) using pointer arithmetic
    ptr = ptr + 2;

    // Dereferencing and assigning a new value
    *ptr = 999;

    cout << "\n=== Array After Modifying 3rd Element via Pointer ===" << endl;
    for (int i = 0; i < 5; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_5\" ; if ($?) { g++ 8.cpp -o 8 } ; if ($?) { .\8 }
=== Original Array ===
10 20 30 40 50 

=== Array After Modifying 3rd Element via Pointer ===
10 20 999 40 50 
```

---

### Task 9. Write a class Rectangle with private members for length and width, and a public member function to set their values. Write a friend function (not a member function) that takes a Rectangle object and directly accesses its private members to calculate and return the area.
In a comment, explain how the friend function was able to access private data without being a member of the class.

**Ans -**

```cpp
#include <iostream>
using namespace std;

class Rectangle {
private:
    double length;
    double width;

public:
    void setDimensions(double l, double w) {
        length = l;
        width = w;
    }

    // Declaring friend function
    friend double calculateArea(Rectangle r);
};

/*
Comment: Explain how the friend function was able to access private data without being a member of the class:
By declaring `friend double calculateArea(Rectangle r);` inside the Rectangle class definition,
the class explicitly grants this external non-member function privileged access to its private and protected members.
Friendship bypasses standard class access control mechanisms strictly for the declared function.
*/

double calculateArea(Rectangle r) {
    // Accessing private members length and width directly
    return r.length * r.width;
}

int main() {
    Rectangle rect;
    rect.setDimensions(8.5, 4.0);

    cout << "=== Rectangle Area via Friend Function ===" << endl;
    cout << "Length: 8.5, Width: 4.0" << endl;
    cout << "Calculated Area: " << calculateArea(rect) << endl;

    return 0;
}
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_5\" ; if ($?) { g++ 9.cpp -o 9 } ; if ($?) { .\9 }
=== Rectangle Area via Friend Function ===
Length: 8.5, Width: 4.0
Calculated Area: 34
```

---

### Task 10. Write a class Box with private members for length, width, and height. Write a friend function that takes two Box objects and returns true if their volumes are equal, false otherwise, accessing both objects' private members directly.

**Ans -**

```cpp
#include <iostream>
using namespace std;

class Box {
private:
    double length;
    double width;
    double height;

public:
    void setDimensions(double l, double w, double h) {
        length = l;
        width = w;
        height = h;
    }

    // Declaring friend function
    friend bool areVolumesEqual(Box b1, Box b2);
};

// Friend function definition
bool areVolumesEqual(Box b1, Box b2) {
    double vol1 = b1.length * b1.width * b1.height;
    double vol2 = b2.length * b2.width * b2.height;
    return (vol1 == vol2);
}

int main() {
    Box box1, box2, box3;

    box1.setDimensions(2.0, 3.0, 4.0); // Volume = 24
    box2.setDimensions(4.0, 3.0, 2.0); // Volume = 24
    box3.setDimensions(5.0, 2.0, 3.0); // Volume = 30

    cout << "=== Comparing Box Volumes using Friend Function ===" << endl;
    cout << "Are Box 1 and Box 2 equal in volume? " 
         << (areVolumesEqual(box1, box2) ? "Yes (Equal)" : "No (Not Equal)") << endl;

    cout << "Are Box 1 and Box 3 equal in volume? " 
         << (areVolumesEqual(box1, box3) ? "Yes (Equal)" : "No (Not Equal)") << endl;

    return 0;
}
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_5\" ; if ($?) { g++ 10.cpp -o 10 } ; if ($?) { .\10 }
=== Comparing Box Volumes using Friend Function ===
Are Box 1 and Box 2 equal in volume? Yes (Equal)
Are Box 1 and Box 3 equal in volume? No (Not Equal)
```

---

### Task 11. Write a friend function that directly modifies a private data member of a class object it's given (for example, resetting a Rectangle's length to zero).
In a comment, discuss the trade-off: since a friend function can freely read and modify private data from outside the class, does this weaken encapsulation? When might that trade-off still be worth it?

**Ans -**

```cpp
#include <iostream>
using namespace std;

class Rectangle {
private:
    double length;
    double width;

public:
    void setDimensions(double l, double w) {
        length = l;
        width = w;
    }

    void display() const {
        cout << "Length: " << length << ", Width: " << width << endl;
    }

    // Friend function to modify private data
    friend void resetLength(Rectangle &r);
};

// Friend function modifying private member 'length' directly
void resetLength(Rectangle &r) {
    r.length = 0.0;
}

/*
Comment: Discuss the trade-off: since a friend function can freely read and modify private data
from outside the class, does this weaken encapsulation? When might that trade-off still be worth it?

Trade-off Discussion:
1. Does it weaken encapsulation?
   Yes, friendship creates tight coupling between external functions and the internal data representation
   of a class. If private member variables change, friend functions must also be updated, which partially
   erodes the boundary of data hiding.
2. When is the trade-off worth it?
   - Operator Overloading: e.g., stream insertion/extraction operators `operator<<` and `operator>>`, where
     the left operand is `std::ostream` and cannot be a class member.
   - High-performance inter-class cooperation: When two closely related classes (e.g., Matrix and Vector,
     or Node and LinkedList) need direct access for performance without exposing public setters to the outside world.
*/

int main() {
    Rectangle rect;
    rect.setDimensions(12.0, 5.0);

    cout << "=== Before Friend Function Modification ===" << endl;
    rect.display();

    resetLength(rect);

    cout << "\n=== After Friend Function Modification (Length Reset to 0) ===" << endl;
    rect.display();

    return 0;
}
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_5\" ; if ($?) { g++ 11.cpp -o 11 } ; if ($?) { .\11 }
=== Before Friend Function Modification ===
Length: 12, Width: 5

=== After Friend Function Modification (Length Reset to 0) ===
Length: 0, Width: 5
```

---

### Task 12. Write a class Student with private members for name and marks. Write a friend function that compares two Student objects and returns the one with higher marks. In main(), create a pointer to a ‘Student’ object, use it to access the object's data via the arrow operator, and pass the pointed-to object into your friend comparison function.

**Ans -**

```cpp
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
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_5\" ; if ($?) { g++ 12.cpp -o 12 } ; if ($?) { .\12 }
=== Accessing Student Data via Pointer and Arrow Operator (->) ===
Student 1 Name  : Aman
Student 1 Marks : 88.5

=== Top Student (Determined via Friend Function) ===
Name  : Riya
Marks : 94
```
