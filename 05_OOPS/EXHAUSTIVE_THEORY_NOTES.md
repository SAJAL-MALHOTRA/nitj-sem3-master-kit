# OBJECT-ORIENTED PROGRAMMING IN C++ (COURSE CODE: ITDC0201)
## The Definitive, Exhaustive Endterm Examination Theory Master Guide
### Author: Distinguished Academic Chair & Professor of Computer Science

---

# TABLE OF CONTENTS
1. [Unit 1: Object-Oriented Programming Paradigm & C++ Functions](#unit-1-object-oriented-programming-paradigm--c-functions)
2. [Unit 2: Classes, Objects, Memory Architecture & Friendship](#unit-2-classes-objects-memory-architecture--friendship)
3. [Unit 3: Constructors, Destructors, Pointers & Operator Overloading](#unit-3-constructors-destructors-pointers--operator-overloading)
4. [Unit 4: Inheritance, Runtime Polymorphism & Virtual Mechanics](#unit-4-inheritance-runtime-polymorphism--virtual-mechanics)
5. [Unit 5: Console I/O, File Stream Handling & Generic Programming (Templates)](#unit-5-console-io-file-stream-handling--generic-programming-templates)
6. [Bonus Exam Mastery: Exception Handling, Modern Type Casting & STL Architecture](#bonus-exam-mastery-exception-handling-modern-type-casting--stl-architecture)
7. [Comprehensive PYQ Direct Mapping & Solution Matrix](#comprehensive-pyq-direct-mapping--solution-matrix)

---

# UNIT 1: Object-Oriented Programming Paradigm & C++ Functions

---

## 1.1 The Software Crisis and the Need for the Object-Oriented Paradigm

During the early eras of computing, software development was dominated by unstructured programming (characterized by widespread use of `goto` statements) and subsequently **Procedural/Structured Programming** (exemplified by C, Pascal, and Fortran). Structured programming organized code around procedures, subroutines, and functions executing algorithmic steps on data.

However, as software complexity grew exponentially in the late 1970s and 1980s—transitioning from simple mathematical scripts to enterprise systems with millions of lines of code—the procedural paradigm suffered severe structural breakdowns known historically as the **Software Crisis**:

1. **Unrestricted Global Data Vulnerability**: In procedural programming, data is treated as a passive entity passed between functions or held globally. Any function with access to global data can modify it inadvertently, causing cascading bugs that are nearly impossible to trace.
2. **Artificial Separation of Data and Behavior**: Real-world entities inherently possess both state (data) and behavior (functions operating on that data). Procedural programming isolates data structures (`struct` in C) from the functions that manipulate them, leaving data integrity unprotected.
3. **High Maintenance and Low Extensibility**: Changing a central data structure in a procedural system necessitates auditing and modifying every single function across the codebase that interacts with that structure.
4. **Poor Real-World Modeling**: Real systems (e.g., banking systems, air-traffic control, graphics systems) consist of discrete interacting entities. Procedural models focus entirely on the *process* rather than the *entities* involved.

### The Paradigm Shift: Object-Oriented Programming (OOP)
Object-Oriented Programming was conceived to invert the relationship between code and data. Instead of placing algorithms at the center and letting data flow loosely between them, **OOP places data at the center of the architecture**, binding functions inextricably to the data they operate on, and hiding internal details behind strictly guarded public interfaces.

---

## 1.2 Procedural Programming (POP) vs. Object-Oriented Programming (OOP)

The following table and architectural diagrams delineate the 10 fundamental architectural, conceptual, and mechanical differences between POP and OOP.

### Architectural Comparison Table

| # | Dimension / Metric | Procedural Programming (POP) | Object-Oriented Programming (OOP) |
|---|---|---|---|
| **1** | **Fundamental Philosophy** | Focuses on *algorithms* and *procedures* (step-by-step instructions to accomplish a task). | Focuses on *data* and *objects* (entities modeling the problem domain). |
| **2** | **Program Decomposition** | Program is divided into units called **Functions** or **Subroutines**. | Program is divided into units called **Classes** and **Objects**. |
| **3** | **Design Approach** | **Top-Down approach**: Begins with the high-level algorithm and decomposes it into smaller functions. | **Bottom-Up approach**: Begins with designing entities, classes, and interactions, building up the system. |
| **4** | **Data Security & Hiding** | **No data hiding**. Data is exposed. Global data can be mutated freely by any function. | **Robust data hiding**. Access specifiers (`private`, `protected`) restrict direct access to state. |
| **5** | **Data Movement & Control Flow** | Data moves freely around the system from function to function via arguments or global scope. | Objects communicate by **message passing** (invoking public member functions on specific object instances). |
| **6** | **Coupling & Cohesion** | High coupling (functions depend heavily on data layouts); Low functional cohesion. | Low coupling (well-defined class interfaces); High cohesive encapsulation within classes. |
| **7** | **Code Reusability** | Limited to function libraries. Extending existing functionality often requires rewriting existing code. | Extensive through **Inheritance** and **Polymorphism** without altering verified base code. |
| **8** | **Extensibility & Scalability** | Adding new data formats requires modifying all existing functions operating on that data. | New classes can be added seamlessly by deriving from existing base classes (Open-Closed Principle). |
| **9** | **Memory & Execution Overhead** | Minimal memory overhead; direct stack allocation and procedural jumps without dynamic dispatch. | Slight memory and performance overhead due to object metadata (e.g., `vptr`, VTABLE lookups). |
| **10** | **Real-World Modeling** | Poor. Maps poorly to real-world objects because processes and state are completely detached. | Natural and expressive. Directly maps real-world entities (e.g., `Car`, `BankAccount`, `Student`) into software objects. |

### Architectural Data Flow Diagrams

#### Procedural Paradigm (Unprotected Data Flow)
```
       +---------------------------------------------+
       |                 GLOBAL DATA                 |
       +---------------------------------------------+
           ^                ^               ^
           | (read/write)   | (read/write)  | (read/write)
           v                v               v
     +------------+   +------------+   +------------+
     | Function A |<->| Function B |<->| Function C |
     +------------+   +------------+   +------------+
           ^                                 ^
           | (passes local data)             |
           +---------------------------------+
```
*Vulnerability: Any bug in Function B can silently corrupt Global Data, immediately crashing Function A and C.*

#### Object-Oriented Paradigm (Encapsulated Autonomous Objects)
```
  +-------------------------------+       +-------------------------------+
  |        OBJECT A               |       |        OBJECT B               |
  |  +-------------------------+  |       |  +-------------------------+  |
  |  |   PRIVATE DATA (State)  |  |       |  |   PRIVATE DATA (State)  |  |
  |  +-------------------------+  |       |  +-------------------------+  |
  |               ^               |       |               ^               |
  |               | (controlled)  |       |               | (controlled)  |
  |  +-------------------------+  |       |  +-------------------------+  |
  |  | PUBLIC METHODS (Behavior)|  |       |  | PUBLIC METHODS (Behavior)|  |
  |  +-------------------------+  |       |  +-------------------------+  |
  +---------------^---------------+       +---------------^---------------+
                  |                                       |
                  |======== Message Passing (Method Call) =|
                  +---------------------------------------+
```
*Integrity: Object A cannot manipulate Object B's private data directly. It must send a message (call a method) to Object B, which validates and executes the request safely.*

---

## 1.3 The Core Concepts of OOP

OOP is formally defined by eight interlocking architectural pillars:

### 1. Objects
An **Object** is a basic runtime entity in an object-oriented system. It represents an instance of a user-defined class. Mechanically, an object resides in memory (either stack, heap, or static segment) and occupies a definite number of bytes determined by its non-static data members.
Every object has three core characteristics:
- **State**: The specific set of values held by its attributes/data members at any given time.
- **Behavior**: The set of actions and transformations it can perform, defined by its member functions.
- **Identity**: A unique identifier that distinguishes it from all other objects in the system, physically embodied by its unique memory address (`&object`).

### 2. Classes
A **Class** is a syntactical blueprint or template that specifies the attributes (data members) and operations (member functions) that objects instantiated from it will possess. A class is a **User-Defined Type (UDT)**. A class creates no physical memory for variables when declared; memory is allocated only when an instance (object) is constructed.

### 3. Data Abstraction
**Data Abstraction** refers to the act of representing essential features of an entity without including the background details or internal implementation complexities.
- **Interface vs. Implementation**: Abstraction establishes a clean boundary. A user interacts with an object strictly through its abstract interface (e.g., `stack.push(10)`, `stack.pop()`), completely oblivious to whether the stack is internally implemented using a dynamic array, a doubly linked list, or contiguous blocks.
- **Levels of Abstraction**: High-level code deals with what an operation accomplishes, whereas low-level internal code deals with how it accomplishes it.

### 4. Encapsulation & Data Hiding
- **Encapsulation**: The programmatic mechanism of wrapping data (variables) and code (functions) together into a single cohesive unit known as a Class.
- **Data Hiding**: The deliberate concealment of internal object components through access specifiers (`private` / `protected`) to prevent direct, unmediated outside access.
- *Distinction*: Encapsulation is the *containerization* of data and behavior; Data Hiding is the *security barrier* enforced within that container. Data hiding is achieved via encapsulation, but encapsulation also groups public interfaces.

### 5. Inheritance
**Inheritance** is the mechanism by which one class (the Derived or Child class) acquires the properties, attributes, and behaviors of another class (the Base or Parent class).
- It models the hierarchical **"Is-A" relationship** (e.g., a `Dog` *is a* `Mammal`, which *is an* `Animal`).
- **Code Reusability**: Common functionality is written, debugged, and optimized once in the base class. Derived classes inherit this code without modification and can specialize or extend it.
- **Transitivity**: If Class C inherits from Class B, and Class B inherits from Class A, then Class C transitively inherits attributes and methods of Class A.

### 6. Polymorphism
Derived from the Greek *poly* (many) and *morph* (forms), **Polymorphism** is the capability of a single entity (such as a function name or operator symbol) to behave differently based on the context or the underlying type of the object invoking it.
- **Compile-Time Polymorphism (Static / Early Binding)**: Resolved by the compiler during code translation. Implemented via **Function Overloading**, **Operator Overloading**, and **Templates**.
- **Run-Time Polymorphism (Dynamic / Late Binding)**: Resolved at runtime based on the actual object type pointed to by a pointer or reference. Implemented via **Virtual Functions** and inheritance hierarchies.

### 7. Dynamic Binding (Late Binding)
**Binding** refers to the association of a procedure call to the physical address of the executable code to be executed in response to the call.
- In **Static Binding**, the target function address is fixed at compile/link time.
- In **Dynamic Binding**, the target code address is resolved dynamically at runtime using dispatch tables (VTABLEs). This ensures that calling `shape->draw()` invokes `Circle::draw()` if `shape` points to a `Circle` object, and `Square::draw()` if it points to a `Square` object.

### 8. Message Passing
In pure object-oriented theory, execution proceeds by objects sending and receiving messages.
A message consists of:
1. The **destination object** receiving the request.
2. The **name of the operation / method** to be invoked.
3. The **arguments / parameters** required by the operation.
Syntax: `objectPointer->methodName(arg1, arg2);`

---

## 1.4 Benefits and Applications of OOP

### Quantitative Benefits of OOP
1. **Elimination of Redundant Code**: Inheritance allows code reuse across domain families, reducing bug surfaces.
2. **Modular Architecture & High Maintainability**: Objects are decoupled. Bug fixes within class internals do not break external client code as long as public interfaces remain stable.
3. **Data Integrity & Robust Security**: Sensitive state variables cannot be altered without passing through validating member functions.
4. **Natural Parallelism & Software Scaling**: Objects can be mapped naturally to concurrent tasks or distributed micro-entities.

### Primary Applications
- **System Software & Operating Systems**: Modern kernel abstractions (Windows NT object manager, modern macOS Mach/BSD drivers).
- **GUI Frameworks**: Windowing systems (Qt, wxWidgets, Windows Win32/MFC) inherently map UI widgets (Buttons, TextBoxes, Canvas) to class inheritance trees.
- **Computer Graphics, Simulation & Game Engines**: Unreal Engine, physics engines (PhysX), CAD/CAM modeling systems where 3D meshes, lights, and cameras are distinct polymorphic objects.
- **Database Management Systems**: Object-Relational Mapping (ORM) and Object-Oriented Databases (OODBMS).

---

## 1.5 Functions in C++: Deep Dive

### 1.5.1 The `main()` Function Structure
In C++, `main()` is the standard entry point of an executable program.
```cpp
int main(int argc, char* argv[]) {
    // Statements
    return 0; // Indicating success to the OS
}
```
- **Return Type**: Under ISO C++ standards, `main()` must return an `int`. Declaring `void main()` is strictly non-standard and rejected by modern conforming compilers.
- **Implicit Return**: If control reaches the end of `main()` without encountering a `return` statement, the compiler implicitly inserts `return 0;`.
- **Exit Codes**: Returning `0` or `EXIT_SUCCESS` signals normal, error-free termination to the host operating system. Returning a non-zero value or `EXIT_FAILURE` signals an error state.

### 1.5.2 Function Prototyping
A **function prototype** (forward declaration) declares the function’s interface to the compiler before its actual definition appears in the translation unit.
- **Syntax**: `ReturnType FunctionName(ParameterType1 param1, ParameterType2 param2, ...);`
- **Compiler Necessity**: C++ requires strong type checking. The prototype informs the compiler of the function's name, return type, number of parameters, and exact parameter types so the compiler can validate calls, perform necessary type promotions, and configure stack frames.
- Parameter variable names in the prototype are optional and ignored by the compiler (e.g., `int add(int, int);` is fully legal), though descriptive names improve header readability.

---

### 1.5.3 Inline Functions

#### Definition and Conceptual Goal
In standard C++, invoking a normal function introduces a definite execution overhead:
1. The caller pushes arguments onto the execution stack or loads them into architecture registers.
2. The current instruction pointer (`EIP`/`RIP`) is pushed onto the stack as the return address.
3. A branch/jump instruction transfers execution to the function’s entry point.
4. The callee allocates a local stack frame.
5. Upon completion, the stack frame is torn down, the return value is loaded into an accumulator register (`EAX`/`RAX`), and a `RET` instruction pops the return address to jump back.

For small functions (1–3 lines) executed millions of times inside tight loops, this invocation overhead can exceed the actual execution time of the function body.

An **Inline Function** is a function for which the compiler attempts to replace the function call directly with the exact machine code of the function body at every call site, completely eliminating the call-return overhead.

```cpp
inline int square(int x) {
    return x * x;
}
```

```
Normal Call Flow:
[Caller Code] ---> [Push Args] ---> [JUMP to square()] ---> [Compute] ---> [RET] ---> [Resume Caller]

Inlined Flow:
[Caller Code] ---> [Direct In-Place Computation: (x * x)] ---> [Resume Next Instruction]
```

#### The `inline` Keyword as a Compiler Request, Not a Command
Declaring a function `inline` is merely a **request** (a hint) to the optimizing compiler. The compiler's cost-model heuristics evaluate the trade-off between execution speed and binary code bloat. If the function is deemed too complex, the compiler silently ignores the request and compiles the function as a normal out-of-line subroutine.

#### Strict Conditions Where Inlining Is Typically Ignored by Compilers:
1. **Presence of Loops**: Functions containing `for`, `while`, or `do-while` loops.
2. **Presence of Recursion**: A function that calls itself cannot be infinitely inlined at compile time.
3. **Presence of Complex Control Flow**: Heavy `switch` statements or multiple `goto` labels.
4. **Presence of Static Variables**: Functions containing `static` local variables.
5. **Taking the Address of the Function**: If any part of the program takes a pointer to the function (`&func`), the compiler is forced to generate a physical out-of-line machine address for it.
6. **Large Function Body**: Functions exceeding a certain threshold of statements or intermediate assembly instructions (which would trigger severe instruction cache thrashing and code bloat).

> **Viva / Exam Pitfall**: Inline functions vs. Preprocessor Macros (`#define`):
> Macros do not obey C++ scope rules, perform zero type-checking, and cause infamous side-effect evaluation bugs (e.g., `#define SQ(x) ((x)*(x))` evaluated on `SQ(i++)` increments `i` twice). Inline functions provide full type safety, scope rules, and debuggability while retaining macro speed.

---

### 1.5.4 Reference Variables

A **Reference Variable** provides an alternative name (an alias) for an already existing variable.

#### Syntax & Core Rules
```cpp
int a = 10;
int& ref = a; // 'ref' is now an alias for 'a'
```
1. **Mandatory Initialization**: A reference **must be initialized** at the exact moment of declaration. `int& r;` is a fatal compilation error.
2. **Immutable Binding**: Once a reference is bound to a specific variable, it **cannot be reseated** to refer to another variable. Any subsequent assignment `ref = b;` does NOT rebind `ref`; it copies the value of `b` into the variable `a` that `ref` aliases!
3. **No Null References**: A reference cannot refer to `nullptr` or null memory. It must always bind to a valid object.
4. **Shared Identity**: `&ref` and `&a` yield the exact same memory address.

#### Internal Implementation Mechanism
To the developer, a reference behaves like an alias. Under the hood, however, standard C++ compilers implement reference variables as **constant pointers with automatic dereferencing**:
```cpp
int a = 10;
int& ref = a;       // Conceptually
int* const ptr = &a;// Compiler's internal machine-level implementation!
ref = 20;           // Becomes: *ptr = 20;
```

#### Detailed Comparison: Pointers vs. Reference Variables

| Dimension | Pointer (`Type*`) | Reference (`Type&`) |
|---|---|---|
| **Definition** | A distinct variable holding the memory address of another variable. | An alias/alternate identifier for an existing variable. |
| **Initialization** | Can be left uninitialized (`int* p;` contains garbage/wild pointer). | **Must** be initialized upon declaration (`int& r = x;`). |
| **Nullability** | Can be assigned `nullptr` or `NULL` to indicate absence of target. | Cannot be null. Must always refer to valid storage. |
| **Reassignment** | Can be reassigned to point to different memory addresses at any time. | Bound permanently to its initial target; cannot be rebound. |
| **Memory Address** | Has its own distinct memory address (`&p != &target`). | Shares the identical memory address of its target (`&r == &target`). |
| **Dereference Syntax**| Requires explicit indirection operator `*` or `->` (`*p = 5;`). | Uses direct variable access syntax transparently (`r = 5;`). |
| **Arithmetic** | Supports pointer arithmetic (`p++`, `p + 4`, indexing `p[i]`). | No arithmetic operations on the reference itself. |
| **Indirection Levels**| Supports multiple levels of indirection (`int**`, `int***`). | Cannot have a reference to a reference (`int&&` denotes an rvalue reference, not multiple indirection). |

#### The Fatal Trap: Dangling References
Returning a reference to a local variable allocated on the function's stack frame produces **Undefined Behavior (UB)**. When the function returns, its stack frame is popped/invalidated. The returned reference points to deallocated stack memory that will be overwritten by subsequent function calls.

```cpp
// ❌ FATAL RUNTIME BUG: Returning reference to local variable
int& getLocalVariable() {
    int localVal = 100;
    return localVal; // Compiler warning: reference to local variable returned
}

int main() {
    int& ref = getLocalVariable(); // ref binds to dead stack memory
    std::cout << ref << std::endl; // Might print 100, or garbage, or crash!
    // Any intervening function call will overwrite this memory address!
}
```

---

### 1.5.5 Parameter Passing: Value vs. Reference vs. Address (Pointer)

Parameter passing mechanisms determine how arguments are communicated from the caller to the callee.

```
1. Call by Value:
   Caller Memory [ a = 5 ]  ----(Copy Value)---->  Callee Stack [ x = 5 ]
   * Callee modifies 'x'. Caller's 'a' remains unchanged at 5.

2. Call by Address (Pointer):
   Caller Memory [ a = 5 ] (Addr: 0x1000)
         ^
         | (Points to 0x1000)
   Callee Stack [ ptr = 0x1000 ]
   * Callee executes *ptr = 10. Memory at 0x1000 is updated directly!

3. Call by Reference:
   Caller Memory [ a = 5 ] (Addr: 0x1000)
         ^
         | (Alias: ref is another name for 0x1000)
   Callee Frame [ ref ]
   * Callee executes ref = 10. Memory at 0x1000 is updated directly!
```

#### Comparative Implementation: The Canonical Swap Problem

```cpp
#include <iostream>

// 1. Call by Value (Fails to swap caller variables)
void swapByValue(int x, int y) {
    int temp = x;
    x = y;
    y = temp;
} // x and y destroyed here; caller's variables completely unaffected

// 2. Call by Address / Pointer (Successfully swaps caller variables)
void swapByPointer(int* x, int* y) {
    if (x == nullptr || y == nullptr) return; // Null check safety
    int temp = *x;
    *x = *y;
    *y = temp;
}

// 3. Call by Reference (Cleanest, most idiomatic C++ syntax)
void swapByReference(int& x, int& y) {
    int temp = x;
    x = y;
    y = temp;
}

// 4. The "Pointer Swap Failure" Trap (from Mid-Sem & Quiz 2!)
void badPointerSwap(int* a, int* b) {
    int* temp = a;
    a = b;
    b = temp;
} // Only the local pointer variables 'a' and 'b' on the stack were swapped!
  // The actual integer values in caller memory remained untouched!
```

#### Pass-by-Value vs. Pass-by-Reference Scenarios (Exam Question 3a Analysis)
- **When Pass-by-Value is More Beneficial**:
  1. Primitive, lightweight data types (`int`, `char`, `float`, `double`) where the cost of copying (4–8 bytes) is equal to or less than passing an address.
  2. When the callee *requires* an independent, isolated working copy that it modifies destructively without altering the caller's state.
  3. Avoidance of aliasing hazards and unintended side-effects across concurrent threads.
- **When Pass-by-Reference (especially `const &`) is More Beneficial**:
  1. Large user-defined class objects, complex structs, strings, or large standard containers (`std::vector`). Passing by value invokes the **copy constructor**, allocating heap memory and copying every member (expensive O(N) operation). Passing by reference is O(1) (passing an 8-byte pointer under the hood).
  2. When the caller explicitly expects the function to mutate the original argument (output parameters).
  3. Enabling runtime polymorphism: Passing derived objects to base class parameters requires references or pointers to prevent **Object Slicing**.

---

### 1.5.6 Default Arguments

A **Default Argument** is a value provided in the function declaration that is automatically assigned by the compiler if the calling code omits that specific argument.

#### Syntax and Grammar Rules
```cpp
void displayMessage(std::string msg, int count = 1, bool newline = true);
```
1. **Right-to-Left Precedence Rule**: Default arguments **must be added from right to left**. Once a parameter has a default argument, all parameters to its right must also have default arguments.
   ```cpp
   // ❌ ILLEGAL (Compilation Error)
   void func(int a, int b = 10, int c); // Error: parameter 'c' must have default
   
   // ✅ LEGAL
   void func(int a, int b = 10, int c = 20); // Rightmost parameters have defaults
   void func(int a, int b, int c = 20);      // Rightmost parameter has default
   ```
2. **Declaration vs. Definition Placement**: Default arguments should be specified in the **function declaration (prototype)**, typically in the header file, and **MUST NOT be repeated in the function definition**.
   ```cpp
   // Header / Prototype:
   void calculate(int x, int y = 100);

   // Source / Implementation:
   void calculate(int x, int y) { // Notice: NO '= 100' here!
       std::cout << x + y;
   }
   ```
   *Repeating default values in both prototype and definition causes a compilation error: "redefinition of default argument".*
3. **Cannot Skip Arguments at the Call Site**: If a function takes three default arguments, the caller cannot skip the second and provide only the first and third:
   ```cpp
   void plot(int x = 0, int y = 0, int z = 0);
   plot(10, , 30); // ❌ SYNTAX ERROR! C++ does not support skipping parameters.
   ```

---

### 1.5.7 Constant Arguments

Passing arguments with the `const` qualifier enforces immutability.

#### The Idiomatic C++ Pattern: `const Type&`
```cpp
void printStudentRecord(const Student& s) {
    // s.marks = 95.0; // ❌ COMPILE ERROR: Cannot modify through const reference!
    s.display();       // ✅ LEGAL: Only calls const member functions
}
```
- **Performance**: Zero-copy overhead (passes pointer under the hood).
- **Safety**: The compiler prevents accidental mutation of caller state.
- **Rvalue Binding**: In C++, a non-const lvalue reference (`Type&`) *cannot* bind to a temporary value (rvalue). However, a **const lvalue reference (`const Type&`) can bind to temporary objects / literals**:
  ```cpp
  void process(int& x);
  process(10); // ❌ COMPILE ERROR: Cannot bind non-const lvalue reference to rvalue

  void processConst(const int& x);
  processConst(10); // ✅ LEGAL: Compiler creates temporary int holding 10!
  ```

---

## 1.6 Function Overloading: Principles and Overload Resolution

**Function Overloading** allows multiple functions in the same scope to share the identical identifier (name), provided their parameter lists (signatures) are distinguishable by the compiler.

### Core Principles
1. **Differentiating Criteria**: Overloaded functions must differ in:
   - Number of parameters.
   - Types of parameters.
   - Sequence/order of parameter types (e.g., `(int, double)` vs. `(double, int)`).
2. **Return Type Is Irrelevant**: Functions *cannot* be overloaded based solely on return type.
   ```cpp
   int calculate(int a);
   double calculate(int a); // ❌ COMPILE ERROR: Redefinition of calculate(int)
   ```
   *Reason*: When a function is called as a statement (`calculate(5);`), the compiler cannot determine from the call site which return type is expected.

### Name Mangling (Name Decoration)
At the assembly and binary level, linkers require unique symbol names. The C++ compiler generates unique internal names by encoding parameter types into the function symbol:
```cpp
void display(int x);       // Mangled name: _Z7displayi
void display(double x);    // Mangled name: _Z7displayd
void display(int x, int y);// Mangled name: _Z7displayii
```

---

### The Overload Resolution Hierarchy (Step-by-Step Rules)

When resolving an overloaded function call `func(arg1, arg2)`, the compiler executes a strict 5-stage matching process:

```
[Function Call: func(args)]
             |
             v
   [Stage 1: Exact Match?] -------- YES ------> [Invoke Exact Function]
             | NO
             v
   [Stage 2: Promotion?] ---------- YES ------> [Invoke Promoted Function]
             | NO
             v
   [Stage 3: Standard Conversion?] - YES ------> [Invoke Converted Function]
             | NO
             v
   [Stage 4: User-Defined Conv.?] - YES ------> [Invoke User-Converted Function]
             | NO
             v
   [Stage 5: Ellipsis (...) Match?] - YES ----> [Invoke Variadic Function]
             | NO
             v
   [COMPILATION ERROR: No Matching Function Found]
```

#### Detailed Breakdown of Stages:
1. **Stage 1: Exact Match**:
   - Parameter types match argument types exactly without modification.
   - Includes trivial conversions: Array-to-pointer decay (`int[]` -> `int*`), Function-to-pointer decay, and qualification adjustment (non-const to const).
2. **Stage 2: Integral & Floating-Point Promotions**:
   - `char`, `signed char`, `unsigned char`, `short`, and `bool` promote to `int` (or `unsigned int`).
   - `float` promotes to `double`.
3. **Stage 3: Standard Conversions**:
   - Numeric conversions: `int` -> `double`, `double` -> `int`, `long` -> `float`.
   - Pointer conversions: Derived pointer to Base pointer (`Derived*` -> `Base*`), any pointer to `void*`, `0`/`nullptr` to any pointer.
4. **Stage 4: User-Defined Conversions**:
   - Single-argument constructors and user-defined conversion operators (`operator Type()`).
5. **Stage 5: Ellipsis Match**:
   - Variadic functions matching `...`.

---

### Overload Ambiguity Traps (High Exam Probability)

#### Trap 1: Ambiguity Induced by Default Arguments
```cpp
void print(int a) { std::cout << a << std::endl; }
void print(int a, int b = 50) { std::cout << a + b << std::endl; }

int main() {
    print(10); // ❌ COMPILE ERROR: Call to 'print' is ambiguous!
    // Compiler cannot decide between print(int) and print(int, 50).
}
```

#### Trap 2: Floating-Point Literal Ambiguity
```cpp
void compute(float f) { std::cout << "Float: " << f; }
void compute(long double ld) { std::cout << "Long Double: " << ld; }

int main() {
    compute(3.14); // ❌ COMPILE ERROR: Call to 'compute' is ambiguous!
    // Why? In C++, '3.14' is a 'double' literal by default.
    // Converting double -> float is a standard conversion.
    // Converting double -> long double is ALSO a standard conversion.
    // Neither is preferred; both belong to Stage 3.
    // FIX: compute(3.14f); // Exact match with float!
}
```

#### Trap 3: Character Promotion vs. Double Conversion
```cpp
void test(int x)    { std::cout << "Int: " << x; }
void test(double x) { std::cout << "Double: " << x; }

int main() {
    test('A'); // ✅ PRINTS: "Int: 65"
    // Why? 'char' -> 'int' is an INTEGRAL PROMOTION (Stage 2).
    // 'char' -> 'double' is a STANDARD CONVERSION (Stage 3).
    // Promotion (Stage 2) beats Conversion (Stage 3)!
}
```

---

## 1.7 Math Library Functions in `<cmath>`

The `<cmath>` header provides mathematical operations. All functions operate primarily on `double`, `float`, and `long double`.

| Function Prototype | Mathematical Operation | Example Usage | Output / Behavior |
|---|---|---|---|
| `double sqrt(double x)` | Computes square root of x | `sqrt(25.0)` | `5.0` (Domain error if x < 0, returns `NaN`) |
| `double pow(double b, double e)` | Computes power b^e | `pow(2.0, 8.0)` | `256.0` |
| `double ceil(double x)` | Smallest integer >= x | `ceil(4.2)` / `ceil(-4.8)` | `5.0` / `-4.0` |
| `double floor(double x)` | Largest integer <= x | `floor(4.8)` / `floor(-4.2)` | `4.0` / `-5.0` |
| `double round(double x)` | Rounds to nearest integer | `round(4.5)` / `round(4.4)` | `5.0` / `4.0` (Halfway cases rounded away from 0) |
| `double trunc(double x)` | Truncates fractional part | `trunc(4.9)` / `trunc(-4.9)`| `4.0` / `-4.0` |
| `double fabs(double x)` | Absolute value of floating-point | `fabs(-12.34)` | `12.34` |
| `double fmod(double x, double y)` | Floating-point remainder x - n*y | `fmod(5.3, 2.0)` | `1.3` (5.3 = 2 * 2.0 + 1.3) |
| `double sin(double rad)` | Trigonometric sine (radians) | `sin(3.14159 / 2)` | ~1.0 |
| `double cos(double rad)` | Trigonometric cosine (radians)| `cos(0.0)` | `1.0` |
| `double tan(double rad)` | Trigonometric tangent (radians)| `tan(3.14159 / 4)` | ~1.0 |
| `double log(double x)` | Natural logarithm ln(x) (base e)| `log(2.71828)` | ~1.0 (x > 0) |
| `double log10(double x)` | Common logarithm log10(x) | `log10(1000.0)` | `3.0` |
| `double exp(double x)` | Exponential function e^x | `exp(1.0)` | ~2.71828 |
| `double hypot(double x, double y)`| Hypotenuse sqrt(x^2 + y^2) | `hypot(3.0, 4.0)` | `5.0` (Avoids intermediate overflow) |

---

## 1.8 Unit 1 High-Probability Exam Questions & Review Points

1. **"Explain how encapsulation ensures data security. Should all attributes be public and methods private to achieve encapsulation?" (End-Sem 2024, Q1a)**
   - *Model Answer Summary*: Encapsulation bundles data and member functions. Data security is guaranteed by marking attributes `private`, forcing external access through validating `public` methods (getters/setters). If all attributes were `public` and methods `private`, data would be completely exposed to arbitrary external corruption without any way for the object to perform its operations—violating both data hiding and encapsulation.
2. **"Consider `void example(int x, int y = 5, int z);`. Explain the issue and how to correct it." (End-Sem 2024, Q1b)**
   - *Model Answer Summary*: Violates the Right-to-Left Rule for default arguments. In C++, once a parameter has a default value, all following parameters to its right must have defaults. Correction 1: `void example(int x, int y, int z = 5);` (default only rightmost). Correction 2: `void example(int x, int y = 5, int z = 10);` (provide default for `z`). Correction 3: Reorder parameters: `void example(int x, int z, int y = 5);`.
3. **"Can inline functions have static variables?" (Mid-Sem Exam Question)**
   - *Model Answer Summary*: In standard C++, an inline function is legally permitted to have static local variables. However, all inlined expansions across all translation units will share the exact same single static variable instance. In practice, compilers often refuse to inline functions with local static variables to prevent storage duplication hazards.



---

# UNIT 2: Classes, Objects, Memory Architecture & Friendship

---

## 2.1 Specifying a Class

A **Class** in C++ is a user-defined compound type that encapsulates state (data members) and operations (member functions). It establishes an Abstract Data Type (ADT) that binds attributes to the algorithms that manipulate them.

### General Syntax of Class Specification
```cpp
class ClassName {
    private:
        // Variables and functions accessible ONLY within this class
        // Default access mode in C++ classes
        int privateData;
        void privateHelperMethod();

    protected:
        // Variables and functions accessible within this class
        // and its derived (child) classes
        int protectedData;

    public:
        // Variables and functions accessible from anywhere in the program
        // forms the public interface of the class
        void setValues(int val);
        int getValues() const;
}; // Note: Semicolon is syntactically mandatory
```

### Access Specifiers: The Triple Partition

C++ enforces data hiding and interface segregation through three access specifiers:

| Access Specifier | Accessibility Within Same Class | Accessibility in Derived (Sub) Class | Accessibility from Outside World (Client Code) |
|---|---|---|---|
| `private` | **YES** | **NO** (Inaccessible directly) | **NO** (Compile-time access violation) |
| `protected` | **YES** | **YES** (Inherited accessibility) | **NO** (Compile-time access violation) |
| `public` | **YES** | **YES** | **YES** (Unrestricted via object instance) |

#### Core Rules of Access Specifiers:
1. **Default Visibility**: If no access specifier is explicitly stated at the beginning of a `class` body, all members default to **`private`**.
2. **Order and Repetition**: Access specifiers can appear in any order and may be repeated multiple times within the class body.
3. **Compile-Time Enforcement**: Access control in C++ is checked entirely at **compile time**. It incurs zero runtime execution overhead.

---

## 2.2 Difference Between C Structure (`struct`) and C++ Class

In C++, both `struct` and `class` define compound types with member functions, constructors, destructors, and inheritance. However, they possess crucial syntactical defaults and architectural distinctions.

### Comprehensive Comparison Table

| Feature / Dimension | C Structure (`struct` in C) | C++ Structure (`struct` in C++) | C++ Class (`class` in C++) |
|---|---|---|---|
| **Default Member Access** | Always `public` (C has no access specifiers). | **`public`** by default. | **`private`** by default. |
| **Default Inheritance Mode** | Inheritance not supported in C. | **`public`** inheritance by default (`struct D : B`). | **`private`** inheritance by default (`class D : B`). |
| **Member Functions / Methods**| Cannot contain functions (only function pointers). | Fully supports member functions, constructors, destructors. | Fully supports member functions, constructors, destructors. |
| **Data Hiding & Security** | None. All members are exposed globally. | Supported, but requires explicit `private:` label. | Enforced by default; encapsulates and hides state. |
| **Polymorphism & Virtuals** | Not supported. | Fully supports `virtual` functions, VTABLEs, and abstract types. | Fully supports `virtual` functions, VTABLEs, and abstract types. |
| **Idiomatic Industry Usage** | Grouping heterogeneous data records. | Used for **Plain Old Data (POD)** structs or data-only DTOs. | Used for encapsulated entities with complex state and invariants. |

#### Demonstrating Default Inheritance Difference:
```cpp
class Base { public: int x; };

struct DerivedStruct : Base { }; // Inherits Base as PUBLIC by default!
class DerivedClass   : Base { }; // Inherits Base as PRIVATE by default!

int main() {
    DerivedStruct s;
    s.x = 10; // ✅ LEGAL: Base::x remains public in DerivedStruct

    DerivedClass c;
    // c.x = 10; // ❌ COMPILE ERROR: Base::x became private in DerivedClass!
}
```

---

## 2.3 Member Functions: Inline, Scope Resolution & Nesting

Member functions implement the behaviors of a class. They can access all data members of their class directly, regardless of access specifiers.

### 2.3.1 Defining Member Functions: Inside vs. Outside Class

#### 1. Inside Class Definition (Implicit Inlining)
Any member function whose complete definition is written directly inside the class body is **implicitly treated as an `inline` function** by the compiler:
```cpp
class MathOperations {
public:
    int cube(int n) { // Implicitly inline!
        return n * n * n;
    }
};
```
- **Advantages**: Convenient for short, 1-to-2 line getters, setters, or mathematical primitives.
- **Disadvantages**: Clutters the class header; large bodies increase compilation dependencies and cause binary bloat.

#### 2. Outside Class Definition (Scope Resolution Operator `::`)
When separating class interface from implementation, member functions are prototyped inside the class and defined outside using the **Scope Resolution Operator (`::`)**:
```cpp
class BankAccount {
private:
    double balance;
public:
    void deposit(double amount); // Prototype inside
};

// Definition outside the class:
// Syntax: ReturnType ClassName::FunctionName(ParameterList)
void BankAccount::deposit(double amount) {
    if (amount > 0) {
        balance += amount;
    }
}
```
- **The Role of `::`**: The scope resolution operator informs the compiler that `deposit` does not belong to the global namespace, but is an authorized member of `BankAccount`, granting it access to `balance`.
- **Explicit Inlining**: An out-of-line definition can be requested to be inline by prepending the `inline` keyword to the definition:
  ```cpp
  inline void BankAccount::deposit(double amount) { balance += amount; }
  ```

---

### 2.3.2 Nesting of Member Functions

In C++, a member function can invoke another member function of the **same class directly without using an object identifier or the dot operator**. This architectural pattern is called **Nesting of Member Functions**.

```cpp
#include <iostream>

class NumberAnalyzer {
private:
    int num1, num2;

    // Private member function: Helper routine
    int findMax() {
        return (num1 > num2) ? num1 : num2;
    }

public:
    void readData(int a, int b) {
        num1 = a;
        num2 = b;
    }

    void displayLargest() {
        // Direct nested call to another member function!
        int largest = findMax(); 
        std::cout << "The largest number is: " << largest << std::endl;
    }
};
```

### 2.3.3 Private Member Functions (Utility / Helper Methods)
Not all member functions belong in the public interface. A **Private Member Function** can only be called by other member functions of the same class (or friend functions/classes).
- **Primary Use Cases**:
  1. Internal validation routines (e.g., validating password complexity or credit card checksums before saving).
  2. Factoring out duplicated logic from multiple public member functions.
  3. Preventing outside code from triggering dangerous intermediate internal state transitions.

---

## 2.4 Internal Memory Allocation for Objects

A critical concept frequently tested in university examinations is: **How is memory physically partitioned between objects and their member functions?**

### The Core Architectural Principle
- **Member Functions**: When a class is compiled, its member functions are translated into machine instructions and loaded into the **Code Segment (Text Segment)** of memory **EXACTLY ONCE**. Regardless of whether zero, one, or ten thousand objects of that class are instantiated, only a single copy of each member function exists in memory!
- **Data Members**: Every time an object is instantiated, a distinct block of memory is allocated in the **Stack**, **Heap**, or **Data Segment** exclusively for that object's **non-static data members**.

### Architectural Memory Allocation Layout Diagram

```
+========================================================================+
|                    CODE SEGMENT (SHARED READ-ONLY)                     |
|                                                                        |
|   void Student::setData(int, float)  [Address: 0x00401000]             |
|   void Student::display()            [Address: 0x00401080]             |
|   float Student::computeAverage()    [Address: 0x00401120]             |
+========================================================================+
       ^                                  ^                  ^
       |                                  |                  |
       | (Hidden 'this' = 0x1000)         | (this = 0x1010)  | (this = 0x1020)
       |                                  |                  |
+---------------------+          +---------------------+    +---------------------+
|      Object s1      |          |      Object s2      |    |      Object s3      |
|  [Address: 0x1000]  |          |  [Address: 0x1010]  |    |  [Address: 0x1020]  |
| +-----------------+ |          | +-----------------+ |    | +-----------------+ |
| | rollNo: 101     | |          | | rollNo: 102     | |    | | rollNo: 103     | |
| | marks: 88.5     | |          | | marks: 92.0     | |    | | marks: 74.5     | |
| +-----------------+ |          | +-----------------+ |    | +-----------------+ |
| Size: 8 bytes       |          | Size: 8 bytes       |    | Size: 8 bytes       |
+---------------------+          +---------------------+    +---------------------+
```

### Determining Object Size (`sizeof` Rules & Memory Alignment)
1. **Formula**: `sizeof(Object) = Sum of sizes of non-static data members + Padding bytes for memory alignment`.
2. **Exclusion of Functions**: Ordinary member functions do **not** contribute to the `sizeof` an object because they reside in the code segment.
3. **The Empty Class Rule**: An empty class (`class Empty {};`) has a size of **1 byte**, never 0 bytes!
   - *Reason*: Under ISO C++, every distinct object must have a unique memory address. If `sizeof(Empty)` were 0, creating an array `Empty arr[5];` would mean all 5 objects would share the exact same address, violating object identity (`&arr[0] == &arr[1]`). The compiler allocates 1 dummy byte to ensure address uniqueness.
4. **Data Alignment & Padding**: Compilers align data on natural word boundaries (e.g., 4-byte or 8-byte boundaries) for hardware CPU bus efficiency, inserting invisible padding bytes between members.

---

## 2.5 Arrays Within a Class

A class can contain array variables as its data members. This is typical when an object represents an aggregate entity containing a list of sub-items (e.g., a student's marks across 5 subjects, or a shopping cart item list).

```cpp
#include <iostream>

class StudentReport {
private:
    int rollNumber;
    static const int NUM_SUBJECTS = 5;
    float marks[NUM_SUBJECTS]; // Array as a data member

public:
    void input(int roll) {
        rollNumber = roll;
        std::cout << "Enter marks for " << NUM_SUBJECTS << " subjects: ";
        for (int i = 0; i < NUM_SUBJECTS; ++i) {
            std::cin >> marks[i];
        }
    }

    float calculateTotal() const {
        float sum = 0.0f;
        for (int i = 0; i < NUM_SUBJECTS; ++i) {
            sum += marks[i];
        }
        return sum;
    }
};
```

---

## 2.6 Array of Objects

An **Array of Objects** is a collection of multiple object instances of the same class stored contiguously in memory.

### Declaration and Memory Representation
```cpp
StudentReport batch[3]; // Allocates memory for 3 consecutive StudentReport objects
```

#### Contiguous Memory Layout
```
+-----------------------------------+-----------------------------------+-----------------------------------+
|             batch[0]              |             batch[1]              |             batch[2]              |
| rollNumber (4B) | marks[0..4](20B)| rollNumber (4B) | marks[0..4](20B)| rollNumber (4B) | marks[0..4](20B)|
+-----------------------------------+-----------------------------------+-----------------------------------+
[Address: 0x2000]                   [Address: 0x2018]                   [Address: 0x2030]
```
- Total memory consumed = $3 \times \text{sizeof}(\text{StudentReport}) = 3 \times 24 = 72 \text{ bytes}$.
- **Constructor Invocations**: When `batch[3]` is declared, the **default constructor is invoked automatically 3 times**, once for each element in ascending index order (`batch[0]`, then `batch[1]`, then `batch[2]`).
- **Parameterized Initialization**:
  ```cpp
  class Complex {
      double real, imag;
  public:
      Complex(double r, double i) : real(r), imag(i) {}
  };

  Complex arr[3] = { Complex(1.0, 2.0), Complex(3.0, 4.0), Complex(5.0, 6.0) };
  ```

---

## 2.7 Static Data Members

A **Static Data Member** is a class variable that is shared by all objects of the class. It possesses class scope rather than object scope.

### Core Characteristics of Static Data Members
1. **Single Instance**: Only one copy of the static data member exists for the entire class, regardless of how many objects are instantiated.
2. **Shared State**: All instances access and modify the exact same physical memory cell.
3. **Storage Location**: Stored in the **Global / Static Data Segment** of memory, NOT inside any individual object's stack or heap footprint.
4. **Lifetime**: Initialized when the program begins execution and persists until the program completely terminates.
5. **Default Initialization**: Automatically initialized to zero (`0`, `0.0`, or `nullptr`) if not explicitly initialized.

### Declaration vs. Definition (Mandatory Academic Rule)
In C++, declaring a static data member inside the class **only declares its name and type**; it does NOT allocate memory for it. **It must be explicitly defined outside the class in file scope to allocate physical memory.**

```cpp
class ServerConnection {
private:
    int connectionID;
    static int activeConnections; // 1. Declaration inside class

public:
    ServerConnection(int id) : connectionID(id) {
        activeConnections++;
    }
    ~ServerConnection() {
        activeConnections--;
    }
};

// 2. Mandatory definition outside class at file scope:
// Syntax: DataType ClassName::VariableName = InitialValue;
int ServerConnection::activeConnections = 0; // Memory physically allocated here!
```
*Failure to provide the external definition results in an unresolved external symbol linker error (`LNK2001` / `undefined reference`).*

---

## 2.8 Static Member Functions

A **Static Member Function** is a member function that acts upon the class as a whole, rather than on a specific object instance.

### Core Characteristics & Rules
1. **Invocation Without Object**: Can be called directly using the class name and scope resolution operator:
   `ClassName::staticFunction();`
2. **Restriction 1: NO `this` Pointer**: A static member function does **not** receive an implicit `this` pointer argument.
3. **Restriction 2: Access Limitations**: A static member function **can ONLY directly access static data members and call other static member functions** of that class. It cannot access non-static data members or non-static member functions directly.

---

### In-Depth Justification: Why Static Member Functions Cannot Access Non-Static Data Members (End-Sem 2024 Exam Question 2a)

> **Academic Rigorous Justification**:
> In C++, every ordinary (non-static) member function has an invisible, implicit first parameter passed to it by the compiler: the **`this` pointer** (`ClassName* const this`), which holds the unique memory address of the specific object instance invoking the method:
> ```cpp
> void display()  ===>  void display(ClassName* const this)
> ```
> When an ordinary member function accesses a non-static attribute `x`, the compiler translates this to `this->x`.
>
> In contrast, a **Static Member Function** has class-level scope and can be invoked **independently of any object instance** (`ClassName::method()`). Consequently, the compiler passes **NO `this` pointer** to static member functions.
>
> If a static member function were permitted to write `balance = 500;`, the runtime would have no mechanism to determine **which specific object instance's balance** in memory should be updated. Because non-static data members require a concrete object instance and a valid `this` pointer to locate their offset in memory, attempting to access non-static members inside a static member function is fundamentally impossible and prohibited at compile-time.

#### Practical Object Tracker Implementation (Past Paper Favorite):
```cpp
#include <iostream>

class InstanceCounter {
private:
    int objectID;
    static int totalCount; // Static data member

public:
    InstanceCounter() {
        totalCount++;
        objectID = totalCount;
        std::cout << "Constructed Object ID: " << objectID << std::endl;
    }

    ~InstanceCounter() {
        std::cout << "Destroying Object ID: " << objectID << std::endl;
        totalCount--;
    }

    // Static member function
    static void printTotalActive() {
        // Legal: Accesses static data member
        std::cout << "Currently Active Objects: " << totalCount << std::endl;
        
        // Illegal:
        // std::cout << objectID; // ❌ COMPILE ERROR: invalid use of member 'objectID' in static member function
    }
};

// Allocation of memory in data segment:
int InstanceCounter::totalCount = 0;

int main() {
    InstanceCounter::printTotalActive(); // Output: 0

    InstanceCounter obj1;
    InstanceCounter obj2;
    InstanceCounter::printTotalActive(); // Output: 2

    {
        InstanceCounter obj3;
        InstanceCounter::printTotalActive(); // Output: 3
    } // obj3 destroyed here

    InstanceCounter::printTotalActive(); // Output: 2
    return 0;
}
```

---

## 2.9 Friend Functions and Friend Classes

Under strict encapsulation, private members of a class cannot be accessed by any outside function. However, certain legitimate programming scenarios (such as operator overloading for stream I/O or tightly coupled mathematical bridges) require controlled, explicit access. C++ provides this mechanism via the **`friend`** keyword.

### 2.9.1 Friend Functions: Definition, Syntax and Rules

A **Friend Function** is a non-member function that is granted full access to the `private` and `protected` members of the class that declares it as a friend.

#### Syntax & Implementation
```cpp
#include <iostream>

class Box {
private:
    double length;

public:
    Box(double l) : length(l) {}

    // Friend function declaration inside class:
    friend void printBoxLength(const Box& b);
};

// Definition OUTSIDE class:
// 1. NO 'friend' keyword in definition!
// 2. NO 'Box::' scope resolution operator! (It is NOT a member!)
void printBoxLength(const Box& b) {
    // Directly accesses private member 'length'
    std::cout << "Box Length: " << b.length << std::endl;
}

int main() {
    Box b1(45.5);
    // Invocation: Called like a regular global C++ function, NOT via dot operator!
    printBoxLength(b1); // ✅ LEGAL
    // b1.printBoxLength(b1); // ❌ COMPILE ERROR: Not a member of Box!
}
```

#### The 6 Inviolable Rules and Characteristics of Friend Functions:
1. **Non-Member Status**: A friend function is not a member of the class. It resides in the enclosing namespace.
2. **Invocation Mechanism**: It cannot be called using the object dot operator (`object.friendFunc()` is a syntax error). It is invoked as a standard global function, taking objects as arguments.
3. **Arbitrary Placement**: The `friend` declaration can be placed under `private:`, `protected:`, or `public:` sections within the host class—its meaning and access privileges remain identical.
4. **No Implicit `this` Pointer**: Because it is not a member function, it receives no `this` pointer. It must access private members explicitly through an object parameter passed to it.
5. **Non-Symmetric (Non-Mutual)**: Friendship is granted, not taken. If Class A declares function `F` as a friend, `F` can access `A`. But `A` has no special access to anything inside `F`.
6. **Non-Inherited & Non-Transitive**: Friendship is not inherited by child classes, nor does it carry over transitively.

---

### 2.9.2 Friend Classes

A class can declare an entire external class as a friend:
```cpp
class Screen; // Forward declaration

class WindowManager {
public:
    void maximize(Screen& s);
    void minimize(Screen& s);
};

class Screen {
private:
    int width, height;

    // Grant entire class WindowManager full friend access:
    friend class WindowManager;
};

// Now ALL member functions of WindowManager have access to Screen's private members!
void WindowManager::maximize(Screen& s) {
    s.width = 1920;
    s.height = 1080;
}
```

---

### 2.9.3 The Transitivity Trap: Analysis of End-Sem 2024 Exam Question 3b

> **The Question**:
> *"Consider two classes, A and B. Class A has a private data member `x`; Class B has a private data member `y`. Class A declares Class B as a `friend class`, and Class B declares a non-member function `print()` as a `friend function`. Can the `print()` function directly access and display the private members `x` and `y`? Justify your answer, and if it cannot, provide a solution to make it possible for `print` to display both `x` and `y`."*

#### Rigorous Academic Justification:
**Answer: NO, `print()` CANNOT directly access member `x`.**

1. **Access to `y`**: Function `print()` is explicitly declared as a `friend function` inside Class B. Therefore, `print()` has full authorization to access Class B's private member `y`.
2. **Access to `x`**: Class A granted friendship exclusively to **Class B**. 
   - A friend declaration grants access **only to the member functions of that designated friend class**.
   - `print()` is a **non-member function**; it is NOT a member function of Class B! It is merely a friend of B.
   - Most importantly, **Friendship in C++ is strictly NON-TRANSITIVE**:
     $$\text{If } \text{Class B is a friend of Class A}, \text{ and } \text{Function } print() \text{ is a friend of Class B}, \implies print() \text{ IS NOT a friend of Class A!}$$
   - Therefore, attempting to access `a.x` inside `print()` causes a fatal compile-time error: `error: 'int A::x' is private within this context`.

#### Concrete Code Demonstration & Solution:
```cpp
#include <iostream>

class B; // Forward declaration

class A {
private:
    int x;
public:
    A(int val) : x(val) {}

    // A grants friendship to Class B
    friend class B;

    // SOLUTION: To allow non-member print() to access A::x,
    // Class A MUST ALSO explicitly declare print() as its friend!
    friend void print(const A& a, const B& b);
};

class B {
private:
    int y;
public:
    B(int val) : y(val) {}

    // B grants friendship to print()
    friend void print(const A& a, const B& b);
};

// Now print() is an authorized friend of BOTH Class A and Class B!
void print(const A& a, const B& b) {
    std::cout << "A::x = " << a.x << ", B::y = " << b.y << std::endl;
}

int main() {
    A objA(100);
    B objB(200);
    print(objA, objB); // Successfully prints: A::x = 100, B::y = 200
    return 0;
}
```

---

## 2.10 Pros and Cons of Friendship in C++

| Advantages of Friendship | Disadvantages / Architectural Risks |
|---|---|
| **Facilitates Operator Overloading**: Essential for overloading `<<` and `>>` where the left operand is an `ostream`/`istream` stream class. | **Weakens Encapsulation**: Grants outside entities direct access to private implementation details, creating tight coupling. |
| **High-Performance Inter-Class Bridges**: Allows two tightly coordinated classes (e.g., `Matrix` and `Vector`) to share raw internal buffers without accessor function overhead. | **Maintenance Fragility**: Any structural change to private variables in the host class immediately breaks all friend functions. |
| **Controlled Exception to Access Rules**: More secure than making attributes `public`, because access is strictly restricted to designated entities. | **Cannot Be Inherited or Delegated**: Requires explicit maintenance across complex inheritance hierarchies. |



---

# UNIT 3: Constructors, Destructors, Pointers & Operator Overloading

---

## 3.1 Constructors: Mechanics, Types and Invariants

A **Constructor** is a special non-static member function of a class that is automatically invoked whenever an instance of that class is created. Its primary architectural duty is to initialize the object's data members and establish its invariant state.

### 3.1.1 Essential Characteristics of Constructors
1. **Identifier Matching**: A constructor possesses the **exact same name as the class**.
2. **No Return Type**: It has **no return type whatsoever**, not even `void`. Attempting to specify a return type triggers a compilation error.
3. **Automatic Invocation**: Invoked implicitly by the runtime upon object instantiation (stack allocation, heap allocation via `new`, or static allocation).
4. **No Direct Address**: You cannot take the memory address of a constructor.
5. **Cannot Be Virtual**: Under ISO C++, constructors **cannot be `virtual`** because virtual dispatch requires an existing VTABLE and VPTR, which are only constructed during the constructor's execution.
6. **Can Have Default Arguments & Be Overloaded**: Fully supports overloading and default parameter values.

---

### 3.1.2 The Taxonomy of Constructors

#### 1. Default Constructor
A constructor that accepts no arguments, or where all arguments possess default values.
- **Compiler-Synthesized Default Constructor**: If a class defines **no constructors at all**, the compiler automatically synthesizes an inline public default constructor. This constructor performs default initialization of members (primitives are left with garbage values; objects have their default constructors called).
- **The Suppression Rule (Crucial Exam Rule)**: If a developer defines **any constructor with parameters**, the compiler **suppresses and does NOT generate the automatic default constructor**. Any attempt to declare `ClassName obj;` will result in a fatal compile error unless the developer explicitly writes a parameterless default constructor.

```cpp
class Complex {
private:
    double real, imag;
public:
    // User-defined Default Constructor
    Complex() : real(0.0), imag(0.0) {
        std::cout << "Default constructor invoked." << std::endl;
    }
};
```

#### 2. Parameterized Constructor
A constructor that accepts arguments to initialize data members to specific values upon instantiation.
```cpp
class Complex {
private:
    double real, imag;
public:
    // Parameterized Constructor using Member Initializer List
    Complex(double r, double i) : real(r), imag(i) {}
};

// Invocation Styles:
Complex c1(3.5, 4.2);        // Functional / Explicit notation
Complex c2 = Complex(1.0, 2.0); // Explicit temporary object assignment
```

#### 3. Copy Constructor
A constructor that initializes an object using another already existing object of the exact same class.
- **Canonical Prototype**: `ClassName(const ClassName& source);`

##### Why Must the Copy Constructor Parameter Be Passed by Reference? (Universal Viva Question)
> **Mathematical Proof / Justification**:
> If the parameter to a copy constructor were passed by value:
> `ClassName(ClassName source); // ❌ FATAL RECURSIVE DISASTER`
> Under C++ calling conventions, **passing an object by value requires making a copy of that object**. 
> To make a copy of the argument to pass it to the copy constructor, the runtime would have to call the copy constructor again.
> Calling that copy constructor would again require copying the argument by value, which calls the copy constructor yet again.
> This triggers an **infinite compile-time/runtime recursion** that completely exhausts the call stack! 
> Hence, ISO C++ strictly mandates that copy constructors **must take their argument by reference (`const ClassName&`)**.

---

### 3.1.3 Shallow Copy vs. Deep Copy: The Dynamic Memory Dilemma

When an object encapsulates raw pointers pointing to heap memory allocated with `new`, understanding the distinction between shallow and deep copying is vital.

#### 1. Shallow Copy (Bitwise Copy)
- Copies data members value-by-value, bit-by-bit.
- The **compiler-generated default copy constructor** always performs a **shallow copy**.
- **The Catastrophe**: If an object contains a pointer `int* data`, a shallow copy copies the *address* stored in `data`, not the memory it points to. Both original and copied objects now point to the **exact same physical memory block on the heap**!

#### 2. Deep Copy
- Allocates a brand-new, independent memory block on the heap for the new object.
- Copies the actual data elements from the original memory block into the new block.
- Both objects maintain total isolation and independent lifetimes.

#### Memory Layout Diagram: Shallow vs. Deep Copy

```
========================================================================
SCENARIO A: SHALLOW COPY (DANGEROUS POINTER SHARING)
========================================================================
Stack: Object 1 [ data = 0x5000 ] --------+
                                          |-----> Heap: [ Value: 42 ] (Addr: 0x5000)
Stack: Object 2 [ data = 0x5000 ] --------+

* Consequences:
  1. obj2.modify() silently changes obj1's internal data!
  2. When obj2 goes out of scope, its destructor runs: delete data; (0x5000 freed).
  3. When obj1 goes out of scope, its destructor runs: delete data; (0x5000 freed again!).
  ===> FATAL RUNTIME ABORT: "DOUBLE FREE OR CORRUPTION DETECTED"!

========================================================================
SCENARIO B: DEEP COPY (INDEPENDENT HEAP ALLOCATIONS)
========================================================================
Stack: Object 1 [ data = 0x5000 ] --------------> Heap Block 1: [ Value: 42 ] (0x5000)

Stack: Object 2 [ data = 0x8000 ] --------------> Heap Block 2: [ Value: 42 ] (0x8000)

* Consequences:
  1. Complete state isolation.
  2. Safe destruction: obj2 deletes 0x8000; obj1 deletes 0x5000 independently.
```

#### Complete Implementation of Deep Copy:
```cpp
#include <iostream>
#include <cstring>

class DynamicString {
private:
    char* buffer;
    int length;

public:
    // Parameterized Constructor
    DynamicString(const char* str) {
        length = std::strlen(str);
        buffer = new char[length + 1]; // Allocate on heap
        std::strcpy(buffer, str);
    }

    // User-Defined Deep Copy Constructor
    DynamicString(const DynamicString& other) {
        length = other.length;
        buffer = new char[length + 1]; // 1. Allocate fresh heap block
        std::strcpy(buffer, other.buffer); // 2. Copy contents
        std::cout << "Deep copy constructor executed successfully.\n";
    }

    // Destructor
    ~DynamicString() {
        delete[] buffer; // Deallocate heap memory
        buffer = nullptr;
    }

    void display() const { std::cout << buffer << std::endl; }
};
```

---

### 3.1.4 Dynamic Initialization of Objects

**Dynamic Initialization** refers to initializing an object at runtime using variables, calculations, or resources whose values are known only during program execution (e.g., from user input, hardware sensors, or dynamic file reads), rather than compile-time constants.

```cpp
#include <iostream>

class FixedDeposit {
private:
    long accountNumber;
    double principal;
    float rate;
    int tenureYears;
    double maturityAmount;

public:
    // Dynamic constructor: Rate provided as percentage integer (e.g., 12%)
    FixedDeposit(long acc, double p, int y, int r) 
        : accountNumber(acc), principal(p), tenureYears(y), rate(float(r) / 100.0f) {
        maturityAmount = principal;
        for (int i = 0; i < tenureYears; ++i) {
            maturityAmount *= (1.0 + rate);
        }
    }

    // Overloaded dynamic constructor: Rate provided as decimal float (e.g., 0.12)
    FixedDeposit(long acc, double p, int y, float r) 
        : accountNumber(acc), principal(p), tenureYears(y), rate(r) {
        maturityAmount = principal;
        for (int i = 0; i < tenureYears; ++i) {
            maturityAmount *= (1.0 + rate);
        }
    }

    void display() const {
        std::cout << "Account: " << accountNumber 
                  << " | Maturity Value: " << maturityAmount << std::endl;
    }
};

int main() {
    long acc; double p; int y;
    std::cout << "Enter account, principal, years: ";
    std::cin >> acc >> p >> y;

    char formatChoice;
    std::cout << "Is rate integer (I) or fractional float (F)? ";
    std::cin >> formatChoice;

    if (formatChoice == 'I' || formatChoice == 'i') {
        int rateInt;
        std::cin >> rateInt;
        FixedDeposit fd(acc, p, y, rateInt); // Dynamically initialized at runtime!
        fd.display();
    } else {
        float rateFloat;
        std::cin >> rateFloat;
        FixedDeposit fd(acc, p, y, rateFloat); // Dynamically initialized at runtime!
        fd.display();
    }
    return 0;
}
```

---

### 3.1.5 Constructor Overloading & Default Argument Ambiguities

A class may define multiple constructors provided their parameter lists are distinct. However, combining constructor overloading with default arguments can create **ambiguity collisions**:

```cpp
class Window {
public:
    Window() { std::cout << "Default\n"; }
    Window(int width = 800, int height = 600) { std::cout << "Parameterized\n"; }
};

int main() {
    // Window w; // ❌ COMPILE ERROR: Call of overloaded 'Window()' is ambiguous!
    // Compiler cannot decide whether to call Window() or Window(800, 600)!
}
```

---

### 3.1.6 Addressing Name Shadowing in Constructors (End-Sem 2024 Exam Question 2b)

> **Question**: *"Can a constructor in C++ have a parameter with the same name as a member variable? What issues might arise, and how can they be resolved? Explain with code."*

When a constructor parameter shares the exact identifier with a member variable, the parameter **shadows (hides)** the member variable within the constructor's scope:
```cpp
class Point {
    int x, y;
public:
    Point(int x, int y) {
        x = x; // ❌ ERROR/BUG: Assigns parameter 'x' to itself! Member 'x' remains uninitialized garbage!
        y = y;
    }
};
```

#### Resolutions:
1. **Resolution 1: Explicit `this->` Pointer Qualification**:
   ```cpp
   Point(int x, int y) {
       this->x = x; // 'this->x' explicitly designates the member variable!
       this->y = y;
   }
   ```
2. **Resolution 2: Member Initializer List (Best Practice)**:
   ```cpp
   Point(int x, int y) : x(x), y(y) {}
   ```
   *Why this works*: In the initialization list `x(x)`, the compiler's grammar rules unambiguously dictate that the identifier outside the parenthesis is the member name, and the identifier inside is the parameter!

---

### 3.1.7 Can a Constructor Be Explicitly Invoked Like a Regular Member Function? (End-Sem 2024 Exam Question 4a)

> **Question**: *"Can a constructor be explicitly invoked like a regular member function in C++? Justify your answer with an example."*

#### Rigorous Academic Justification:
**Answer: NO, a constructor CANNOT be invoked on an existing object using member access syntax (`object.Constructor()`).**

1. **Syntactical Rejection**: In C++, writing `obj.Point(5, 10);` is a fatal compile-time syntax error. A constructor is not a normal callable member; it has no addressable symbol accessible via an object instance.
2. **Explicit Temporary Object Creation**: You can explicitly invoke a constructor to construct a **new, unnamed temporary object**:
   ```cpp
   Point p1(1, 2);
   p1 = Point(10, 20); // Legal: Explicitly creates a temporary Point object and copies it into p1
   ```
3. **Placement `new`**: The only mechanism in C++ to invoke a constructor on an already existing raw memory buffer is via **placement new**:
   ```cpp
   char memoryBuffer[sizeof(Point)];
   Point* ptr = new (memoryBuffer) Point(5, 5); // Explicit construction in pre-allocated buffer
   ptr->~Point(); // Explicit destructor invocation required
   ```

---

## 3.2 Destructors

A **Destructor** is a special member function that is executed automatically when an object's lifetime ends (e.g., when a stack object leaves its enclosing scope `{ }`, when a heap object is deallocated via `delete`, or when the program exits for static objects).

### Core Characteristics & Rules
1. **Syntax**: Exactly the class name preceded by a tilde symbol (`~`), e.g., `~Student()`.
2. **No Arguments and No Return Type**: A destructor takes **zero parameters** and returns nothing.
3. **No Overloading**: Because it accepts no parameters, **a class can have exactly one destructor**.
4. **Order of Invocation (The LIFO Rule)**: Destructors are executed in the **exact reverse order of constructor invocation** (Last-In, First-Out / Stack unwinding).

```cpp
#include <iostream>

class LifetimeDemo {
    int id;
public:
    LifetimeDemo(int i) : id(i) {
        std::cout << "Constructor [" << id << "] called.\n";
    }
    ~LifetimeDemo() {
        std::cout << "Destructor  [" << id << "] called.\n";
    }
};

int main() {
    LifetimeDemo a(1);
    LifetimeDemo b(2);
    LifetimeDemo c(3);
    std::cout << "Exiting main...\n";
    return 0;
}
```
**Output**:
```
Constructor [1] called.
Constructor [2] called.
Constructor [3] called.
Exiting main...
Destructor  [3] called.
Destructor  [2] called.
Destructor  [1] called.
```

---

## 3.3 Pointers in C++: Core Architecture & Pitfalls

A **Pointer** is a variable whose value is the physical memory address of another variable.

### 3.3.1 Address-of (`&`) and Dereference (`*`) Operators
- `&` (Address-of): Returns the hexadecimal memory address of its operand.
- `*` (Indirection / Dereference): Accesses the contents stored in the memory address pointed to.

```cpp
int value = 42;
int* ptr = &value; // ptr stores memory address of value
*ptr = 99;         // Dereferences ptr, mutating 'value' to 99
```

### 3.3.2 Pointer Arithmetic Mechanics
Arithmetic on pointers is strictly scaled by the size of the underlying data type ($\text{sizeof}(T)$):
$$\text{New Address} = \text{Base Address} + (i \times \text{sizeof}(T))$$
- `ptr++`: Advances the pointer by $\text{sizeof}(*ptr)$ bytes.
- `ptr1 - ptr2`: Returns the number of elements of type $T$ separating the two addresses (type `ptrdiff_t`).
- **Illegal Operations**: Adding two pointers (`ptr1 + ptr2`), multiplying pointers, or dividing pointers is illegal.

---

### 3.3.3 The `this` Pointer

In non-static member functions, the keyword **`this`** represents an implicit, immutable pointer (`ClassName* const this`) that points directly to the specific object instance for which the member function was called.

#### Three Primary Architectural Uses of `this`:
1. **Disambiguating Shadowed Identifiers**:
   ```cpp
   void setRadius(double radius) { this->radius = radius; }
   ```
2. **Method Chaining (Fluent Interface)**: By returning `*this` by reference, multiple member function calls can be chained together sequentially:
   ```cpp
   class Builder {
   public:
       Builder& setStepA() { /* step A */ return *this; }
       Builder& setStepB() { /* step B */ return *this; }
   };
   // Usage:
   Builder b;
   b.setStepA().setStepB();
   ```
3. **Guarding Against Self-Assignment**: In overloaded assignment operators (`operator=`), verifying `if (this == &rhs)` prevents deleting own resources before copying.

---

### 3.3.4 Special Pointer Categories & Traps

#### 1. Void Pointer (`void*` - The Generic Pointer)
- Points to data of any unspecified type.
- **Rules**: Cannot be directly dereferenced (`*vPtr` is illegal). Cannot undergo pointer arithmetic directly. Must be explicitly typecast before dereferencing:
  ```cpp
  int num = 50;
  void* v = &num;
  int extracted = *(static_cast<int*>(v)); // Valid
  ```

#### 2. Dangling Pointer
- Occurs when a pointer continues to hold the memory address of an object that has already been deallocated/freed.
- **Causes**:
  1. Deallocating memory with `delete ptr;` without setting `ptr = nullptr;`.
  2. Returning a pointer to a local stack variable from a function.
  3. Pointer referencing a variable that has gone out of scope.
- **Solution**: Always reset deallocated pointers to `nullptr`.

#### 3. Null Pointer (`NULL` vs. `nullptr`)
- In legacy C/C++, `NULL` is a preprocessor macro defined as integer `0` or `((void*)0)`.
- **The C++11 Solution (`nullptr`)**: `NULL` causes severe function overloading ambiguities:
  ```cpp
  void process(int x);
  void process(int* ptr);
  // process(NULL); // ❌ AMBIGUOUS: NULL is 0 (int), which function is intended?
  process(nullptr); // ✅ UNAMBIGUOUS: Calls process(int*) because nullptr has type std::nullptr_t!
  ```

#### 4. Wild Pointer
- An uninitialized pointer variable (`int* p;`). It contains random garbage bits pointing to an arbitrary memory segment. Dereferencing a wild pointer causes immediate operating system segmentation faults or silent memory corruption.

---

### 3.3.5 Dynamic Memory Allocation: `new` / `delete` vs. `malloc()` / `free()`

| Dimension / Metric | `malloc()` / `free()` (C Standard Library) | `new` / `delete` (C++ Operators) |
|---|---|---|
| **Nature** | Standard library functions (`<cstdlib>`). | Built-in language **operators**. |
| **Object Lifecycle** | **Does NOT call constructors or destructors**. Merely allocates raw bytes. | **Calls constructors** upon allocation and **calls destructors** upon deallocation. |
| **Type Safety & Casting**| Returns raw `void*`; requires explicit typecasting (`int* p = (int*)malloc(...)`). | **Type-safe**. Automatically returns the correct typed pointer (`int* p = new int;`). |
| **Size Computation** | Requires manual size calculation via `sizeof` (`malloc(sizeof(int) * 10)`). | Computes size automatically (`new int[10]`). |
| **Failure Behavior** | Returns `NULL` upon memory exhaustion. | Throws **`std::bad_alloc` exception** by default (or returns null with `nothrow`). |
| **Array Deallocation** | Same `free(ptr)` function for single elements and arrays. | Distinguishes between single element (`delete ptr;`) and array (`delete[] ptr;`). |

---

## 3.4 Operator Overloading

**Operator Overloading** is a compile-time polymorphic feature in C++ that enables existing language operators (`+`, `-`, `*`, `==`, `<<`, etc.) to be assigned custom, user-defined semantics when applied to objects of user-defined classes.

### 3.4.1 Inviolable Rules of Operator Overloading
1. **Operators That CANNOT Be Overloaded**:
   - `.` (Class member access operator)
   - `.*` (Pointer-to-member operator)
   - `::` (Scope resolution operator)
   - `?:` (Ternary conditional operator)
   - `sizeof` (Size-of operator)
   - `typeid` (RTTI operator)
2. **No New Operator Symbols**: You cannot invent new operator tokens (e.g., `**` or `<=>` prior to C++20).
3. **Immutability of Precedence and Associativity**: Overloading cannot alter the inherent precedence or associativity of an operator.
4. **Immutability of Arity**: Unary operators must remain unary; binary operators must remain binary.
5. **Mandatory User-Defined Operand**: At least one operand must be of a user-defined class/enum type. You cannot overload operators for primitive built-in types (e.g., you cannot redefine `int + int`).
6. **No Default Arguments**: Overloaded operator functions cannot have default arguments.

---

### 3.4.2 Member Function vs. Friend Function in Operator Overloading

| Property | Overloading via Member Function | Overloading via Friend / Non-Member Function |
|---|---|---|
| **Parameter Count (Unary)** | **0 parameters** (invoked on `this` object: `obj.operator++()`). | **1 parameter** (receives target object explicitly: `operator++(obj)`). |
| **Parameter Count (Binary)**| **1 parameter** (left operand is `*this`, right operand is passed: `obj1.operator+(obj2)`). | **2 parameters** (both left and right operands passed explicitly: `operator+(obj1, obj2)`). |
| **Left Operand Constraint** | Left operand **MUST** be an object of this exact class. | Left operand can be of a **different class or primitive type**! |
| **Stream I/O (`<<`, `>>`)** | **Cannot be implemented as member functions** of our class. | **Must be implemented as friend/non-member functions**. |

---

### 3.4.3 Overloading Unary Operators: Prefix vs. Postfix (`++` / `--`)

In C++, prefix increment (`++obj`) and postfix increment (`obj++`) share the identical symbol `++`. To distinguish between them, C++ uses an academic convention: **the postfix operator function accepts a dummy `int` parameter**.

```cpp
#include <iostream>

class Counter {
private:
    int count;

public:
    Counter(int c = 0) : count(c) {}

    // 1. Prefix Increment (++c): Member function
    // Signature: Return by REFERENCE to allow chained operations (++(++c))
    Counter& operator++() {
        ++count;
        return *this; // Return mutated object
    }

    // 2. Postfix Increment (c++): Member function
    // Signature: Dummy 'int' argument; Return by VALUE of previous state!
    Counter operator++(int) {
        Counter temp = *this; // Save current state
        count++;              // Mutate current object
        return temp;          // Return unmodified prior state
    }

    void display() const { std::cout << "Count: " << count << std::endl; }
};
```

---

### 3.4.4 Overloading Binary Operators: Complete `Time` Addition Class (End-Sem 2024 Exam Question 3b)

> **Exam Requirement**: *"Design a class Time that represents time in hours, minutes, and seconds format. Implement operator overloading to allow the addition of two Time objects using the `+` operator."*

```cpp
#include <iostream>

class Time {
private:
    int hours;
    int minutes;
    int seconds;

    void normalize() {
        minutes += seconds / 60;
        seconds %= 60;
        hours += minutes / 60;
        minutes %= 60;
    }

public:
    Time(int h = 0, int m = 0, int s = 0) : hours(h), minutes(m), seconds(s) {
        normalize();
    }

    // Binary + Operator Overloading as a Member Function
    Time operator+(const Time& t) const {
        Time result;
        result.seconds = this->seconds + t.seconds;
        result.minutes = this->minutes + t.minutes;
        result.hours   = this->hours   + t.hours;
        result.normalize(); // Handles rolling 60 seconds into minutes, 60 minutes into hours
        return result;
    }

    // Stream Insertion Operator Overload (Friend Function)
    friend std::ostream& operator<<(std::ostream& out, const Time& t) {
        out << (t.hours < 10 ? "0" : "") << t.hours << ":"
            << (t.minutes < 10 ? "0" : "") << t.minutes << ":"
            << (t.seconds < 10 ? "0" : "") << t.seconds;
        return out;
    }
};

int main() {
    Time t1(2, 45, 50);
    Time t2(1, 20, 30);
    Time t3 = t1 + t2; // Equivalent to: t1.operator+(t2)

    std::cout << "Time 1: " << t1 << std::endl;
    std::cout << "Time 2: " << t2 << std::endl;
    std::cout << "Sum   : " << t3 << std::endl; // Prints: 04:06:20
    return 0;
}
```

---

### 3.4.5 Overloading Stream Insertion (`<<`) and Extraction (`>>`) Operators

#### Why MUST Stream Operators Be Overloaded as Friend / Non-Member Functions?
When writing `std::cout << myObj;`:
- The binary operator `<<` takes two operands: `std::cout` on the left (an object of class `std::ostream`), and `myObj` on the right (our class).
- If overloaded as a member function, it would have to be a member function of `std::ostream`. We cannot modify the standard C++ `<iostream>` library class!
- If implemented as a member of our class, the syntax would be inverted to `myObj << std::cout;`, which breaks standard C++ conventions.
- Therefore, `operator<<` and `operator>>` **must be non-member functions**, typically declared as `friend` functions to access private data.
- **Chaining**: Both operators return a reference to the stream (`std::ostream&` / `std::istream&`) to support chained statements like `std::cout << a << b << c;`.

---

## 3.5 Type Conversion in C++

C++ automatically manages conversions between basic types (`int` to `double`). For user-defined classes, the compiler must be instructed how to perform conversions across three distinct boundaries:

```
                    +---------------------------+
                    | Basic Type <--> Class Type|
                    +---------------------------+
                                  |
            +---------------------+---------------------+
            |                                           |
            v                                           v
[Basic Type -> Class Type]                  [Class Type -> Basic Type]
   * Parameterized Constructor                 * Casting / Conversion Operator
     (e.g., Complex(double))                     (e.g., operator double())

                                  |
                                  v
                    +---------------------------+
                    | Class Type <--> Class Type|
                    +---------------------------+
            +---------------------+---------------------+
            |                                           |
            v                                           v
[Constructor in Destination Class]          [Conversion Operator in Source Class]
```

### 1. Basic Type to Class Type
Achieved via a **Single-Argument Constructor** in the destination class:
```cpp
class Distance {
private:
    int kilometers;
    float meters;
public:
    Distance(float totalMeters) { // Basic float -> Class Distance
        kilometers = int(totalMeters / 1000);
        meters = totalMeters - (kilometers * 1000);
    }
};
// Usage:
Distance d = 2500.50f; // Automatically invokes Distance(float)
```

### 2. Class Type to Basic Type: The Conversion Operator
Achieved by defining a **Casting / Conversion Operator function** inside the class.
#### Syntactical Rules of Conversion Operators:
1. It must be a **member function**.
2. It **must NOT specify a return type**, not even `void`! (The return type is implicitly the type being converted to).
3. It must take **zero parameters**.

#### Implementation: `Temperature` Class (End-Sem 2024 Exam Question 5)
```cpp
#include <iostream>

class Temperature {
private:
    float celsius;

public:
    // a) Constructor initializing Celsius
    Temperature(float c = 0.0f) : celsius(c) {}

    // b) Member function to convert Celsius to Fahrenheit: F = (C * 9/5) + 32
    float toFahrenheit() const {
        return (celsius * 9.0f / 5.0f) + 32.0f;
    }

    // c) Conversion operator to automatically convert Temperature to float (Fahrenheit)
    operator float() const {
        return (celsius * 9.0f / 5.0f) + 32.0f;
    }

    float getCelsius() const { return celsius; }
};

int main() {
    // d) Demonstrate conversion using both approaches:
    Temperature t(100.0f); // Boiling point of water

    // Approach 1: Member function call
    float f1 = t.toFahrenheit();
    std::cout << "Via Member Function     : " << f1 << " F" << std::endl;

    // Approach 2: Conversion operator (Implicit & Explicit cast)
    float f2 = t; // Implicit invocation of operator float()
    std::cout << "Via Conversion Operator : " << f2 << " F" << std::endl;
    return 0;
}
```

### 3. One Class Type to Another Class Type
Converting an object of `Class Source` into an object of `Class Destination`.

#### Approach A: Conversion Constructor in the Destination Class
```cpp
class Source; // Forward declaration

class Destination {
public:
    Destination(const Source& src); // Destination constructor takes Source reference
};
```

#### Approach B: Conversion Operator in the Source Class
```cpp
class Source {
public:
    operator Destination() const; // Source defines operator to cast to Destination
};
```
*Design Rule: Implement either Approach A or Approach B in a given project, never both simultaneously, otherwise the compiler will report an ambiguity error when converting!*



---

# UNIT 4: Inheritance, Runtime Polymorphism & Virtual Mechanics

---

## 4.1 Inheritance Fundamentals & Visibility Modes

**Inheritance** is the object-oriented mechanism by which a new class (the **Derived / Child class**) is constructed from an existing class (the **Base / Parent class**), inheriting its attributes and behaviors while adding new features or modifying existing behaviors.

### Conceptual Foundations
- **"Is-A" Relationship**: Models taxonomic hierarchies (e.g., a `CheckingAccount` *is a* `BankAccount`).
- **Code Reusability**: Prevents code duplication by factoring shared logic into common ancestors.
- **Extensibility & Polymorphic Substitution**: Derived objects can be substituted wherever base class instances are expected (Liskov Substitution Principle).

### General Syntax of Class Derivation
```cpp
class DerivedClass : visibility-mode BaseClass {
    // Derived class body
};
```

---

### The Visibility Modes & Member Accessibility Matrix

The **Visibility Mode** (`public`, `protected`, or `private`) controls how members inherited from the Base class are exposed within the Derived class:

| Base Class Member Access | Inherited via `public` Mode | Inherited via `protected` Mode | Inherited via `private` Mode |
|---|---|---|---|
| **`private`** | **Inaccessible directly** (Accessible only via Base public/protected methods) | **Inaccessible directly** | **Inaccessible directly** |
| **`protected`** | Becomes **`protected`** in Derived class | Becomes **`protected`** in Derived class | Becomes **`private`** in Derived class |
| **`public`** | Becomes **`public`** in Derived class | Becomes **`protected`** in Derived class | Becomes **`private`** in Derived class |

#### Critical Academic Insights:
1. **Private Members Are Never Directly Accessible**: Base class `private` data members are physically inherited in memory, but the compiler strictly forbids direct name access inside derived member functions.
2. **Default Visibility Mode**: If the visibility mode is omitted:
   - For `class Derived : Base` $\rightarrow$ defaults to **`private`**.
   - For `struct Derived : Base` $\rightarrow$ defaults to **`public`**.

---

## 4.2 Types of Inheritance

C++ supports five distinct architectural configurations of inheritance:

```
1. Single Inheritance:      2. Multilevel:         3. Multiple:
       +---+                    +---+              +----+   +----+
       | A |                    | A |              | B1 |   | B2 |
       +---+                    +---+              +----+   +----+
         |                        |                   \       /
         v                        v                    v     v
       +---+                    +---+                   +---+
       | B |                    | B |                   | D |
       +---+                    +---+                   +---+
                                  |
                                  v
                                +---+
                                | C |
                                +---+

4. Hierarchical:            5. Hybrid (The Diamond):
       +---+                        +---+
       | A |                        | A | (Common Base)
       +---+                        +---+
      /     \                      /     \
     v       v                    v       v
   +---+   +---+                +---+   +---+
   | B |   | C |                | B |   | C |
   +---+   +---+                +---+   +---+
                                  \       /
                                   v     v
                                    +---+
                                    | D | (Diamond Derived)
                                    +---+
```

---

### 4.2.1 Multiple Inheritance and Name Ambiguity

**Multiple Inheritance** occurs when a single derived class inherits directly from two or more base classes.

#### The Member Name Ambiguity Collision (End-Sem 2024 Exam Question 6a)
> **Question**: *"In a multiple inheritance scenario, if two base classes have a function with the same signature, will there be any problem when calling that function from a derived class? If yes, how can such conflicts be resolved explicitly in C++?"*

When two base classes (`Base1` and `Base2`) declare a function with identical signatures (`void display()`), attempting to invoke `d.display()` on an object of derived class `Derived` creates a **compile-time ambiguity error**: the compiler cannot determine which base class implementation is intended.

#### Explicit Resolution Mechanisms:

```cpp
#include <iostream>

class Base1 {
public:
    void display() { std::cout << "Base1 display\n"; }
};

class Base2 {
public:
    void display() { std::cout << "Base2 display\n"; }
};

class Derived : public Base1, public Base2 {
public:
    // Resolution Method 2: Override the conflicting function in Derived class
    void display() {
        std::cout << "Derived resolves conflict by explicitly dispatching:\n";
        Base1::display(); // Delegate to Base1
        Base2::display(); // Delegate to Base2
    }
};

int main() {
    Derived d;

    // ❌ d.display(); -> Ambiguous IF Derived did not override display()!

    // Resolution Method 1: Using Scope Resolution Operator from client code:
    d.Base1::display(); // Explicitly calls Base1's version
    d.Base2::display(); // Explicitly calls Base2's version

    // Invoking overridden method:
    d.display();
    return 0;
}
```

---

### 4.2.2 Hybrid Inheritance & The Diamond Problem: Virtual Base Classes

#### The Problem: Duplicate Subobjects and Ambiguity
In the canonical Diamond hierarchy:
- Class `A` is the root base class.
- Classes `B` and `C` inherit from `A`.
- Class `D` inherits from both `B` and `C`.

Without virtual inheritance, an object of class `D` physically contains **two separate subobjects of Class A** (one inherited through `B`, and one inherited through `C`).

```
Non-Virtual Diamond Memory Layout of Object D:
+-----------------------------------+
|  Subobject B                      |
|  +------------------------------+ |
|  | Subobject A (Copy 1: x = 10) | |
|  +------------------------------+ |
|  | Member b                     | |
+-----------------------------------+
|  Subobject C                      |
|  +------------------------------+ |
|  | Subobject A (Copy 2: x = 10) | |
|  +------------------------------+ |
|  | Member c                     | |
+-----------------------------------+
|  Member d                         |
+-----------------------------------+
```
- **Consequences**:
  1. **Memory Bloat**: Duplicate storage for all of A's data members.
  2. **Compilation Failure**: Calling `d.x` or `d.show()` is rejected: `error: request for member 'x' is ambiguous`.

---

#### The Solution: Virtual Base Classes
By declaring `A` as a **`virtual` base class** during the derivation of `B` and `C`, C++ guarantees that **only a single, shared subobject of `A` will exist** within any downstream derived class (`D`).

```cpp
#include <iostream>

class A {
public:
    int x;
    A(int val = 0) : x(val) {
        std::cout << "A constructor called with x = " << x << std::endl;
    }
};

// Virtual base class declaration:
class B : virtual public A {
public:
    B(int val) : A(val) { std::cout << "B constructor called\n"; }
};

class C : public virtual A { // Order of 'virtual' and 'public' does not matter
public:
    C(int val) : A(val) { std::cout << "C constructor called\n"; }
};

class D : public B, public C {
public:
    // CRITICAL RULE: In virtual inheritance, the MOST DERIVED CLASS (D)
    // is directly responsible for initializing the virtual base class (A)!
    D(int vA, int vB, int vC, int vD) : A(vA), B(vB), C(vC) {
        std::cout << "D constructor called\n";
    }

    void print() {
        std::cout << "x = " << x << std::endl; // ✅ UNAMBIGUOUS! Only ONE 'x' exists!
    }
};

int main() {
    D obj(100, 20, 30, 40);
    obj.print();
    return 0;
}
```

#### Constructor Execution Order in Virtual Inheritance (Quiz 2, Q4 Favorite):
1. **Virtual Base Classes are ALWAYS constructed FIRST**, before any non-virtual base classes, regardless of where they appear in the derivation list.
2. In the code above, the sequence is:
   $$\text{A constructor} \longrightarrow \text{B constructor} \longrightarrow \text{C constructor} \longrightarrow \text{D constructor}$$
3. Intermediate constructor calls to `A` from `B(vB)` and `C(vC)` are **silently suppressed and ignored** during the construction of `D`. Only `D`'s direct call `A(vA)` executes!

---

## 4.3 Containership (Delegation / Composition) vs. Inheritance

### "Is-A" vs. "Has-A" Architecture

| Dimension | Inheritance ("Is-A") | Containership / Composition ("Has-A") |
|---|---|---|
| **Relationship** | Class B *is a* specialized type of Class A (`Dog` is an `Animal`). | Class B *has an* instance of Class A as a component (`Car` has an `Engine`). |
| **Coupling Level** | Tight coupling (changes to Base can break Derived). | Loose coupling (Container interacts only through public interface). |
| **Encapsulation** | Weakened (Derived often accesses Base protected members). | Strictly preserved (Container cannot access private internals of member). |
| **Polymorphism** | Directly enables dynamic polymorphism via base pointers. | Indirect (can forward calls dynamically to contained pointers). |
| **Design Principle** | "Favor object composition over class inheritance". | Ideal for assembling complex systems from discrete parts. |

---

## 4.4 Constructors and Destructors in Derived Classes

When an instance of a derived class is constructed or destroyed, constructor and destructor calls proceed according to strict deterministic rules:

### Execution Sequence Rules:
1. **Constructors**:
   - Virtual base class constructors execute first.
   - Non-virtual base class constructors execute next, **in the exact order they are listed in the class derivation header** (left-to-right).
   - Contained member-object constructors execute next, in the order they are declared in the class body.
   - Derived class constructor body executes last.
2. **Destructors**:
   - Execute in the **exact reverse order** of constructors (stack unwinding / LIFO).

```cpp
#include <iostream>

class Base1 {
public:
    Base1() { std::cout << "Base1 Constructor\n"; }
    ~Base1() { std::cout << "Base1 Destructor\n"; }
};

class Base2 {
public:
    Base2() { std::cout << "Base2 Constructor\n"; }
    ~Base2() { std::cout << "Base2 Destructor\n"; }
};

class Derived : public Base1, public Base2 {
public:
    Derived() { std::cout << "Derived Constructor\n"; }
    ~Derived() { std::cout << "Derived Destructor\n"; }
};

int main() {
    Derived d;
    return 0;
}
```
**Output**:
```
Base1 Constructor
Base2 Constructor
Derived Constructor
Derived Destructor
Base2 Destructor
Base1 Destructor
```

---

## 4.5 Polymorphism: Compile-Time vs. Run-Time

```
                                POLYMORPHISM
                                     |
           +-------------------------+-------------------------+
           |                                                   |
           v                                                   v
  Compile-Time Polymorphism                           Run-Time Polymorphism
  (Static / Early Binding)                            (Dynamic / Late Binding)
  * Function Overloading                              * Virtual Functions
  * Operator Overloading                              * Dynamic Binding via VTABLE
  * Templates (Generic Programming)                   * Pointer-to-Derived Mechanics
```

### Deep Comparison Table

| Attribute | Compile-Time Polymorphism | Run-Time Polymorphism |
|---|---|---|
| **Binding Time** | Resolved by compiler during compilation/linking. | Resolved at runtime during program execution. |
| **Dispatch Mechanism** | Direct subroutine call to fixed memory address. | Indirect dispatch lookup through **VTABLE / VPTR**. |
| **Execution Speed** | **Fastest** (Zero runtime overhead; enables inlining). | Slightly slower due to pointer indirection. |
| **Memory Footprint**| No extra memory per object. | Incurs overhead of 1 pointer (`vptr`, 8 bytes on 64-bit) per object + static VTABLE. |
| **Flexibility** | Rigid at runtime (all types fixed at compile time). | Highly flexible (new derived types plug in seamlessly). |

---

## 4.6 Pointers to Derived Class Objects & Object Slicing

In C++, a base class pointer can legally store the memory address of any publicly derived class object:
```cpp
Base* bPtr = new Derived(); // Completely legal and foundational to OOP
```

### The Static Type vs. Dynamic Type Distinction:
- **Static Type**: The declared type of the pointer at compile time (here, `Base*`).
- **Dynamic Type**: The actual type of the object occupying the memory at runtime (here, `Derived`).

### The Danger of Object Slicing
**Object Slicing** occurs when a Derived class object is assigned **by value** to a Base class object:
```cpp
class Base { public: int b; };
class Derived : public Base { public: int d; };

Derived dev;
dev.b = 10;
dev.d = 20;

Base baseObj = dev; // ⚠️ OBJECT SLICING OCCURS!
```
- **Internal Mechanism**: `baseObj` only has memory allocated for `sizeof(Base)`. When `dev` is assigned to `baseObj`, the compiler copies only the `Base` subobject portion. All derived attributes (`d`) and VTABLE associations are **sliced off and permanently discarded**.
- **Prevention**: Always pass and manipulate polymorphic objects via **pointers (`Base*`) or references (`Base&`)**, never by value!

---

## 4.7 Virtual Functions and the VTABLE / VPTR Architecture

### Why Virtual Functions Are Essential
Without the `virtual` keyword, C++ performs **static early binding**: the function to be called is determined exclusively by the static type of the pointer, NOT the actual object pointed to!

```cpp
class Base {
public:
    void show() { std::cout << "Base Show\n"; } // Non-virtual
};
class Derived : public Base {
public:
    void show() { std::cout << "Derived Show\n"; }
};

Base* ptr = new Derived();
ptr->show(); // Prints: "Base Show" (Static binding binds to Base::show!)
```
Prepending **`virtual`** to the base declaration instructs the compiler to defer function address resolution until runtime:
```cpp
class Base {
public:
    virtual void show() { std::cout << "Base Show\n"; }
};
// Now: ptr->show() prints: "Derived Show"!
```

---

### Internal Working Mechanism: The VTABLE & VPTR Architecture

Whenever a class declares or inherits at least one `virtual` function, the C++ compiler injects specialized runtime machinery:

1. **VTABLE (Virtual Table)**:
   - A static, read-only array of function pointers constructed by the compiler in static data memory for **each polymorphic class** (one table per class, NOT per object).
   - Each entry holds the memory address of the most derived virtual function override for that class.
2. **VPTR (Virtual Pointer)**:
   - A hidden pointer member automatically injected as the first 8 bytes (on 64-bit systems) of **every object instance** of that class.
   - When an object is constructed, the constructor automatically initializes this `vptr` to point to that class's corresponding `VTABLE`.

---

### Detailed ASCII Architecture Diagram: VTABLE and VPTR Dynamic Dispatch

```
========================================================================================
MEMORY LAYOUT: OBJECT INSTANCE IN HEAP vs. CLASS VTABLES IN STATIC MEMORY
========================================================================================

Code Statement:
Base* bPtr = new Derived();
bPtr->show();

Step 1: Object Memory Layout (Heap / Stack)
+---------------------------------------------------+
|  Derived Object Instance (at Address: 0x0080FF00) |
|  +---------------------------------------------+  |
|  | VPTR (8 Bytes)  -----> Holds: 0x0040A000     |  | (Points to Derived's VTABLE)
|  +---------------------------------------------+  |
|  | Base::dataMemberA                           |  |
|  +---------------------------------------------+  |
|  | Derived::dataMemberB                        |  |
|  +---------------------------------------------+  |
+---------------------------------------------------+
                             |
                             v  (Dereferenced at runtime)
Step 2: Virtual Method Tables (Static Data Segment)

  Base Class VTABLE [Addr: 0x00409000]
  +-------+------------------------------------------+
  | Slot  | Function Target Address                  |
  +-------+------------------------------------------+
  | [ 0 ] | &Base::show()     --> Addr: 0x00101000   |
  | [ 1 ] | &Base::print()    --> Addr: 0x00101500   |
  +-------+------------------------------------------+

  Derived Class VTABLE [Addr: 0x0040A000]
  +-------+------------------------------------------+
  | Slot  | Function Target Address                  |
  +-------+------------------------------------------+
  | [ 0 ] | &Derived::show()  --> Addr: 0x00201000   | <--- OVERRIDDEN SHOW!
  | [ 1 ] | &Base::print()    --> Addr: 0x00101500   | <--- INHERITED PRINT!
  +-------+------------------------------------------+
                             |
                             v
Step 3: Execution of Call 'bPtr->show()'
  1. Fetch pointer: bPtr (0x0080FF00)
  2. Dereference VPTR: *(0x0080FF00) -> Yields VTABLE address (0x0040A000)
  3. Look up index for show(): Slot [0] -> Yields function pointer 0x00201000
  4. Jump to instruction address 0x00201000 -> Executes Derived::show()!
```

---

### 4.7.1 The Virtual Destructor Imperative (Quiz 2, Q10 Problem)

> **Exam Question**: *"Why must base class destructors be declared virtual?"*

Consider deleting a derived object through a base pointer when the destructor is non-virtual:
```cpp
class Base {
public:
    ~Base() { std::cout << "~Base()\n"; } // NON-VIRTUAL!
};
class Derived : public Base {
    int* buffer;
public:
    Derived() { buffer = new int[1000]; }
    ~Derived() { 
        delete[] buffer; 
        std::cout << "~Derived()\n"; 
    }
};

int main() {
    Base* ptr = new Derived();
    delete ptr; // ⚠️ DISASTER: Statically binds to ~Base()!
}
```
- **Consequence**: The compiler sees `Base*`, looks at `~Base()`, notes it is non-virtual, and performs static binding. Only `~Base()` executes!
- `~Derived()` is **completely skipped**. The 1000 integers on the heap are never freed, producing a severe **memory leak** and undefined behavior.
- **Rule**: **If a class has ANY virtual functions, its destructor MUST be declared `virtual`!**
  ```cpp
  virtual ~Base() { std::cout << "~Base()\n"; }
  ```

---

## 4.8 Pure Virtual Functions and Abstract Classes

### 4.8.1 Pure Virtual Functions
A **Pure Virtual Function** is a virtual function that provides no default implementation in the base class and mandates that all non-abstract derived classes must override it.
- **Syntax**: `virtual ReturnType FunctionName(Parameters) = 0;`
- The `= 0` notation is termed the *pure-specifier*.

### 4.8.2 Abstract Classes
An **Abstract Class** is any class that contains **at least one pure virtual function**.
- **Cannot Be Instantiated**: Attempting to declare an object of an abstract class (`Shape s;`) is a fatal compile-time error.
- **Can Have Pointers and References**: You can legally declare pointers and references to abstract classes (`Shape* sPtr = new Circle();`).
- **Can Have Constructors**: Abstract classes can define constructors to initialize their protected data members, invoked via derived initialization lists.
- **Pure Virtual Function with Definition**: In C++, a pure virtual function *can* legally have a function body defined outside the class (`void Shape::draw() { ... }`). Derived classes must still override it, but can invoke `Shape::draw()` explicitly.

---

### 4.8.3 Comprehensive Exam Problem: `Shape`, `Circle`, `Rectangle`, `Graphics` (End-Sem 2024 Exam Question 7)

> **Specification**:
> 1. Base class `Shape` with private member `color` and pure virtual function `draw()`.
> 2. Derived classes `Circle` and `Rectangle` overriding `draw()`.
> 3. Class `Graphics` containing an array of `Shape*` pointers demonstrating **containership** and **runtime polymorphism**.

```cpp
#include <iostream>
#include <string>

// a) Base Abstract Class
class Shape {
private:
    std::string color;

public:
    Shape(const std::string& c = "White") : color(c) {}
    virtual ~Shape() {} // Mandatory Virtual Destructor

    std::string getColor() const { return color; }

    // Pure virtual function
    virtual void draw() const = 0;
};

// b) Derived Class: Circle
class Circle : public Shape {
private:
    double radius;
public:
    Circle(double r, const std::string& c = "Red") : Shape(c), radius(r) {}

    void draw() const override {
        std::cout << "Drawing Circle [Color: " << getColor() 
                  << ", Radius: " << radius << "]\n";
    }
};

// b) Derived Class: Rectangle
class Rectangle : public Shape {
private:
    double width, height;
public:
    Rectangle(double w, double h, const std::string& c = "Blue") 
        : Shape(c), width(w), height(h) {}

    void draw() const override {
        std::cout << "Drawing Rectangle [Color: " << getColor() 
                  << ", Width: " << width << ", Height: " << height << "]\n";
    }
};

// c) Container Class: Graphics (Demonstrating Containership & Dynamic Polymorphism)
class Graphics {
private:
    static const int MAX_SHAPES = 10;
    Shape* shapes[MAX_SHAPES]; // Array of Base pointers (Containership)
    int count;

public:
    Graphics() : count(0) {}

    ~Graphics() {
        // Clean up dynamically allocated shapes
        for (int i = 0; i < count; ++i) {
            delete shapes[i];
            shapes[i] = nullptr;
        }
    }

    bool addShape(Shape* s) {
        if (count < MAX_SHAPES) {
            shapes[count++] = s;
            return true;
        }
        return false;
    }

    // Demonstrating Dynamic Polymorphism across contained objects
    void renderAll() const {
        std::cout << "\n--- Rendering Graphics Scene (" << count << " shapes) ---\n";
        for (int i = 0; i < count; ++i) {
            // Polymorphic dispatch via VTABLE lookup:
            shapes[i]->draw();
        }
    }
};

int main() {
    Graphics scene;
    scene.addShape(new Circle(5.5, "Crimson"));
    scene.addShape(new Rectangle(10.0, 4.0, "Navy Blue"));
    scene.addShape(new Circle(2.1, "Emerald Green"));

    scene.renderAll();
    return 0;
}
```



---

# UNIT 5: Console I/O, File Stream Handling & Generic Programming (Templates)

---

## 5.1 C++ Stream Classes Hierarchy

In C++, Input/Output operations are performed using **streams**—an abstract byte sequence flowing into or out of a program. The C++ standard I/O library is organized into a robust object-oriented class hierarchy centered around the base class `ios_base`.

### The Complete C++ Stream Class Hierarchy Tree

```
                                  +------------------+
                                  |     ios_base     |  (Non-templated base: state flags, formatting)
                                  +------------------+
                                           ^
                                           |
                                  +------------------+
                                  |    basic_ios     |  (Type-specific stream state, streambuf link)
                                  |   (typedef ios)  |
                                  +------------------+
                                     /            \
                                    /              \
           +---------------------------+        +---------------------------+
           |       basic_istream       |        |       basic_ostream       |
           |      (typedef istream)    |        |      (typedef ostream)    |
           +---------------------------+        +---------------------------+
               ^                     \            /                      ^
               |                      \          /                       |
               |                  +------------------+                   |
               |                  |  basic_iostream  |                   |
               |                  | (typedef iostream|                   |
               |                  +------------------+                   |
               |                           ^                             |
               |                           |                             |
    +--------------------+       +--------------------+       +--------------------+
    |   basic_ifstream   |       |   basic_fstream    |       |   basic_ofstream   |
    | (typedef ifstream) |       | (typedef fstream)  |       | (typedef ofstream) |
    +--------------------+       +--------------------+       +--------------------+
```

### Roles of Key Stream Classes:
- **`ios_base`**: Topmost non-template base class. Defines format flags (`hex`, `fixed`, `scientific`), I/O state bits (`eofbit`, `failbit`), and seek directions (`beg`, `cur`, `end`).
- **`ios`**: Specializes `basic_ios<char>`. Holds the pointer to the underlying stream buffer (`streambuf`).
- **`istream`**: Handles character-oriented formatted and unformatted input. Defines `operator>>`, `get()`, `getline()`, `read()`, `seekg()`, `tellg()`. Global standard instance: **`std::cin`**.
- **`ostream`**: Handles character-oriented formatted and unformatted output. Defines `operator<<`, `put()`, `write()`, `seekp()`, `tellp()`. Global standard instances: **`std::cout`** (buffered stdout), **`std::cerr`** (unbuffered stderr), **`std::clog`** (buffered log).
- **`iostream`**: Derived via multiple inheritance from both `istream` and `ostream`. Supports bidirectional input and output on the same console stream.

---

## 5.2 Unformatted Console I/O Operations

Unformatted I/O functions transfer raw bytes between memory and streams without applying data conversions, whitespace skipping, or alignment rules.

### 1. `cin.get()`
Used to read raw characters including whitespaces, tabs, and newlines (which `operator>>` skips by default).
- **Variant 1 (Extract char)**: `char ch; cin.get(ch);` (Stores next character in `ch`).
- **Variant 2 (Return int)**: `int c = cin.get();` (Returns character as integer, or `EOF` when stream ends).
- **Variant 3 (Read string buffer)**: `cin.get(charBuffer, bufferSize, delimiter = '\n');`
  - Reads up to `bufferSize - 1` characters or until `delimiter` is encountered.
  - **Critical Nuance**: `get()` **leaves the delimiter character in the input stream**!

### 2. `cout.put()`
Writes a single character to the output stream.
- **Syntax**: `cout.put(char ch);`
- **Example**: `cout.put('A').put('\n');` (Supports method chaining by returning `ostream&`).

### 3. `cin.getline()`
Reads a full line of text including whitespace characters up to a designated delimiter or buffer boundary.
- **Syntax**: `cin.getline(char* buffer, int maxCount, char delimiter = '\n');`
- **Difference from `cin.get()`**: `getline()` **extracts AND DISCARDS the delimiter from the input stream**, positioning the stream pointer directly after the delimiter for subsequent read operations.

### 4. `cin.read()` and `cout.write()`
Used for bulk unformatted binary and block transfers.
- **`cin.read(char* buffer, streamsize n)`**: Reads exactly `n` raw bytes from the stream into `buffer`. Does not append a null terminator `\0`.
- **`cout.write(const char* buffer, streamsize n)`**: Writes exactly `n` raw bytes from `buffer` to the stream, ignoring any embedded `\0` characters.

```cpp
#include <iostream>

int main() {
    char text[50];
    std::cout << "Enter a full line of text: ";
    std::cin.getline(text, 50); // Reads whitespace cleanly

    std::cout << "Writing raw 10 characters using write(): ";
    std::cout.write(text, 10);
    std::cout.put('\n');
    return 0;
}
```

---

## 5.3 Formatted Console I/O Operations: `ios` Member Functions & Flags

The `ios` class manages an internal bitmask of formatting flags that dictate how numbers, strings, and padding are rendered.

### 5.3.1 `ios` Formatting Member Functions

| Member Function | Purpose & Description | Example Code |
|---|---|---|
| `width(int w)` | Sets the minimum field width for the **very next output field only** (resets to 0 immediately after!). | `cout.width(10); cout << 52;` |
| `precision(int p)`| Sets the number of significant digits (or decimal places when combined with `ios::fixed`). **Persistent**. | `cout.precision(2); cout << 3.14159;` $\rightarrow$ `3.1` (or `3.14` with `fixed`) |
| `fill(char ch)` | Sets the fill/padding character used when output occupies less than the set field width. **Persistent**. | `cout.fill('*'); cout.width(6); cout << 42;` $\rightarrow$ `****42` |
| `setf(fmtflags)` | Sets/enables specific format flag bits. | `cout.setf(ios::showpos);` (Prints `+` for positive numbers) |
| `unsetf(fmtflags)`| Clears/disables specific format flag bits. | `cout.unsetf(ios::showpos);` |

### 5.3.2 Bitmask Flag Management with `setf(flag, field)`
Certain format flags are mutually exclusive (e.g., you cannot have a number simultaneously formatted as left-aligned and right-aligned). Setting these flags safely requires the two-parameter overload `setf(flag, field)`:

```cpp
// 1. Base Field (dec, hex, oct)
std::cout.setf(std::ios::hex, std::ios::basefield); // Set Hexadecimal
std::cout << 255; // Prints: ff

// 2. Float Field (fixed, scientific)
std::cout.setf(std::ios::fixed, std::ios::floatfield); // Set Fixed-point decimal
std::cout.precision(3);
std::cout << 3.14159; // Prints: 3.142

// 3. Adjust Field (left, right, internal)
std::cout.setf(std::ios::left, std::ios::adjustfield); // Left alignment
std::cout.width(10);
std::cout << 45; // Prints: "45        "
```

---

## 5.4 Managing Output with Manipulators (`<iomanip>`)

**Manipulators** are special helper functions designed to be chained directly into stream insertion (`<<`) and extraction (`>>`) operations to control formatting cleanly.

### Comprehensive Comparison: `ios` Member Functions vs. Manipulators

| Feature | `ios` Member Functions (`width()`, `precision()`, etc.) | Manipulators (`setw()`, `setprecision()`, etc.) |
|---|---|---|
| **Header File** | Defined in standard `<iostream>`. | Parameterized manipulators require **`<iomanip>`**. |
| **Call Syntax** | Called as separate member statements: `cout.width(5);` | Chained inline inside stream operator: `cout << setw(5);` |
| **Return Value** | Returns prior formatting state. | Returns reference to the stream (`ostream&`). |
| **Code Readability**| Verbose and breaks expression flow. | Compact, declarative, and highly readable. |

### Standard Manipulators Reference Table

| Manipulator | Header | Persistence | Effect |
|---|---|---|---|
| `setw(int n)` | `<iomanip>` | **Non-persistent** (applies only to next item) | Sets field width to $n$ characters. |
| `setprecision(int n)`| `<iomanip>` | **Persistent** | Sets floating-point precision to $n$ places. |
| `setfill(char c)` | `<iomanip>` | **Persistent** | Sets padding fill character to $c$. |
| `endl` | `<iostream>` | One-shot | Inserts newline `'\n'` and flushes the stream buffer. |
| `flush` | `<iostream>` | One-shot | Flushes stream buffer without inserting a newline. |
| `ends` | `<iostream>` | One-shot | Inserts null character `'\0'`. |
| `ws` | `<iostream>` | One-shot | Extractor manipulator: eats leading whitespace. |
| `boolalpha` / `noboolalpha`| `<iostream>`| **Persistent** | Prints `bool` as `"true"`/`"false"` instead of `1`/`0`. |

### Creating Custom Manipulators
C++ allows developers to write custom manipulators to encapsulate repeated formatting styles:

```cpp
#include <iostream>
#include <iomanip>

// Custom parameterless output manipulator: Formats values as Indian Rupees currency
std::ostream& currencyINR(std::ostream& out) {
    out << "Rs. " << std::fixed << std::setprecision(2);
    return out;
}

// Custom parameterless output manipulator: Formats with divider
std::ostream& tabDivider(std::ostream& out) {
    out << "\t|\t";
    return out;
}

int main() {
    double price = 1450.75;
    std::cout << "Total Amount: " << currencyINR << price << std::endl;
    // Output: Total Amount: Rs. 1450.75
    return 0;
}
```

---

## 5.5 Working with Files: File Stream Classes & Modes

File operations in C++ are handled through the `<fstream>` header classes:
- **`ifstream`**: Input file stream. Derived from `istream`. Opens files in read mode (`ios::in`).
- **`ofstream`**: Output file stream. Derived from `ostream`. Opens files in write mode (`ios::out`).
- **`fstream`**: Bidirectional file stream. Derived from `iostream`. Supports simultaneous reading and writing.

### 5.5.1 Opening Files: Constructor vs. `open()`

```cpp
// Method 1: Using Stream Constructor (Binds and opens upon instantiation)
std::ofstream outFile("log.txt", std::ios::out | std::ios::app);

// Method 2: Using explicit open() function (Useful when reusing stream object)
std::ifstream inFile;
inFile.open("data.txt", std::ios::in);
```

---

### 5.5.2 File Modes & Bitmask Combinations

File modes are bitmask flags defined inside `std::ios`:

| File Mode Flag | Purpose & Exact Semantics |
|---|---|
| `ios::in` | Open for reading (Input). File **must already exist**, else open fails. |
| `ios::out` | Open for writing (Output). Creates file if non-existent. **TRUNCATES existing file by default**! |
| `ios::app` | Append mode. Opens file; **forces every write operation to the end of the file**. Does not truncate. |
| `ios::ate` | "At-the-End". Opens file and moves pointer to the end immediately. **Allows random access seeking**! |
| `ios::trunc` | Truncate mode. If file exists, discards its previous contents (length becomes 0). |
| `ios::binary` | Binary mode. Opens file in raw binary format, suppressing CR/LF translation (`\r\n` $\leftrightarrow$ `\n`). |

#### The Crucial Exam Trap: `ios::app` vs. `ios::ate` (Quiz 3 Question 17)
> **Academic Distinction**:
> Both modes position the file pointer at the end of the file upon opening.
> - In **`ios::app` (Append Mode)**, the write pointer is **permanently pinned to the end of the file**. Even if you explicitly call `seekp(0, ios::beg)`, any subsequent write operation will automatically jump back to the end of the file and append!
> - In **`ios::ate` (At-the-End Mode)**, the initial position is moved to the end of the file upon opening, but you **can freely reposition the write pointer** using `seekp` anywhere in the file to overwrite existing data!

#### Does Opening with `ios::out | ios::in` Truncate an Existing File? (Quiz 3 Question 5 & 16)
> When `ios::out` is used alone, it implies `ios::trunc` (truncating existing data).
> However, combining **`ios::out | ios::in` preserves existing content without truncating**!

---

### 5.5.3 Detecting End-of-File and Stream State Bits

The stream state is monitored via four internal error bits:
- **`goodbit`**: No errors. Stream is healthy. Checked via `stream.good()`.
- **`eofbit`**: End-of-File reached during read. Checked via `stream.eof()`.
- **`failbit`**: Logical error (e.g., trying to read an integer but encountering text). Checked via `stream.fail()`.
- **`badbit`**: Fatal hardware/I/O corruption. Checked via `stream.bad()`.
- **`stream.clear()`**: Clears all error flags, restoring the stream to `good` state so further operations can proceed.

---

## 5.6 File Pointers and Random Access Manipulators

C++ file streams maintain two independent internal byte-offset pointers:
- **`get` pointer**: The read pointer (associated with `ifstream` and `fstream`).
- **`put` pointer**: The write pointer (associated with `ofstream` and `fstream`).

```
                              FILE BUFFER
   [ Byte 0 ] [ Byte 1 ] [ Byte 2 ] ... [ Byte N-2 ] [ Byte N-1 ] [ EOF ]
       ^                      ^                                       ^
       |                      |                                       |
    ios::beg               ios::cur                                ios::end
 (Start of file)      (Current position)                        (End of file)
```

### 1. `tellg()` and `tellp()` (Querying Positions)
- `streampos tellg();`: Returns the current byte offset of the **read (get)** pointer from the start of the file.
- `streampos tellp();`: Returns the current byte offset of the **write (put)** pointer from the start of the file.

### 2. `seekg()` and `seekp()` (Repositioning File Pointers)
- **Absolute Positioning**:
  - `seekg(pos)`: Moves read pointer to byte offset `pos`.
  - `seekp(pos)`: Moves write pointer to byte offset `pos`.
- **Relative Positioning**:
  - `seekg(offset, direction)`: Moves read pointer by `offset` bytes relative to `direction`.
  - `seekp(offset, direction)`: Moves write pointer by `offset` bytes relative to `direction`.
  - Valid `direction` constants: `ios::beg` (from start), `ios::cur` (from current position), `ios::end` (from end of file).

---

## 5.7 Binary File Operations & Object Serialization

Text I/O converts in-memory binary values into ASCII strings (e.g., integer `12345` takes 5 bytes as ASCII characters `'1' '2' '3' '4' '5'`). Binary file I/O writes raw memory bytes directly to disk (integer `12345` takes exactly 4 raw bytes), preserving data fidelity, speed, and compact storage.

### The Binary I/O Syntax:
```cpp
// Writing an object:
stream.write(reinterpret_cast<const char*>(&obj), sizeof(obj));

// Reading an object:
stream.read(reinterpret_cast<char*>(&obj), sizeof(obj));
```
- `reinterpret_cast<char*>` converts the typed pointer into a byte-level `char*` pointer required by stream buffers.

---

### 5.7.1 Complete Master Implementation: Random Access Binary File Updating (End-Sem 2024 Exam Question 9)

> **Complete Examination Problem Specification**:
> 1. Define structure `Student` with: `name` (fixed char array to ensure uniform record size), `rollNo` (int), `marks` (float).
> 2. Initialize 5 static student records:
>    - S1: ("ABC", 101, 85.5)
>    - S2: ("DEF", 102, 90.0)
>    - S3: ("GHI", 103, 88.5)
>    - S4: ("JKL", 104, 92.0)
>    - S5: ("XYZ", 105, 95.0)
> 3. Write records to binary file `students.dat`.
> 4. Modify 2nd student's ('DEF') marks to 93.5 using `seekp` and verify write position with `tellp`.
> 5. Read the 3rd record ('GHI') using `seekg` and display its details.

```cpp
#include <iostream>
#include <fstream>
#include <cstring>
#include <iomanip>

// a) Fixed-size POD structure suitable for binary serialization
struct Student {
    char name[20]; // Using char array to guarantee fixed sizeof(Student)
    int rollNo;
    float marks;

    void display() const {
        std::cout << "Roll No: " << rollNo 
                  << " | Name: " << std::left << std::setw(6) << name 
                  << " | Marks: " << std::fixed << std::setprecision(1) << marks << std::endl;
    }
};

int main() {
    const char* filename = "students.dat";

    // b) Initialize 5 static student records
    Student students[5] = {
        {"ABC", 101, 85.5f},
        {"DEF", 102, 90.0f},
        {"GHI", 103, 88.5f},
        {"JKL", 104, 92.0f},
        {"XYZ", 105, 95.0f}
    };

    // c) Write the 5 records to binary file students.dat
    std::ofstream outFile(filename, std::ios::out | std::ios::binary);
    if (!outFile) {
        std::cerr << "Error opening file for writing!\n";
        return 1;
    }

    for (int i = 0; i < 5; ++i) {
        outFile.write(reinterpret_cast<const char*>(&students[i]), sizeof(Student));
    }
    outFile.close();
    std::cout << "[Step c] 5 student records written successfully to " << filename << std::endl;

    // d & e) Open file for bidirectional random access update
    // Note: Use ios::in | ios::out | ios::binary to PREVENT truncation!
    std::fstream file(filename, std::ios::in | std::ios::out | std::ios::binary);
    if (!file) {
        std::cerr << "Error opening file for read/write!\n";
        return 1;
    }

    // Target: Modify second student's ('DEF', index 1) marks to 93.5
    // Byte offset for 2nd record: 1 * sizeof(Student)
    std::streampos record1Pos = 1 * sizeof(Student);
    file.seekp(record1Pos, std::ios::beg); // Seek write pointer to record index 1

    std::cout << "[Step e] Write pointer positioned at byte: " << file.tellp() 
              << " (Expected: " << record1Pos << ")" << std::endl;

    // Read current 2nd record to preserve name and rollNo, modify marks
    Student defStudent;
    file.seekg(record1Pos, std::ios::beg);
    file.read(reinterpret_cast<char*>(&defStudent), sizeof(Student));
    defStudent.marks = 93.5f; // Update marks

    // Reposition write pointer back to record 1 and overwrite
    file.seekp(record1Pos, std::ios::beg);
    file.write(reinterpret_cast<const char*>(&defStudent), sizeof(Student));
    std::cout << "[Step d] Updated DEF marks to 93.5. Current tellp: " << file.tellp() << std::endl;

    // f) Read the 3rd record ('GHI', index 2) from the file and display
    std::streampos record2Pos = 2 * sizeof(Student);
    file.seekg(record2Pos, std::ios::beg);

    Student ghiStudent;
    file.read(reinterpret_cast<char*>(&ghiStudent), sizeof(Student));
    std::cout << "\n[Step f] Successfully read 3rd record from file:\n";
    ghiStudent.display();

    file.close();
    return 0;
}
```

---

## 5.8 Generic Programming: Function Templates & Class Templates

**Generic Programming** is an architectural paradigm wherein algorithms and data structures are authored in terms of generalized types to be specified later upon instantiation. In C++, this is realized via **Templates**.
- **Compile-Time Code Generation (Monomorphization)**: The compiler generates a concrete, type-specific instantiation of the function or class for each unique type combination used, resulting in **zero runtime penalty** compared to hand-written type-specific code.

---

### 5.8.1 Function Templates

#### Syntax
```cpp
template <typename T>
T findMax(T a, T b) {
    return (a > b) ? a : b;
}
```

#### Function Template with Multiple Parameters of Different Types (End-Sem 2024 Exam Question 8b)
> **Exam Question**: *"What is a function template with a parameter in C++? Provide a code snippet demonstrating a template function that finds the maximum of two numbers of different types (e.g., int, float, double)."*

```cpp
#include <iostream>

// Function template accepting two arguments of distinct types T1 and T2
// Uses common auto return type deduction (or common_type)
template <typename T1, typename T2>
auto getMax(T1 a, T2 b) -> decltype((a > b) ? a : b) {
    return (a > b) ? a : b;
}

int main() {
    int x = 45;
    double y = 88.75;
    float z = 92.4f;

    std::cout << "Max between int (" << x << ") and double (" << y << ") is: " 
              << getMax(x, y) << std::endl; // Returns double 88.75

    std::cout << "Max between float (" << z << ") and int (" << x << ") is: " 
              << getMax(z, x) << std::endl; // Returns float 92.4
    return 0;
}
```

#### Overloading Function Templates: Resolution Hierarchy
A function template can be overloaded by regular non-template functions or other templates:
1. **Rule 1**: An exact match non-template function is **always preferred over a template function**.
2. **Rule 2**: If no non-template match exists, the most specialized template is selected.
3. **Explicit Specialization Syntax**:
   ```cpp
   template <>
   const char* getMax<const char*>(const char* a, const char* b) {
       return (std::strcmp(a, b) > 0) ? a : b;
   }
   ```

---

### 5.8.2 Class Templates

Class templates enable the creation of generic containers (such as generic stacks, queues, and vectors).

```cpp
#include <iostream>

template <class T>
class GenericStack {
private:
    T* stackArray;
    int topIndex;
    int capacity;

public:
    GenericStack(int cap = 10) : capacity(cap), topIndex(-1) {
        stackArray = new T[capacity];
    }

    ~GenericStack() {
        delete[] stackArray;
    }

    void push(const T& element) {
        if (topIndex < capacity - 1) {
            stackArray[++topIndex] = element;
        } else {
            std::cerr << "Stack Overflow!\n";
        }
    }

    T pop() {
        if (topIndex >= 0) {
            return stackArray[topIndex--];
        }
        throw std::underflow_error("Stack Underflow!");
    }

    bool isEmpty() const { return topIndex == -1; }
};

int main() {
    GenericStack<int> intStack(5);
    intStack.push(10);
    intStack.push(20);
    std::cout << "Popped: " << intStack.pop() << std::endl;

    GenericStack<std::string> strStack(5);
    strStack.push("Object");
    strStack.push("Oriented");
    std::cout << "Popped: " << strStack.pop() << std::endl;
    return 0;
}
```

#### Non-Type Template Parameters
Templates can accept compile-time values (such as integers or sizes) in addition to types:
```cpp
template <typename T, int Size>
class StaticBuffer {
    T buffer[Size]; // Statically sized array on stack!
public:
    int getSize() const { return Size; }
};
// Instantiation:
StaticBuffer<double, 1024> audioBuffer;
```



---

# BONUS EXAM MASTERY: Exception Handling, Modern Type Casting & STL Architecture

---

## B.1 Exception Handling in C++

Exception handling provides a type-safe, structured mechanism to transfer control and unwind the stack when anomalous runtime errors occur.

### The `try`, `catch`, and `throw` Architecture
- **`throw`**: Signals the occurrence of an exceptional error by creating and dispatching an exception object.
- **`try`**: Encloses a block of code that may potentially throw an exception.
- **`catch`**: Handles the thrown exception based on matching the exception's exact data type.

```
[Normal Execution inside try block]
                 |
        (Error Condition Met)
                 |
                 v
         [throw ExceptionObject]
                 |
                 v  (Stack Unwinding: Local stack objects destroyed in reverse order)
                 |
    +------------+------------+
    |                         |
    v                         v
[catch (Type1 e)]        [catch (Type2 e)]  -----> [Handle and recover]
```

---

### B.1.1 Handling Multiple Exceptions with Multiple Catch Blocks (End-Sem 2024 Exam Question 8a)

> **Exam Question**: *"In C++, how can you handle multiple exceptions of different types using catch blocks? Provide an example demonstrating this."*

A single `try` block can be followed by multiple consecutive `catch` blocks, each configured to handle a distinct exception type:

```cpp
#include <iostream>
#include <string>
#include <stdexcept>

void processTransaction(int accountType, double amount) {
    if (accountType < 1 || accountType > 3) {
        throw accountType; // Throws an integer error code
    }
    if (amount <= 0) {
        throw "Invalid transaction amount: must be positive!"; // Throws const char*
    }
    if (amount > 100000.0) {
        throw std::runtime_error("Amount exceeds maximum single transaction limit!");
    }
    std::cout << "Transaction processed successfully for amount: $" << amount << std::endl;
}

int main() {
    double amountsToTest[] = { -50.0, 200000.0, 500.0 };

    for (double testAmount : amountsToTest) {
        try {
            std::cout << "\nAttempting transaction with amount: " << testAmount << std::endl;
            processTransaction(1, testAmount);
        }
        // Catch Block 1: Catches integer exception
        catch (int errorCode) {
            std::cerr << "[Caught int Exception] Invalid account type code: " << errorCode << std::endl;
        }
        // Catch Block 2: Catches string literal exception (const char*)
        catch (const char* errorMsg) {
            std::cerr << "[Caught const char* Exception] Error: " << errorMsg << std::endl;
        }
        // Catch Block 3: Catches standard library exceptions by reference
        catch (const std::exception& ex) {
            std::cerr << "[Caught std::exception] System error: " << ex.what() << std::endl;
        }
        // Catch-All Block: Catches any other unanticipated exception types
        // Must ALWAYS be placed at the very end of the catch list!
        catch (...) {
            std::cerr << "[Caught Unknown Exception] An unexpected error occurred.\n";
        }
    }
    return 0;
}
```

---

### B.1.2 High-Probability Exception Traps (From Quizzes & Exams)

#### Trap 1: Throwing `const char*` vs. Catching `char*` (Quiz 3 Question 2)
```cpp
try {
    throw "Error occurred"; // "Error occurred" is a string literal of type 'const char*'
} catch (char* msg) {       // ❌ WILL NOT MATCH! const char* cannot bind to non-const char*
    std::cout << msg;
}
```
- **Consequence**: The exception is **NOT caught** by `catch (char*)`. If no other matching catch block or `catch(...)` exists, the runtime immediately calls `std::terminate()`, aborting the program.

#### Trap 2: No Type Promotion in Catch Blocks (Quiz 3 Question 18)
```cpp
try {
    throw 10; // Throws int
} catch (char c) { // ❌ WILL NOT MATCH!
    std::cout << "Caught char";
}
```
- **Rule**: Catch block matching is **strictly invariant**. Unlike normal function overloading, **no numeric conversions or promotions (e.g., `int` -> `char` or `float` -> `double`) occur during exception matching**.

#### Trap 3: Rethrowing Exceptions with `throw;` (Quiz 3 Question 4 & 14)
- **Valid Usage (Nested Rethrow)**: Inside an active `catch` block, writing `throw;` rethrows the current exception up the call stack to enclosing `try-catch` scopes.
- **The Empty `throw;` Trap**: Executing `throw;` when **no exception is currently being handled** immediately invokes `std::terminate()`.

---

## B.2 Modern C++ Explicit Type Casting Operators

Legacy C-style casts `(Type)expression` are perilous: they are syntactically indistinguishable from parentheses, search for any conversion sequence without restriction, and bypass the compiler's type system. C++ introduces four distinct, intention-revealing explicit cast operators:

```cpp
cast_name<TargetType>(expression)
```

### Comprehensive Comparison of the Four C++ Casts

| Cast Operator | Primary Use Case | Compile-Time vs Run-Time | Safety & Validity Restrictions |
|---|---|---|---|
| **`static_cast`** | Standard numeric conversions (`double` $\rightarrow$ `int`), safe upcasting in inheritance hierarchies, void pointer conversion. | **Compile-Time** | Rejects casting between unrelated pointer types (e.g., cannot cast `double*` to `int*`). |
| **`dynamic_cast`**| Safe polymorphic downcasting (`Base*` $\rightarrow$ `Derived*`) along an inheritance tree. | **Run-Time** (Uses RTTI) | **Requires at least one virtual function** in the base class. Returns `nullptr` on pointer failure; throws `std::bad_cast` on reference failure. **Illegal for primitive types**! |
| **`const_cast`**  | Adds or strips away `const` or `volatile` qualifiers from a pointer or reference. | **Compile-Time** | Target type must be identical except for cv-qualifiers. Cannot change underlying data type. |
| **`reinterpret_cast`** | Low-level bitwise reinterpretation of memory addresses (e.g., pointer to integer, `Student*` to `char*`). | **Compile-Time** | Extremely dangerous. Bypasses all type checking. Hardware/driver level. |

---

### Detailed Walkthrough of Quiz 3 Casting Problems:

1. **Why `static_cast` cannot convert unrelated pointer types (Quiz 3, Q1 & Q12)**:
   ```cpp
   int x = 10;
   double* ptr = static_cast<double*>(&x); // ❌ COMPILE ERROR!
   ```
   *Explanation*: `int` and `double` have fundamentally incompatible physical bit-level memory layouts (two's complement integer vs. IEEE 754 floating-point exponent/mantissa) and different sizes (4 bytes vs. 8 bytes). Dereferencing a `double*` that points to a 4-byte `int` would read 4 out-of-bounds garbage bytes from adjacent memory. `static_cast` refuses to perform this conversion because no standard pointer conversion exists between unrelated types. (Requires `reinterpret_cast`).

2. **Converting to and from `void*` with `static_cast` (Quiz 3, Q3)**:
   ```cpp
   int x = 100;
   int* ptr = &x;
   void* v = static_cast<void*>(ptr); // ✅ FULLY VALID!
   ```
   *Explanation*: Under ISO C++, any object pointer can be safely converted to `void*` and back to its original typed pointer using `static_cast`.

3. **Modifying a True `const` Variable via `const_cast` (Quiz 3, Q11, Q19)**:
   ```cpp
   const int x = 10;
   int* p = const_cast<int*>(&x);
   *p = 20; // ⚠️ UNDEFINED BEHAVIOR!
   std::cout << x << " " << *p;
   ```
   *Explanation*: If the original variable `x` was declared `const`, modifying its memory via `*p = 20` produces **Undefined Behavior**. The compiler is legally entitled to store `const int x` in a read-only memory segment (causing a segmentation fault on write), or perform **constant folding** (propagating the literal `10` into `std::cout << x`, so output prints `10 20` even if RAM changed!). `const_cast` is safe ONLY when casting away `const` on a pointer that originally pointed to a non-const variable!

---

## B.3 Standard Template Library (STL) Architecture (End-Sem 2024 Exam Question 10)

> **Exam Question**: *"In C++, what does the Standard Template Library (STL) refer to? Describe the function of containers within the STL and list at least three types of containers, providing examples for each."*

### Definition & Architecture of the STL
The **Standard Template Library (STL)** is a foundational software library included in standard C++ that provides generic, reusable, type-safe data structures and algorithms. The architecture is built upon three orthogonal components:
1. **Containers**: Generic data structures managing collections of objects in memory.
2. **Algorithms**: Generic functions (e.g., `std::sort`, `std::find`, `std::binary_search`) executing computational procedures on container elements.
3. **Iterators**: Pointer-like navigational abstractions that bridge algorithms and containers, allowing algorithms to operate uniformly across any container without knowing its internal memory layout.

```
+--------------------+                       +--------------------+
|     CONTAINER      |                       |     ALGORITHM      |
| (vector, list, etc)|                       | (sort, find, etc.) |
+--------------------+                       +--------------------+
          \                                     /
           \                                   /
            v                                 v
        +-----------------------------------------+
        |                ITERATOR                 |
        |  (begin(), end(), ++, *, bidirectional) |
        +-----------------------------------------+
```

---

### The Function of Containers and Taxonomy of Container Types

**Function of Containers**: Containers encapsulate dynamic memory allocation, element storage, growth heuristics, and boundary management, providing high-performance, bug-free data structure implementations.

The STL provides four fundamental categories of containers:

#### 1. Sequence Containers
Store elements in a strictly linear, sequential order where each element has a position dependent on the time and place of insertion.
- **`std::vector<T>`**: Dynamic contiguous array. Fast random access $O(1)$; amortized $O(1)$ insertion at tail.
  ```cpp
  #include <vector>
  std::vector<int> numbers = {10, 20, 30};
  numbers.push_back(40); // Fast dynamic growth
  ```
- **`std::list<T>`**: Doubly linked list. Non-contiguous memory. Fast $O(1)$ insertion and deletion anywhere once iterator is positioned; no random access ($O(N)$ traversal).
- **`std::deque<T>`**: Double-ended queue. Chunks of contiguous arrays. Fast insertion and deletion at both head and tail in $O(1)$.

#### 2. Associative Containers
Implement sorted, key-based collections typically backed by balanced binary search trees (Red-Black Trees). Elements are automatically maintained in sorted order.
- **`std::set<T>`**: Collection of unique, sorted keys. Search, insertion, and deletion operate in $O(\log N)$ time.
  ```cpp
  #include <set>
  std::set<int> uniqueScores;
  uniqueScores.insert(95);
  uniqueScores.insert(82);
  uniqueScores.insert(95); // Duplicate ignored!
  ```
- **`std::map<Key, Value>`**: Collection of sorted Key-Value pairs where each key is unique. Supports subscript operator `map[key]`.
  ```cpp
  #include <map>
  std::map<std::string, int> ageMap;
  ageMap["Alice"] = 21;
  ageMap["Bob"] = 22;
  ```

#### 3. Unordered Associative Containers
Implement key-value collections backed by **Hash Tables**.
- **`std::unordered_map<Key, Value>`** / **`std::unordered_set<T>`**: Average case $O(1)$ search, insertion, and deletion using hash bucket indices.

#### 4. Container Adapters
Provide constrained, specialized interfaces built on top of underlying sequence containers:
- **`std::stack<T>`**: LIFO data structure (`push`, `pop`, `top`).
- **`std::queue<T>`**: FIFO data structure (`push`, `pop`, `front`).
- **`std::priority_queue<T>`**: Max-heap implementation (`push`, `pop`, `top`).

---

# COMPREHENSIVE PYQ DIRECT MAPPING & SOLUTION MATRIX

This matrix maps every past examination question from recent mid-semester, end-semester, and quiz papers directly to the corresponding sections and worked implementations in this Master Guide.

| Exam Paper | Question No. | Core Concept / Problem Statement | Direct Section Reference in this Guide |
|---|---|---|---|
| **End-Sem Dec 2024 (CSE/DSE)** | Q1 (a) | Encapsulation, data security, all attributes public & methods private | **Section 1.3 (Concept 4) & 1.8 (Q1)** |
| **End-Sem Dec 2024 (CSE/DSE)** | Q1 (b) | Default arguments right-to-left violation: `void example(int x, int y = 5, int z)` | **Section 1.5.6 & Section 1.8 (Q2)** |
| **End-Sem Dec 2024 (CSE/DSE)** | Q2 (a) | Why static member function can only access static members & no `this` pointer | **Section 2.8 (Exam Justification)** |
| **End-Sem Dec 2024 (CSE/DSE)** | Q2 (b) | Constructor parameter name same as member variable (name shadowing & `this->`) | **Section 3.1.6** |
| **End-Sem Dec 2024 (CSE/DSE)** | Q3 (a) | Pass by value vs. Pass by reference trade-offs and scenarios | **Section 1.5.5** |
| **End-Sem Dec 2024 (CSE/DSE)** | Q3 (b) | Friend class & friend function transitivity rule (Class A, B and non-member print) | **Section 2.9.3 (Complete Proof & Code)** |
| **End-Sem Dec 2024 (CSE/DSE)** | Q4 (a) | Can constructor be explicitly invoked like a regular member function? | **Section 3.1.7** |
| **End-Sem Dec 2024 (CSE/DSE)** | Q4 (b) | Default constructor vs. Constructor with default parameters | **Section 3.1.2 & 3.1.5** |
| **End-Sem Dec 2024 (CSE/DSE)** | Q5 (a-d) | Class `Temperature` (Celsius), member func & conversion operator to float (Fahrenheit) | **Section 3.5 (Worked Implementation)** |
| **End-Sem Dec 2024 (CSE/DSE)** | Q6 (a) | Multiple inheritance ambiguity with same function signature & resolution | **Section 4.2.1** |
| **End-Sem Dec 2024 (CSE/DSE)** | Q6 (b) | Abstract class constructor call sequence & explicit invocation rules | **Section 4.2.2, 4.4 & 4.8.2** |
| **End-Sem Dec 2024 (CSE/DSE)** | Q7 (a-c) | `Shape`, `Circle`, `Rectangle`, and `Graphics` containership & dynamic polymorphism | **Section 4.8.3 (Full Code Solution)** |
| **End-Sem Dec 2024 (CSE/DSE)** | Q8 (a) | Handling multiple exceptions of different types using multiple catch blocks | **Section B.1.1** |
| **End-Sem Dec 2024 (CSE/DSE)** | Q8 (b) | Function template with parameters of different types finding maximum | **Section 5.8.1 (Code Solution)** |
| **End-Sem Dec 2024 (CSE/DSE)** | Q9 (a-f) | Binary file operations with `Student` struct, `seekp`, `tellp`, updating record in `students.dat` | **Section 5.7.1 (Complete Working Program)** |
| **End-Sem Dec 2024 (CSE/DSE)** | Q10 | STL definition, function of containers, and 3 types with examples | **Section B.3** |
| **End-Sem Nov 2024 (IT)** | Q1 (a) | POP vs. OOP comparison, modularity, reusability, and problem solving | **Section 1.1 & 1.2** |
| **End-Sem Nov 2024 (IT)** | Q1 (b) | Data hiding and accessing private members without member functions (Friendship) | **Section 1.3 & Section 2.9** |
| **End-Sem Nov 2024 (IT)** | Q2 (a) | Dynamic initialization of objects with practical code example | **Section 3.1.4 (FixedDeposit Code)** |
| **End-Sem Nov 2024 (IT)** | Q2 (b) | Static data members and static functions memory allocation & active instance counter | **Section 2.7 & 2.8 (InstanceCounter Code)** |
| **End-Sem Nov 2024 (IT)** | Q3 (a) | Destructor purpose, significance, and ensuring heap deallocation on scope exit | **Section 3.2** |
| **End-Sem Nov 2024 (IT)** | Q3 (b) | Class `Time` adding two time objects via overloaded binary `+` operator | **Section 3.4.4 (Full Time Class Code)** |
| **End-Sem Nov 2024 (IT)** | Q4 (a) | Pointer to derived class, virtual functions, and runtime polymorphism | **Section 4.6 & Section 4.7** |
| **End-Sem Nov 2024 (IT)** | Q4 (b) | Abstract class `Animal`, derived `Dog` and `Bird`, array of pointers | **Section 4.8** |
| **End-Sem Nov 2024 (IT)** | Q5 (a) | Containership definition and example of member instance | **Section 4.3 & Section 4.8.3** |
| **End-Sem Nov 2024 (IT)** | Q5 (b) | Hierarchy diagram of `ifstream`, `ofstream`, `fstream` and usage | **Section 5.1 & Section 5.5** |
| **End-Sem Nov 2024 (IT)** | Q5 (c) | C++ file program: input array, write sum to file, reopen and display | **Section 5.5 & Section 5.7** |
| **Mid-Sem Sept 2025** | Q1 | Function taking integer by reference and squaring in place | **Section 1.5.5** |
| **Mid-Sem Sept 2025** | Q2 | Hospital Management OOP design: `Person`, `Patient`, `Doctor`, friend function | **Section 2.9 & Unit 4** |
| **Mid-Sem Sept 2025** | Q3 (a-f) | Output tracing: virtual base classes, const objects, friend functions, copy constructors | **Sections 3.1.2, 3.1.3, 4.2.2 & 4.7** |
| **Mid-Sem Sept 2025** | Q4 (i-v) | Operator overloading member vs friend, inline static vars, returning local ref | **Sections 1.5.3, 1.5.4 & 3.4.2** |
| **Quiz 2 (Nov 2025)** | Q1-Q16 | Uninitialized pointer, overload vs override, pointer swap trap, VTABLE dispatch, diamond ambiguity | **Sections 1.5.5, 3.3, 4.2.2, 4.7 & B.2** |
| **Quiz 3 (Nov 2025)** | Q1-Q21 | Explicit casts (`static_cast`, `const_cast`), exception matching, file modes (`ios::ate` vs `ios::app`) | **Sections 5.5.2, B.1 & B.2** |

---
**END OF MASTER BOOK: OBJECT-ORIENTED PROGRAMMING IN C++ (ITDC0201)**
