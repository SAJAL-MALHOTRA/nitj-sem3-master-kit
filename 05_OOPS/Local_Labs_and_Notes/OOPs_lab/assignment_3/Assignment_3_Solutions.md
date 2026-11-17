# Assignment 3: Classes & Scope Resolution

### 1. Write a struct and a class with the exact same two members (one int, one float). In main(), try accessing both members directly using the dot operator on an object of each, without writing any setter functions.
In a comment, explain what happened when you tried this on the class version, and why the struct version behaved differently.

**Ans -**

```cpp
#include <iostream>
using namespace std;

// Struct definition
struct StudentStruct {
    int id;
    float marks;
};

// Class definition
class StudentClass {
    int id;
    float marks;
};

/*
In a comment, explain what happened when you tried this on the class version,
and why the struct version behaved differently:

Observation & Explanation:
- In C++, the only fundamental difference between a `struct` and a `class` is their default access specifier.
- For `struct`, members are PUBLIC by default. Therefore, accessing `s.id` and `s.marks` directly
  using the dot operator succeeds without any compilation errors.
- For `class`, members are PRIVATE by default. Attempting to access `c.id` or `c.marks` directly
  from main() results in a compile-time error:
  "error: 'int StudentClass::id' is private within this context".
- To make the program compile cleanly, the direct access to class private members is commented out below,
  demonstrating the access restriction.
*/

int main() {
    // 1. Accessing struct members directly:
    StudentStruct s;
    s.id = 101;
    s.marks = 88.5f;
    cout << "Struct members accessed directly (default public):" << endl;
    cout << "s.id = " << s.id << ", s.marks = " << s.marks << endl;

    // 2. Trying to access class members directly:
    StudentClass c;
    // c.id = 102;      // COMPILE ERROR: 'id' is private in StudentClass
    // c.marks = 92.0f; // COMPILE ERROR: 'marks' is private in StudentClass
    cout << "\nClass members cannot be accessed directly because they are private by default." << endl;
    cout << "(Attempting c.id = 102 generates a compile error)." << endl;

    return 0;
}
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_3\" ; if ($?) { g++ 1.cpp -o 1 } ; if ($?) { .\1 }
Struct members accessed directly (default public):
s.id = 101, s.marks = 88.5

Class members cannot be accessed directly because they are private by default.
(Attempting c.id = 102 generates a compile error).
```

---

### 2. Write a class Rectangle with private data members for length and width, a public member function to set both values, and a public member function to calculate and return the area. Test it by creating one object, setting its values, and printing the area.

**Ans -**

```cpp
#include <iostream>
using namespace std;

class Rectangle {
private:
    double length;
    double width;

public:
    // Member function to set both values
    void setDimensions(double l, double w) {
        length = l;
        width = w;
    }

    // Member function to calculate and return the area
    double getArea() {
        return length * width;
    }
};

int main() {
    Rectangle rect;
    rect.setDimensions(10.5, 4.0);

    cout << "=== Rectangle Details ===" << endl;
    cout << "Length: 10.5, Width: 4.0" << endl;
    cout << "Calculated Area: " << rect.getArea() << endl;

    return 0;
}
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_3\" ; if ($?) { g++ 2.cpp -o 2 } ; if ($?) { .\2 }
=== Rectangle Details ===
Length: 10.5, Width: 4.0
Calculated Area: 42
```

---

### 3. Write a class Circle where the member functions are only declared inside the class body, and defined outside the class. Include at least one function to set the radius and one to calculate the area.

**Ans -**

```cpp
#include <iostream>
using namespace std;

class Circle {
private:
    double radius;

public:
    // Member functions only declared inside the class body
    void setRadius(double r);
    double calculateArea();
};

// Defining member functions outside the class using Scope Resolution Operator (::)
void Circle::setRadius(double r) {
    radius = r;
}

double Circle::calculateArea() {
    return 3.14159 * radius * radius;
}

int main() {
    Circle c;
    c.setRadius(7.0);

    cout << "=== Circle Details ===" << endl;
    cout << "Radius: 7.0" << endl;
    cout << "Area of Circle: " << c.calculateArea() << endl;

    return 0;
}
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_3\" ; if ($?) { g++ 3.cpp -o 3 } ; if ($?) { .\3 }
=== Circle Details ===
Radius: 7.0
Area of Circle: 153.938
```

