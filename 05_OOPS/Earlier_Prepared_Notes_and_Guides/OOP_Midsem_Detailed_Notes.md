# Object Oriented Programming with C++ (ITDC0201)
## Complete Mid-Semester Notes — NIT Jalandhar, B.Tech IT, 3rd Semester

*Built from: official syllabus (Units 1–3), the Sept-2025 mid-sem paper, and E. Balagurusamy's OOP with C++ (5th ed.)*

---

## 0. Exam Pattern & Strategy

From the Sept 2025 paper (30 marks, 2 hours):

| Q.No | Marks | CO | Cognitive Level | Unit |
|---|---|---|---|---|
| 1 | 4 | 1 | Create | 1 |
| 2 | 6 | 3 | Create | 4 (Inheritance) |
| 3 | 7.5 | 2 | Evaluate | 3,4 |
| 4 | 7.5 | 3 | Evaluate | 2,3 |
| 5 | 5 | 3 | Create | 2 |

**Reading this pattern:**
- Q1 is always a *small, self-contained function* (references, pointers, simple logic) — easy marks, don't drop them.
- Q2 is a *long design program* — usually a mini system (Hospital, Library, Bank) built with base + derived classes, multiple constructors, static members, and a friend/external display function. This is the single highest-value question to drill.
- Q3 is *output tracing* — 5–6 short snippets testing: virtual inheritance, const objects, friend function mismatches, operator overloading semantics, dangling references, copy constructor/destructor order. You must explain *why*, not just guess output.
- Q4 is *conceptual theory + code justification* — short crisp definitions backed by a one-line C++ snippet.
- Q5 is another *design program*, usually operator-overloading-heavy (a mathematical class like Vector3D, Complex, Matrix, Fraction).

**Strategy:** Master Units 1–3 cold (this is the current syllabus), but also revise inheritance/virtual functions/polymorphism basics since the previous paper drew Q2 and part of Q3 from that territory — mid-sems often reuse question shapes even when the syllabus wording changes slightly.

---

## 1. UNIT 1 — Foundations, Functions

### 1.1 Need for Object-Oriented Programming / Procedural vs OOP

**Procedure-oriented programming (POP):**
- Organized around *functions* — the program is a sequence of instructions/algorithms.
- Data is largely **global** or passed between functions as parameters.
- Functions transform data; data itself has no inherent protection.
- Problem at scale: if the data representation changes, *every* function that touches it may break. Tight coupling between data and the many functions using it.
- Follows top-down decomposition: break the problem into functions, then sub-functions.

**Object-oriented programming (OOP):**
- Organized around **objects** that bundle data (state) with the operations (behavior) allowed on that data.
- Data is hidden inside objects (**private**) and can be accessed only through the object's own functions.
- Example: an `Account` object keeps `balance` private; the only way to change it is via `deposit()`/`withdraw()`, so invalid states are prevented at the source.
- Result: safer, more maintainable, more reusable code that models real-world entities more naturally.

**Exam-ready comparison table:**

| Aspect | Procedural | OOP |
|---|---|---|
| Focus | Functions/algorithms | Objects (data + behavior) |
| Data | Global, exposed | Private, encapsulated |
| Approach | Top-down | Bottom-up (build objects, then combine) |
| Security | Low (any function can touch data) | High (controlled access) |
| Reusability | Low | High (via inheritance) |
| Real-world modelling | Weak | Strong |

### 1.2 Object-Oriented Concepts (definitions the exam wants verbatim-precise)

- **Class** — a user-defined data type / blueprint that declares data members and member functions; no memory is allocated for a class by itself.
- **Object** — a runtime instance of a class; each object gets its own copy of the data members (but shares the code of member functions).
- **Encapsulation** — binding data and the functions operating on it together into a single unit (the class).
- **Data hiding** — restricting direct access to an object's internal representation, typically by making data members `private`.
- **Abstraction** — exposing only the essential operations/interface to the user while hiding implementation detail.
  > *Exam trap:* Encapsulation, data hiding and abstraction are related but **not synonyms** — never define all three with one sentence. Encapsulation = the *bundling mechanism*; data hiding = the *access restriction*; abstraction = the *conceptual simplification*.
- **Inheritance** — a derived (child) class acquires the accessible properties and behavior of a base (parent) class; models an "is-a" relationship.
- **Polymorphism** — literally "many forms": the same interface (function name/operator) behaves differently depending on context. Two kinds:
  - *Compile-time (static)* polymorphism — function overloading, operator overloading.
  - *Run-time (dynamic)* polymorphism — virtual functions resolved via base class pointers/references.
- **Dynamic binding** — the decision of *which* overridden virtual function to call is deferred until run time, based on the actual (dynamic) object type.
- **Message passing** — objects communicate by invoking each other's member functions with arguments, just like sending a "message."

**Benefits of OOP (list form for Q4-style answers):** modularity, maintainability, data security via encapsulation, code reuse via inheritance, extensibility, natural modelling of real-world entities, reduced code duplication.

### 1.3 C++ Program Structure

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, C++\n";
    return 0;
}
```

Compilation pipeline (can be asked as theory):
1. **Preprocessor** — expands directives (`#include`, `#define`) before actual compilation.
2. **Compiler** — checks syntax, translates to object code.
3. **Linker** — combines object files + libraries (e.g., resolves `cout` from `iostream`) into an executable.
4. **Loader** — loads the executable into memory for execution.

- `main()` must return `int`.
- `main()` **cannot be overloaded** — there is only ever one entry point.
- Valid signatures: `int main()` and `int main(int argc, char* argv[])`.