---

### 4. Write a program with a global variable and a local variable of the same name inside a function. Access the global variable from inside that function, and print both values to show they are different.

**Ans -**

```cpp
#include <iostream>
using namespace std;

// Global variable
int count = 100;

void showVariables() {
    // Local variable with the exact same name
    int count = 25;

    // Access local variable directly, access global variable using scope resolution (::)
    cout << "Inside showVariables():" << endl;
    cout << "Local variable count  = " << count << endl;
    cout << "Global variable ::count = " << ::count << endl;
}

int main() {
    cout << "Before calling function, Global count = " << count << endl;
    showVariables();
    cout << "After calling function, Global count  = " << count << endl;

    return 0;
}
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_3\" ; if ($?) { g++ 4.cpp -o 4 } ; if ($?) { .\4 }
Before calling function, Global count = 100
Inside showVariables():
Local variable count  = 25
Global variable ::count = 100
After calling function, Global count  = 100
```

---

### 5. Write a class Student with private members for name and marks (use an inline function inside the class for a simple task, like a function that checks if the marks are passing). Add public member functions to set the values and display them.

**Ans -**

```cpp
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
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_3\" ; if ($?) { g++ 5.cpp -o 5 } ; if ($?) { .\5 }
--- Student 1 Details ---
Student Name : Aarav
Marks        : 78.5
Result       : Passed

--- Student 2 Details ---
Student Name : Rohan
Marks        : 32
Result       : Failed
```

---

### 6. Write a class Calculator with public member functions to add, subtract, multiply, and divide two numbers, using function overloading so the same operation names can work for both integers and decimals.

**Ans -**

```cpp
#include <iostream>
using namespace std;

class Calculator {
public:
    // Overloaded add functions
    int add(int a, int b) {
        return a + b;
    }
    double add(double a, double b) {
        return a + b;
    }

    // Overloaded subtract functions
    int subtract(int a, int b) {
        return a - b;
    }
    double subtract(double a, double b) {
        return a - b;
    }

    // Overloaded multiply functions
    int multiply(int a, int b) {
        return a * b;
    }
    double multiply(double a, double b) {
        return a * b;
    }

    // Overloaded divide functions
    double divide(int a, int b) {
        if (b == 0) {
            cout << "Error: Division by zero!" << endl;
            return 0;
        }
        return (double)a / b;
    }
    double divide(double a, double b) {
        if (b == 0.0) {
            cout << "Error: Division by zero!" << endl;
            return 0;
        }
        return a / b;
    }
};

int main() {
    Calculator calc;

    cout << "=== Integer Operations ===" << endl;
    cout << "Add (10, 5)       = " << calc.add(10, 5) << endl;
    cout << "Subtract (10, 5)  = " << calc.subtract(10, 5) << endl;
    cout << "Multiply (10, 5)  = " << calc.multiply(10, 5) << endl;
    cout << "Divide (10, 5)    = " << calc.divide(10, 5) << endl;

    cout << "\n=== Decimal Operations ===" << endl;
    cout << "Add (12.5, 3.5)      = " << calc.add(12.5, 3.5) << endl;
    cout << "Subtract (12.5, 3.5) = " << calc.subtract(12.5, 3.5) << endl;
    cout << "Multiply (12.5, 3.5) = " << calc.multiply(12.5, 3.5) << endl;
    cout << "Divide (12.5, 2.5)   = " << calc.divide(12.5, 2.5) << endl;

    return 0;
}
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_3\" ; if ($?) { g++ 6.cpp -o 6 } ; if ($?) { .\6 }
=== Integer Operations ===
Add (10, 5)       = 15
Subtract (10, 5)  = 5
Multiply (10, 5)  = 50
Divide (10, 5)    = 2

=== Decimal Operations ===
Add (12.5, 3.5)      = 16
Subtract (12.5, 3.5) = 9
Multiply (12.5, 3.5) = 43.75
Divide (12.5, 2.5)   = 5
```

---

### 7. Write a class Temperature with a private data member to hold a value in Celsius, a public member function to set it, and a public member function to convert and return the value in Fahrenheit — using a default argument so the function assumes Celsius input unless told otherwise.

**Ans -**

```cpp
#include <iostream>
using namespace std;

class Temperature {
private:
    double celsius;

public:
    // Member function to set Celsius value
    void setCelsius(double c) {
        celsius = c;
    }

    // Member function to convert and return value in Fahrenheit
    // Uses default argument: isCelsiusInput = true assumes the stored/passed value is in Celsius
    double toFahrenheit(double temp = -1000.0, bool isCelsiusInput = true) {
        double cVal = (temp == -1000.0) ? celsius : temp;
        if (isCelsiusInput) {
            return (cVal * 9.0 / 5.0) + 32.0;
        } else {
            return cVal; // already in Fahrenheit
        }
    }
};

int main() {
    Temperature t;
    t.setCelsius(37.0);

    cout << "=== Temperature Conversion ===" << endl;
    cout << "Stored Temperature in Celsius: 37 C" << endl;
    cout << "Converted to Fahrenheit (using default argument): " 
         << t.toFahrenheit() << " F" << endl;

    cout << "\nConverting 100 C explicitly: " 
         << t.toFahrenheit(100.0) << " F" << endl;
    cout << "Converting 0 C explicitly: " 
         << t.toFahrenheit(0.0) << " F" << endl;

    return 0;
}
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_3\" ; if ($?) { g++ 7.cpp -o 7 } ; if ($?) { .\7 }
=== Temperature Conversion ===
Stored Temperature in Celsius: 37 C
Converted to Fahrenheit (using default argument): 98.6 F

Converting 100 C explicitly: 212 F
Converting 0 C explicitly: 32 F
```

---

### 8. Write a class Book with private members for title, author, and number of available copies. Include public member functions to:
- set the book's details
- display the book's details
- issue a copy
Define at least two of these member functions outside the class. Test by creating two different Book objects and issuing copies from each.

**Ans -**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Book {
private:
    string title;
    string author;
    int availableCopies;

public:
    // Member functions declaration
    void setDetails(string t, string a, int copies);
    void displayDetails();
    void issueCopy();
};

// Defining member functions outside the class using Scope Resolution Operator (::)
void Book::setDetails(string t, string a, int copies) {
    title = t;
    author = a;
    availableCopies = copies;
}

void Book::displayDetails() {
    cout << "Title: " << title 
         << " | Author: " << author 
         << " | Available Copies: " << availableCopies << endl;
}

void Book::issueCopy() {
    if (availableCopies > 0) {
        availableCopies--;
        cout << "Successfully issued 1 copy of \"" << title << "\". Copies left: " << availableCopies << endl;
    } else {
        cout << "Sorry, \"" << title << "\" is currently out of stock!" << endl;
    }
}

int main() {
    Book b1, b2;

    b1.setDetails("The C++ Programming Language", "Bjarne Stroustrup", 2);
    b2.setDetails("Clean Code", "Robert C. Martin", 1);

    cout << "=== Initial Book Records ===" << endl;
    b1.displayDetails();
    b2.displayDetails();

    cout << "\n=== Issuing Copies ===" << endl;
    b1.issueCopy();
    b1.issueCopy();
    b1.issueCopy(); // Attempt to issue when 0 copies left

    cout << endl;
    b2.issueCopy();
    b2.issueCopy(); // Attempt to issue when 0 copies left

    cout << "\n=== Final Book Records ===" << endl;
    b1.displayDetails();
    b2.displayDetails();

    return 0;
}
```

```text
PS C:\Users\2006s\Desktop\OOPs_lab> cd "c:\Users\2006s\Desktop\OOPs_lab\assignment_3\" ; if ($?) { g++ 8.cpp -o 8 } ; if ($?) { .\8 }
=== Initial Book Records ===
Title: The C++ Programming Language | Author: Bjarne Stroustrup | Available Copies: 2
Title: Clean Code | Author: Robert C. Martin | Available Copies: 1

=== Issuing Copies ===
Successfully issued 1 copy of "The C++ Programming Language". Copies left: 1
Successfully issued 1 copy of "The C++ Programming Language". Copies left: 0
Sorry, "The C++ Programming Language" is currently out of stock!

Successfully issued 1 copy of "Clean Code". Copies left: 0
Sorry, "Clean Code" is currently out of stock!

=== Final Book Records ===
Title: The C++ Programming Language | Author: Bjarne Stroustrup | Available Copies: 0
Title: Clean Code | Author: Robert C. Martin | Available Copies: 0
```