### 1.4 Function Prototyping

- A **prototype** declares return type, function name, and parameter types *before* first use — it does not include a body.
- A **definition** supplies the full body.
- Parameter *names* in a prototype are optional (only types matter for the compiler); you may write `double area(double, double);`.
- Prototyping lets you call a function before its definition appears later in the file (or in another file, via a header).

```cpp
double area(double, double);              // prototype
double area(double length, double width) { // definition
    return length * width;
}
```

### 1.5 Inline Functions

- `inline` is a **request**, not a command, to the compiler: it asks that the function body be substituted directly at each call site instead of a normal function call (saves call-overhead for small, frequently used functions).
- The compiler is free to ignore the request (e.g., if the function is too large, recursive, or has loops).
- A function **defined inside a class body** is implicitly `inline` for linkage purposes, even without the keyword.
- **A `static` local variable is legal inside an inline function** (frequently asked!) — though its presence often makes true inlining impractical, since each expansion must still respect one shared static instance.

```cpp
inline int cube(int n) { return n * n * n; }
```

### 1.6 Reference Variables & Call by Reference

- A **reference** (`int&`) is an *alias* for an existing variable — not a new variable, not a pointer. It shares the same memory address as the variable it refers to.
- A reference **must be initialized at declaration** and **cannot be reseated** afterward to refer to something else.
- A non-const reference (`int&`) **cannot bind to a literal or a temporary** value — e.g. `int& r = 5;` is illegal.
- A **`const` reference** *can* bind to a temporary, which is why it's the idiomatic way to pass large objects for read-only access without copying: `void print(const string& s)`.

**Call by value vs call by reference vs call by pointer:**

| Mechanism | What's passed | Effect on original |
|---|---|---|
| Call by value | A copy | Unaffected |
| Call by reference (`T&`) | An alias | Modified directly |
| Call by pointer (`T*`) | An address | Modified via dereferencing (`*ptr`) |

```cpp
void squareInPlace(int& n) { n = n * n; }
int main() {
    int x = 6;
    squareInPlace(x);   // call as squareInPlace(x), NOT squareInPlace(&x)
    // x is now 36
}
```
> **Common mistake (exam Q1 style!):** for `void f(int& x)`, call it as `f(a)`. The `&` belongs only in the *parameter declaration*, never in the call.

**Return by reference:** a function returning `T&` returns an *alias* to an object that must outlive the call — this makes the function call usable as an **lvalue** (can appear on the left of `=`).

```cpp
int& larger(int& a, int& b) { return (a > b) ? a : b; }
int main() {
    int x = 5, y = 10;
    larger(x, y) = 100;   // y becomes 100
}
```
> **Danger:** Never return a reference (or pointer) to a **local automatic variable** — it is destroyed when the function returns, leaving a **dangling reference**; using it afterward is undefined behavior (this is exactly the trap in the previous paper's `getLarger` question — see solved traces below).

### 1.7 Default Arguments

- A default argument is a value automatically supplied for a trailing parameter if the caller omits it.
- Defaults must be specified **from right to left** (trailing parameters only) and only **once** — either in the prototype or the definition, not both.

```cpp
void printBill(int id, int copies = 1, bool detailed = false);
printBill(101);          // copies=1, detailed=false
printBill(101, 3);       // detailed=false
printBill(101, 3, true);
```

### 1.8 Function Overloading

- Multiple functions with the **same name** but differing in **number, type, or order** of parameters.
- **Return type alone cannot distinguish overloads** — `int maximum(int,int)` and `double maximum(int,int)` together is a compile error.

```cpp
int maximum(int a, int b);
double maximum(double a, double b);
int maximum(int a, int b, int c);
```
- Overload resolution happens at **compile time** → this is why overloading is called *static/compile-time polymorphism*.
- A `const` parameter (e.g. `void f(const int)`) promises the function will not modify that parameter's copy, but note: `f(int)` and `f(const int)` are treated as the **same signature** for top-level `const` on a by-value parameter (cannot overload on that alone).
- **Recursion** is related conceptually: needs a base case + a recursive case that converges toward it; every call gets its own stack frame.

```cpp
long long factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}
```

### 1.9 Math Library Functions

Declared in `<cmath>` (C++) / `<math.h>` (C-style). Frequently used ones to know cold:

| Function | Purpose | Example |
|---|---|---|
| `sqrt(x)` | Square root | `sqrt(16.0)` → 4.0 |
| `pow(x, y)` | x raised to power y | `pow(2, 3)` → 8 |
| `abs(x)` / `fabs(x)` | Absolute value (int / double) | `fabs(-3.5)` → 3.5 |
| `ceil(x)` | Round up | `ceil(4.2)` → 5.0 |
| `floor(x)` | Round down | `floor(4.8)` → 4.0 |
| `round(x)` | Round to nearest | `round(4.5)` → 5.0 |
| `sin(x), cos(x), tan(x)` | Trigonometric (radians) | — |
| `log(x)` | Natural log | — |
| `log10(x)` | Base-10 log | — |
| `exp(x)` | e^x | — |

```cpp
#include <cmath>
double d = sqrt(pow(3,2) + pow(4,2)); // 5.0 — classic distance formula usage
```
These typically show up as small utility calls inside larger design programs (e.g., a `Vector3D::magnitude()` using `sqrt`), rather than being tested standalone — but a direct short-answer question ("name any 4 math library functions with syntax") is possible.

---

## 2. UNIT 2 — Classes, Objects, Static & Friend

### 2.1 Difference between C `struct` and C++ `class`

| | `struct` | `class` |
|---|---|---|
| Default member access | `public` | `private` |
| Default inheritance | `public` | `private` |
| Can have member functions, constructors | Yes (in C++) | Yes |
| Conventional use | Plain data aggregates | Full-featured objects with behavior |

> Key exam line: *"class defaults to private access; struct defaults to public access. A C++ struct can still contain member functions and participate in inheritance — the only functional difference from a class is the default access specifier."*

### 2.2 Specifying a Class

```cpp
class BankAccount {
private:
    long accountNumber;
    double balance;
    bool validAmount(double amount) const { return amount > 0; }  // private helper
public:
    void open(long number, double initialBalance);
    void deposit(double amount);
    void display() const;
};   // <-- semicolon is REQUIRED after a class definition
```
- **`private`** members: accessible only within the class's own member functions (and its friends).
- **`protected`** members: accessible within the class and any class that inherits from it.
- **`public`** members: form the external interface, accessible from anywhere the object is visible.

### 2.3 Member Functions, Memory Layout, and the `this` Pointer

- Every **object** gets its **own storage** for non-static data members.
- **Member function code is shared** across all objects — it is not duplicated per object.
- An out-of-class definition is qualified with `ClassName::` but is still a full member with access to private data:

```cpp
void BankAccount::open(long number, double initialBalance) {
    accountNumber = number;
    balance = initialBalance >= 0 ? initialBalance : 0.0;
}
void BankAccount::display() const {
    cout << accountNumber << " : " << balance << '\n';
}
```
- **`this`** — an implicit pointer available inside every non-static member function, pointing to the object on which the function was invoked. A **static member function has no `this` pointer** (no object context).

```cpp
class Item {
    int code;
public:
    Item& setCode(int code) {
        this->code = code;   // disambiguates member 'code' from parameter 'code'
        return *this;        // enables chaining: obj.setCode(1).setCode(2)
    }
};
```

### 2.4 Scope Resolution Operator (`::`)

Three uses, all testable:
1. **Access a global variable hidden by a local of the same name.**
2. **Define a member function outside the class.**
3. **Qualify a name inside a namespace.**

```cpp
int value = 100;               // global
int main() {
    int value = 20;            // local, hides global
    cout << value << " " << ::value;  // prints: 20 100
}
```

### 2.5 Array Within a Class

A class can contain an array as a data member, just like any other type:
```cpp
class Student {
    int marks[5];       // array within the class
    string name;
public:
    Student(string n) : name(n) { for (int i=0;i<5;i++) marks[i]=0; }
    void setMark(int i, int m) { marks[i] = m; }
};
```
Each object stores its own independent copy of the array.

### 2.6 Array of Objects

```cpp
class Student {
    string name;
public:
    Student() : name("Unnamed") {}     // default constructor REQUIRED for plain array
    Student(string n) : name(n) {}
};
int main() {
    Student batch[3];                  // needs Student() default constructor
    Student named[2] = { Student("A"), Student("B") };  // uses parameterized ctor
}
```
> **Exam trap:** `ClassName arr[n];` calls the **default constructor** for every element — if no default constructor exists (e.g., because you defined only a parameterized one), this line is a **compile error**.

### 2.7 Static Data Members and Static Member Functions

```cpp
class Doctor {
    string name;
    static int totalDoctors;     // declaration only, inside class
public:
    Doctor(string n) : name(n) { ++totalDoctors; }
    static int count() { return totalDoctors; }  // static member function
};
int Doctor::totalDoctors = 0;    // definition + initialization, OUTSIDE the class (mandatory, once)
```
- A **static data member** exists in exactly **one copy shared by all objects** of the class — it is *not* part of any individual object's storage.
- It is (traditionally) **declared inside** the class and **defined/initialized outside**, exactly once, using `ClassName::member = value;`.
- A **static member function**:
  - Is called using `ClassName::function()` (no object required), though it can also be called via an object.
  - Has **no `this` pointer**.
  - Can **directly access only other static members** (it has no specific object's non-static data to work with).

> **Common mistake:** a static function trying to directly read/write an ordinary (non-static) data member is a compile error — it would need an object reference to do that.

### 2.8 Friend Function

```cpp
class Box {
    int length;
public:
    Box(int l) : length(l) {}
    friend void printLength(const Box& b);   // friend declaration, INSIDE class
};
void printLength(const Box& b) {              // definition OUTSIDE, NO ClassName:: prefix
    cout << b.length;                          // can access private member directly
}
```
Key rules (heavily tested via Q3-style traces):
- A friend function is a **non-member** function granted explicit access to a class's private/protected members.
- Declared with the `friend` keyword **inside** the class, but **defined like an ordinary function outside** — it must **not** use the `ClassName::` scope operator (it isn't a member).
- Called like any regular function: `printLength(myBox);`, not `myBox.printLength();`.
- **Friendship is not inherited, not transitive, and not reciprocal** (if A is a friend of B, B is not automatically a friend of A).
- **The friend declaration's parameter types must exactly match the definition's signature** — a mismatch (e.g., `friend void printLength(Box b);` declared but `void printLength()` defined with zero parameters) creates a **different, unrelated function** with no friend access → compile error if it tries to touch private data. *(This exact trap appears in the previous paper's Q3c — see solved traces.)*
- A class can also declare an **entire other class** as its friend, or a **specific member function of another class**.

---

## 3. UNIT 3 — Constructors, Destructors, Operator Overloading, Pointers

### 3.1 Constructors

- A **constructor** is a special member function that runs **automatically** when an object is created.
- Same name as the class, **no return type** (not even `void`).
- **Can be overloaded** (multiple constructors, differing in parameters).
- Used to guarantee the object starts in a valid state.

**Types of constructors:**

1. **Default constructor** — takes no arguments (or all-defaulted arguments).
```cpp
class Patient {
    int id, room; string disease;
public:
    Patient() : id(0), room(-1), disease("Unknown") {}
};
```
2. **Parameterized constructor** — takes arguments to initialize members with caller-supplied values.
```cpp
Patient(int i, string d) : id(i), room(-1), disease(d) {}
```
3. **Copy constructor** — constructs a new object as a copy of an existing one of the same class. Canonical signature: `ClassName(const ClassName& other)`.
```cpp
Array(const Array& other) : size(other.size), data(new int[other.size]) {
    for (int i = 0; i < size; ++i) data[i] = other.data[i];
}
```
   - If you don't write one, the compiler generates an **implicit memberwise copy constructor** — fine for simple value members, but **dangerous for a class owning a raw pointer** (see shallow vs deep copy below).
   - Copy constructor is invoked in three situations: (a) `T b = a;` or `T b(a);`, (b) passing an object **by value** to a function, (c) returning an object **by value** from a function (subject to compiler copy elision).
4. **Constructor overloading** — several constructors, e.g. Patient can be built from just `(id, disease)` or from full `(name, age, gender, id, disease, room)` — enables "multiple ways to create objects," a phrase that shows up verbatim in Q2-style hospital/library system prompts.

**Member-initializer list** — the `: member(value), ...` syntax:
- **Required** (not optional) for: `const` data members, reference data members, and members that are objects of a class with no default constructor, and for initializing a base class's constructor.
- Members are initialized in the **order they are declared in the class**, not the order written in the initializer list (a subtle output-tracing trap).

```cpp
class Doctor {
    const string hospital;     // const member — MUST use initializer list
public:
    Doctor(string h) : hospital(h) {}
};
```

**Dynamic initialization of objects** — supplying constructor arguments computed or obtained at run time (e.g., from user input, a function call, or `new`), rather than fixed compile-time literals:
```cpp
int n; cin >> n;
Array a(n);                      // size decided at run time
Patient* p = new Patient(id, disease);   // dynamically allocated + initialized
```

**`const` objects:**
- A `const` object can call **only `const` member functions**.
- The `const` qualifier is written **after** the parameter list: `void show() const { ... }`.
```cpp
class Sample {
    int x;
public:
    Sample(int a) : x(a) {}
    void show() { cout << x; }     // NOT const
};
int main() {
    const Sample obj(5);
    obj.show();   // COMPILE ERROR: cannot call non-const function on a const object
}
```

### 3.2 Destructors

- Written `~ClassName()`. **No parameters, no return type, cannot be overloaded** (only one destructor per class).
- Runs **automatically**: at scope exit for an automatic (stack) object, or after `delete` for a dynamically allocated (heap) object.
- **Objects are destroyed in reverse order of construction.**
- For derived-class objects: **derived class destructor runs first, then the base class destructor** (opposite of construction order, which is base-first).
- **Deep copy vs shallow copy:**
  - *Shallow copy* (default memberwise copy): if a class owns a raw pointer (e.g., dynamically allocated array), copying just duplicates the *address* — both objects now point to the same memory. When both are destroyed, the memory is `delete`d **twice** → undefined behavior / crash.
  - *Deep copy*: the copy constructor allocates **new, independent storage** and copies the actual values.
- **Rule of Three:** if a class needs a custom destructor (because it manages a resource like heap memory), it almost always also needs a custom **copy constructor** and **copy assignment operator**.

```cpp
class Array {
    int size; int* data;
public:
    Array(int n) : size(n), data(new int[n]{}) {}
    Array(const Array& o) : size(o.size), data(new int[o.size]) {
        for (int i=0;i<size;++i) data[i]=o.data[i];
    }
    ~Array() { delete[] data; }
};
```
> **Tracing note:** exact copy-constructor/destructor call counts around **return-by-value** can vary due to compiler **copy elision** (the compiler is allowed to skip a copy entirely). In an exam trace, explain the *lifetime/order logic* rather than assuming one fixed portable count — this exact ambiguity is baked into the previous paper's Q3f (`createSample()` trace).

### 3.3 Operator Overloading and Type Conversion

**Core rule:** operator overloading gives an *existing* C++ operator additional meaning for a user-defined type, via a specially named function `operator@` (where `@` is the symbol). You **cannot**:
- invent brand-new operator symbols,
- change an operator's precedence, associativity, or arity (number of operands),
- overload `.`, `.*`, `::`, `?:`, or `sizeof`.
- At least **one operand must be of a user-defined type**.

**Member vs non-member (friend) implementation:**

| | Member operator function | Non-member / friend operator function |
|---|---|---|
| Left operand | Implicit (the calling object, via `this`) | Must be passed explicitly as a parameter |
| `a + b` becomes | `a.operator+(b)` | `operator+(a, b)` |
| Use when | Left operand is always your class type | Left operand is **not** your class (e.g., `cout << obj`, where the left operand is `ostream`) |
| Must-be-member operators | `=`, `[]`, `()`, `->` (these can **never** be non-member) | — |

**Defining/overloading a unary operator** (one operand, e.g., unary `-`, `++`, `--`):
```cpp
class Counter {
    int val;
public:
    Counter(int v=0): val(v) {}
    Counter operator-() const { return Counter(-val); }   // unary minus, no parameters (member)
    Counter& operator++() { ++val; return *this; }         // prefix ++
    Counter operator++(int) { Counter tmp=*this; val++; return tmp; } // postfix ++ (dummy int param)
};
```

**Defining/overloading a binary operator** (two operands, e.g. `+`, `-`, `*`, `==`):
```cpp
class Vector3D {
    double x,y,z;
public:
    Vector3D(double a=0,double b=0,double c=0):x(a),y(b),z(c){}
    Vector3D operator+(const Vector3D& r) const { return Vector3D(x+r.x, y+r.y, z+r.z); }
};
```

**Overloading `<<` for `cout` (must-know, appears almost every year):**
- `ostream` is the **left operand** of `<<` and you cannot modify the built-in `ostream` class.
- Therefore `operator<<` **must be implemented as a non-member (usually `friend`) function**, returning `ostream&` so that chained output (`cout << a << b`) keeps working.
```cpp
friend ostream& operator<<(ostream& out, const Vector3D& v) {
    return out << '(' << v.x << ", " << v.y << ", " << v.z << ')';
}
```

**Type conversion** (three directions — asked conceptually):
1. **Basic type → class type**: handled automatically by a matching constructor, e.g. `Vector3D v = 5;` works if there's a constructor `Vector3D(double)`.
2. **Class type → basic type**: needs a special **conversion operator** member function with no return type and no parameters: `operator double() const { return magnitude; }`.
3. **Class type → different class type**: achieved either via a converting constructor in the destination class, or a conversion operator in the source class.

**Tracing tip:** always **follow the actual code inside the operator function**, ignoring what the operator symbol "should" intuitively mean. E.g., if `operator+` is coded to internally do `value - n.value`, then `a + b` genuinely *subtracts* — the misleading name never overrides the real implementation (this exact trap is Q3d in the previous paper).

### 3.4 Introduction to Pointers

- A **pointer** is a variable that stores the **memory address** of another variable, rather than a data value directly.
- **Pointer and address:** every variable lives at some address in memory; a pointer variable's *value* is that address.
- **Address-of operator `&`:** applied to a variable, yields its memory address.
```cpp
int x = 10;
int* p = &x;     // p now holds the address of x
cout << *p;      // dereference: prints 10 (the value AT that address)
cout << p;       // prints the address itself
```
- **Pointer variable declaration:** `type* name;` — e.g. `int* p;`, `double* q;`, `char* c;`. The pointer's type must match the type of variable it points to (so the compiler knows how many bytes to read/write and how to interpret pointer arithmetic).
- **Dereference operator `*`:** applied to a pointer, accesses/modifies the value **at** the address it holds.

```cpp
int x = 6;
int* p = &x;
*p = 20;          // x is now 20 — modifying through the pointer
```

**Void pointer (`void*`):**
- A **generic pointer** that can hold the address of *any* data type, but **cannot be directly dereferenced** (the compiler doesn't know the size/type of what it points to) without first casting it to a concrete type.
```cpp
int a = 5; double b = 3.14;
void* vp;
vp = &a;   // OK
vp = &b;   // also OK — void* accepts any type's address
// cout << *vp;         // ERROR — cannot dereference void* directly
cout << *(int*)vp;      // OK after cast (if vp currently holds an int's address)
```

**Dangling pointer:**
- A pointer that still holds the address of memory that has been **freed / gone out of scope** (e.g., `delete`d, or a local variable that has returned).
- Using (dereferencing) a dangling pointer is **undefined behavior**.
```cpp
int* p = new int(5);
delete p;      // memory freed
// p is now dangling — p still holds the old address
cout << *p;    // undefined behavior
p = nullptr;   // good practice: neutralize the dangling pointer
```
- This is the pointer analogue of the reference-to-local-variable trap in section 1.6.

**Null pointer:**
- A pointer explicitly set to point to **nothing** — conventionally `nullptr` in modern C++ (or `NULL`/`0` in older code).
- Used to signal "this pointer is not currently valid / not pointing anywhere," and should always be checked before dereferencing.
```cpp
int* p = nullptr;
if (p != nullptr) { cout << *p; }   // safe guard
```

**Quick contrast table (a favorite short-answer ask):**

| Pointer type | Meaning |
|---|---|
| `void*` | Can point to any type; needs casting to dereference |
| Dangling pointer | Points to freed/invalid memory — accidental, dangerous |
| Null pointer | Deliberately points to nothing — safe, checkable |

---

## 4. Bonus Coverage: Inheritance & Virtual Functions
*(Not in the current syllabus scan, but directly tested in the previous mid-sem's Q2/Q3 — worth knowing at a working level in case it resurfaces.)*

### 4.1 Base/Derived Classes & Inheritance Visibility

```cpp
class Person {
protected:
    string name; int age;
public:
    Person(string n, int a) : name(n), age(a) {}
};
class Patient : public Person {
    int patientId;
public:
    Patient(string n, int a, int id) : Person(n,a), patientId(id) {}
};
```
- Inheritance models an **"is-a"** relationship.
- A base class's **private** members are never *directly* accessible in the derived class (though they still physically exist in the base sub-object).

**Effect of inheritance mode on inherited member visibility:**

| Inheritance type | Base `public` becomes | Base `protected` becomes |
|---|---|---|
| `public` | `public` | `protected` |
| `protected` | `protected` | `protected` |
| `private` | `private` | `private` |

> **Exam-favorite line:** *"Under private inheritance, both the public and protected members of the base class become private in the derived class."*

### 4.2 Construction Order, Multiple & Virtual Inheritance

- Construction order for a derived object: **base class subobject(s) first → then members → then the derived class constructor body**. Destruction happens in **exact reverse**.
- **Multiple inheritance** — a derived class has more than one direct base class.
- **The diamond problem:** if `B` and `C` both (non-virtually) inherit from `A`, and `D` inherits from both `B` and `C`, then `D` ends up with **two separate copies of `A`** — any unqualified reference to an `A` member from `D` is **ambiguous → compile error**.
- **Virtual inheritance** (`class B : virtual public A`) solves this: it guarantees only **one shared copy** of `A` exists in `D`, no matter how many paths lead to it. The **most-derived class** becomes responsible for initializing the virtual base.

```cpp
class A { public: void show(){ cout<<"A\n"; } };
class B : virtual public A { public: B(){ cout<<"B "; } };
class C : virtual public A { public: C(){ cout<<"C "; } };
class D : public B, public C { public: D(){ cout<<"D "; } };
// Only ONE A exists. d.show() is unambiguous.
```
> If only **one** of `B`/`C` inherits virtually and the other doesn't (as in the previous paper's Q3a), `D` still ends up with **two `A` subobjects**, and calling `obj.show()` is **ambiguous → does not compile.**

### 4.3 Polymorphism & Virtual Functions

- **Compile-time polymorphism**: function/operator overloading (resolved at compile time, by signature).
- **Run-time polymorphism**: `virtual` functions, resolved at run time based on the object's actual (dynamic) type, accessed via a base class pointer or reference.
```cpp
class Person { public: virtual void role() const { cout<<"Person\n"; } virtual ~Person()=default; };
class Doctor : public Person { public: void role() const override { cout<<"Doctor\n"; } };
Person* p = new Doctor;
p->role();   // prints "Doctor" — dynamic binding
delete p;
```
- `override` — asks the compiler to *verify* this really overrides a base virtual function (catches typos in signature).
- **Virtual destructor** — essential whenever an object might be `delete`d through a base class pointer; without it, only the base part is destroyed (derived resources leak).
- **Pure virtual function** (`virtual ... = 0;`) makes a class **abstract** — it cannot be instantiated directly, only used as a base.

---

## 5. Previous Mid-Sem Paper — Fully Solved (Sept 2025)

### Q1 (4 marks) — Reference parameter, square in place

```cpp
#include <iostream>
using namespace std;

void squareIt(int &n) {
    n = n * n;
}

int main() {
    int x;
    cout << "Enter a number: ";
    cin >> x;
    squareIt(x);
    cout << "Squared value: " << x << endl;
    return 0;
}
```
*Justification:* `n` is a reference to `x`, so `n = n*n` directly mutates `x` itself — no return value is needed, satisfying "modifies the original variable."

### Q2 (6 marks) — Hospital Management System

```cpp
#include <iostream>
#include <string>
using namespace std;

class Patient; class Doctor;
void displayPatient(const Patient&);
void displayDoctor(const Doctor&);

class Person {
protected:
    string name, gender;
    int age;
public:
    Person(string n="Not recorded", int a=0, string g="Not recorded")
        : name(n), age(a), gender(g) {}
};

class Patient : public Person {
    int id, room;
    string disease;
public:
    // partial info constructor
    Patient(int i, string d) : Person(), id(i), room(-1), disease(d) {}
    // full info constructor
    Patient(string n, int a, string g, int i, string d, int r)
        : Person(n,a,g), id(i), room(r), disease(d) {}
    friend void displayPatient(const Patient& p);
};

class Doctor : public Person {
    string specialty;
    const string hospital;         // cannot be changed once assigned
    static int total;              // tracks total doctor records created
public:
    Doctor(string n, int a, string g, string s, string h)
        : Person(n,a,g), specialty(s), hospital(h) { ++total; }
    static int count() { return total; }
    friend void displayDoctor(const Doctor& d);
};
int Doctor::total = 0;

// non-member functions with friend access — can read private/protected data of BOTH classes
void displayPatient(const Patient& p) {
    cout << "Patient -> ID: " << p.id << ", Disease: " << p.disease
         << ", Room: " << p.room << ", Name: " << p.name << '\n';
}
void displayDoctor(const Doctor& d) {
    cout << "Doctor -> Name: " << d.name << ", Specialty: " << d.specialty
         << ", Hospital: " << d.hospital << '\n';
}

int main() {
    Patient p1(101, "Fever");                                   // partial-info constructor
    Patient p2("Aarav", 20, "Male", 102, "Migraine", 12);        // full-info constructor
    Doctor  d1("Meera", 42, "Female", "Cardiology", "NIT Hospital"); // full detail doctor

    displayPatient(p1);
    displayPatient(p2);
    displayDoctor(d1);
    cout << "Total doctor records created: " << Doctor::count() << endl;
    return 0;
}
```
**Design notes to state in the exam:**
- `Person` is the common base holding `name`, `age`, `gender`.
- `Patient` demonstrates **constructor overloading** (two ways to build an object — partial vs full detail).
- `Doctor::hospital` is `const` → **must** be set via the member-initializer list, and can never change afterward.
- `Doctor::total` is `static` → **one shared counter** across all `Doctor` objects, incremented in the constructor.
- `displayPatient`/`displayDoctor` are **non-member friend functions**, so they can read private data of both classes without being a member of either.

### Q3 — Output Tracing With Justification

**(a) Diamond problem — mixed virtual/non-virtual inheritance**
```cpp
class A { public: A(){cout<<"A ";} void show(){cout<<"show A\n";} };
class B : virtual public A { public: B(){cout<<"B ";} };
class C : public A { public: C(){cout<<"C ";} };       // NOT virtual
class D : public B, public C { public: D(){cout<<"D ";} };
int main() { D obj; obj.show(); }
```
> **Answer:** `B` inherits `A` **virtually**, but `C` inherits `A` **non-virtually** — so `D` ends up with **two distinct `A` sub-objects** (one shared-virtual one via `B`, one separate one via `C`). Construction order would print something like `A B A C D`, **but** `obj.show()` is **ambiguous** (the compiler cannot tell which `A::show()` you mean) → **this is a compile-time error, there is no runtime output.**

**(b) `const` object calling a non-const member function**
```cpp
class Sample {
    int x;
public:
    Sample(int a): x(a) {}
    void show() { cout << "Value: " << x << endl; }   // NOT const
};
int main() { const Sample obj(5); obj.show(); return 0; }
```
> **Answer:** **Compile error.** `obj` is declared `const`, so it may only call member functions also marked `const`. `show()` lacks the `const` qualifier, so this call is illegal — no output.

**(c) Friend declaration/definition signature mismatch**
```cpp
class Box {
    int length;
public:
    Box(int l): length(l) {}
    friend void printLength(Box b);      // friend declared taking a Box parameter
};
void printLength() {                     // but DEFINED with NO parameters!
    Box b(10);
    cout << "Length: " << b.length << endl;   // tries to access private member
}
int main() { printLength(); }
```
> **Answer:** **Compile error.** The `friend` declaration inside `Box` names a function `printLength(Box)`, but the actual defined function is `printLength()` — a completely **different, unrelated function** with a different signature. That defined `printLength()` was **never granted friendship**, so its attempt to access `b.length` (a private member) is illegal → compile error.

**(d) Operator overloading — follow the code, not the symbol**
```cpp
class Number {
    int value;
public:
    Number(int v): value(v) {}
    Number operator+(const Number &n) { return Number(value - n.value); }  // "+" actually subtracts!
    void display() { cout << "Value: " << value << endl; }
};
int main() { Number a(10), b(4); Number c = a + b; c.display(); }
```
> **Answer:** `a + b` calls `a.operator+(b)`, whose body computes `value - n.value` = `10 - 4` = `6`. Output: **`Value: 6`**. The lesson: never assume `+` means addition — always trace the actual function body.

**(e) Returning a reference to a local variable — dangling reference**
```cpp
int& getLarger(int &a, int &b) {
    int local;
    if (a > b) local = a; else local = b;
    return local;     // returning reference to a LOCAL variable
}
int main() {
    int x = 5, y = 10;
    int &ref = getLarger(x, y);
    ref = 100;
    cout << "x = " << x << ", y = " << y << endl;
}
```
> **Answer:** `local` is destroyed the instant `getLarger` returns, so `ref` is a **dangling reference** to freed stack memory. Writing `ref = 100` is **undefined behavior** — the output of `x` and `y` **cannot be reliably predicted** (in practice `x` and `y` are typically unaffected since `local` was a separate variable, but this is not guaranteed — the correct exam answer is "undefined behavior," not a specific number).

**(f) Constructor / copy constructor / destructor ordering**
```cpp
class Sample {
    int id;
public:
    Sample(int i): id(i) { cout << "Constructor called for id = " << id << endl; }
    Sample(const Sample &s): id(s.id) { cout << "Copy Constructor called for id = " << id << endl; }
    ~Sample() { cout << "Destructor called for id = " << id << endl; }
};
Sample createSample() { Sample temp(99); return temp; }
int main() {
    Sample s1(1);
    Sample s2 = createSample();
    Sample s3(s1);
    cout << "End of main" << endl;
}
```
> **Answer (with copy elision, the typical modern-compiler case):**
> ```
> Constructor called for id = 1        // s1
> Constructor called for id = 99       // temp inside createSample (elided directly into s2)
> Copy Constructor called for id = 1   // s3(s1)
> End of main
> Destructor called for id = 1         // s3 destroyed first (reverse of construction)
> Destructor called for id = 99        // s2
> Destructor called for id = 1         // s1
> ```
> *State explicitly in the exam:* "Modern compilers apply **copy elision** for `return temp;`, so the copy constructor for `temp → s2` is typically skipped; if elision did **not** apply, an extra 'Copy Constructor called for id = 99' and matching destructor would appear." Destruction order is always the **reverse of construction order** for objects in the same scope: `s3, s2, s1`.

### Q4 (7.5 marks) — Conceptual + Justification

**i. Member vs non-member operator overloading:**
A member operator implicitly takes the calling object as its left operand (`a+b` → `a.operator+(b)`), so it can only be used when the left operand is your own class type. A non-member (often `friend`) operator takes both operands explicitly as parameters (`operator+(a,b)`), which is required when the left operand isn't your class — e.g. `cout << obj` needs a non-member `operator<<` since `ostream` is on the left.

**ii. Can inline functions have static variables?**
Yes. A `static` local variable is legal inside an `inline` function. However, because a static variable must exist as one shared instance regardless of how many times the function is expanded, it typically discourages the compiler from actually inlining the call (the compiler may fall back to a normal function call to keep the static instance single).

**iii. Private inheritance visibility:**
If a class is inherited using `private` visibility mode, **both the public and protected members of the base class become private** in the derived class — inaccessible to any further class that inherits from the derived class.

**iv. Overloading `<<` for `cout`:**
Implement it as a **non-member (typically `friend`) function**, since `ostream` (the type of `cout`) is the left operand and cannot be modified. It must return `ostream&` to allow chained calls:
```cpp
friend ostream& operator<<(ostream& out, const MyClass& obj) {
    out << obj.someMember;
    return out;
}
```

**v. Returning a reference to a local variable:**
The local variable's storage is deallocated the moment the function returns, so the returned reference becomes a **dangling reference** pointing to invalid/freed stack memory. Any subsequent use (read or write) through that reference is **undefined behavior** — it may appear to "work" by chance, crash, or silently corrupt memory, and the behavior is not portable/reliable.

### Q5 (5 marks) — Vector3D Drone Navigation

```cpp
#include <iostream>
#include <cmath>
using namespace std;

class Vector3D {
    double x, y, z;
public:
    Vector3D(double a=0, double b=0, double c=0) : x(a), y(b), z(c) {}

    Vector3D operator+(const Vector3D& r) const {   // vector addition -> new position
        return Vector3D(x+r.x, y+r.y, z+r.z);
    }
    Vector3D operator-(const Vector3D& r) const {   // displacement between two positions
        return Vector3D(x-r.x, y-r.y, z-r.z);
    }
    double operator*(const Vector3D& r) const {     // dot product
        return x*r.x + y*r.y + z*r.z;
    }
    double magnitude() const {                       // distance from origin
        return sqrt(x*x + y*y + z*z);
    }
    friend ostream& operator<<(ostream& out, const Vector3D& v) {
        return out << '(' << v.x << ", " << v.y << ", " << v.z << ')';
    }
};

int main() {
    double px, py, pz, mx, my, mz;
    cout << "Enter current position (x y z): ";
    cin >> px >> py >> pz;
    cout << "Enter movement vector (x y z): ";
    cin >> mx >> my >> mz;

    Vector3D position(px, py, pz);
    Vector3D movement(mx, my, mz);
    Vector3D finalPosition = position + movement;

    cout << "New position: " << finalPosition << endl;
    cout << "Displacement from origin: " << finalPosition.magnitude() << endl;
    cout << "Dot product (initial . final): " << position * finalPosition << endl;
    return 0;
}
```
**Design notes to state in the exam:**
- `operator+` overloaded for **vector addition** → new drone position.
- `operator-` overloaded for **displacement** between two positions.
- `operator*` overloaded (returns `double`, not `Vector3D`) for **dot product**.
- `operator<<` implemented as a **non-member friend**, returning `ostream&`, since `ostream` must be the left operand.
- "Displacement from the origin" is naturally the vector's **magnitude** (`sqrt(x²+y²+z²)`), separate from the `operator-` displacement between two arbitrary points — mention both interpretations if the question is ambiguous, since examiners have used it both ways.

---

## 6. Final Revision Checklist (say these exact things if asked to define/compare)

- `class` defaults to **private**; `struct` defaults to **public**. Both can have constructors, member functions, and participate in inheritance.
- A **static data member** has one class-wide copy; conventionally declared inside, defined once outside. A **static member function** has no `this` pointer and can only directly touch other static members.
- A **friend** function/class is a **non-member** granted explicit access; friendship is **not inherited, not transitive, not reciprocal**, and the declared signature must match the defined signature exactly.
- A **constructor** has the class's name and **no return type**; can be overloaded. A **destructor** is `~ClassName()`, has **no parameters**, **cannot be overloaded**, and runs in **reverse order** of construction.
- **Default arguments** must be **trailing** and specified **once**. **Return type alone** can never distinguish overloaded functions.
- A **reference** must be initialized at declaration and can never be reseated; **never return a reference (or pointer) to a local variable** — it dangles.
- `operator<<` for `cout` should (almost) always be a **non-member/friend** returning `ostream&`.
- **Private inheritance** converts both inherited `public` and `protected` members to `private` in the derived class.
- **Virtual inheritance** prevents duplicate common-base copies in a diamond hierarchy; the **most-derived class** initializes the virtual base.
- A **virtual destructor** is essential whenever deleting a derived object through a base class pointer.
- A **`void*`** can hold any type's address but needs an explicit cast before dereferencing; a **dangling pointer** points to freed memory (accidental danger); a **null pointer** (`nullptr`) deliberately points to nothing and should be checked before use.

### General Output-Tracing Method (apply to every Q3-style question)
1. **Check compilation first.** Invalid private access, `const` mismatch, friend signature mismatch, missing semicolon, or inheritance ambiguity → **no runtime output at all**, just state "compile error" and why.
2. **List construction order**: base(s) first, then members, then the constructor body; note whether any base is virtual (single shared copy) or not (separate copies, possible ambiguity).
3. **Track references/pointers vs by-value copies separately** — only a reference/pointer can change the caller's original.
4. **For any overloaded operator, mentally substitute the operator expression with its actual function call**, then trace the function body literally — never assume the "obvious" mathematical meaning.
5. **At scope exit, destroy automatic objects in exact reverse order of construction.** Flag return-by-value cases as subject to **copy elision** rather than asserting one guaranteed count.

---

*Reference basis: E. Balagurusamy, Object-Oriented Programming with C++, 5th Edition — chapters on OOP principles, functions, classes & objects, constructors & destructors, operator overloading, and inheritance/virtual functions — cross-checked against the official ITDC0201 syllabus and the Sept-2025 mid-semester paper.*
