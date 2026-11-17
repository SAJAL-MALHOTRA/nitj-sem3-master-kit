# Data Structures Lab — Experiment 6
## Stack Implementation and Applications in C++

> **Language:** C++  
> **Implementation:** Array-based stack  
> **Experiment:** Implement stack using an array and perform `push()` and `pop()` operations.

---

# 1. What is a Stack?

A **stack** is a linear data structure that follows **LIFO — Last In, First Out**.

Think of a stack of plates:

```text
       TOP
        ↓
     +-----+
     |  C  |  ← removed first
     +-----+
     |  B  |
     +-----+
     |  A  |
     +-----+
```

The last element inserted is the first element removed.

All main operations happen at the **top**.

---

# 2. Basic Stack Operations

| Operation | Meaning |
|---|---|
| `push()` | Add an element to the top |
| `pop()` | Remove the top element |
| `peek()` | See the top element without removing it |
| `isEmpty()` | Check whether the stack is empty |
| `isFull()` | Check whether the stack is full |

For an array-based stack, these basic operations take **O(1)** time.

---

# 3. The Most Important Variable: `top`

For an array stack, we keep an integer called `top`.

Initially:

```cpp
top = -1;
```

Why `-1`?

Because there is no element in the stack yet.

For an array:

```text
Index:   0   1   2   3   4
         -------------------
Array:  [ ] [ ] [ ] [ ] [ ]
top = -1
```

After pushing `10`:

```text
Index:   0   1   2   3   4
         -------------------
Array:  [10][ ] [ ] [ ] [ ]
          ↑
         top
top = 0
```

After pushing `20`:

```text
Array:  [10][20][ ] [ ] [ ]
             ↑
            top
top = 1
```

---

# 4. Basic Array Stack Code

This is the core stack code. Learn this first because the assignment programs are built around the same idea.

```cpp
#include <iostream>
using namespace std;

#define SIZE 5

class Stack {
private:
    int arr[SIZE];
    int top;

public:
    Stack() {
        top = -1;
    }

    void push(int value) {
        if (top == SIZE - 1) {
            cout << "Stack Overflow\n";
            return;
        }

        top++;
        arr[top] = value;
    }

    int pop() {
        if (top == -1) {
            cout << "Stack Underflow\n";
            return -1;
        }

        int value = arr[top];
        top--;
        return value;
    }

    int peek() {
        if (top == -1) {
            cout << "Stack is empty\n";
            return -1;
        }

        return arr[top];
    }

    bool isEmpty() {
        return top == -1;
    }

    bool isFull() {
        return top == SIZE - 1;
    }
};

int main() {
    Stack s;

    s.push(10);
    s.push(20);
    s.push(30);

    cout << "Top element: " << s.peek() << endl;

    cout << "Removed: " << s.pop() << endl;
    cout << "Removed: " << s.pop() << endl;

    cout << "Top element: " << s.peek() << endl;

    return 0;
}
```

---

# 5. Understanding `push()`

The purpose of `push()` is to **insert an element at the top**.

```cpp
void push(int value) {
    if (top == SIZE - 1) {
        cout << "Stack Overflow\n";
        return;
    }

    top++;
    arr[top] = value;
}
```

### Step 1 — Check Overflow

```cpp
if (top == SIZE - 1)
```

If the array has size `5`, the last valid index is `4`.

So:

```text
top == 4
```

means the stack is full.

### Step 2 — Move `top`

```cpp
top++;
```

### Step 3 — Store the value

```cpp
arr[top] = value;
```

So the basic logic is:

```text
CHECK → MOVE TOP → INSERT
```

---

# 6. Understanding `pop()`

The purpose of `pop()` is to **remove the top element**.

```cpp
int pop() {
    if (top == -1) {
        cout << "Stack Underflow\n";
        return -1;
    }

    int value = arr[top];
    top--;
    return value;
}
```

### Step 1 — Check Underflow

```cpp
if (top == -1)
```

If `top == -1`, there is nothing to remove.

### Step 2 — Save the top value

```cpp
int value = arr[top];
```

### Step 3 — Move `top` down

```cpp
top--;
```

### Step 4 — Return removed value

```cpp
return value;
```

So:

```text
CHECK → SAVE → MOVE TOP → RETURN
```

---

# 7. Overflow vs Underflow

### Overflow

Trying to `push()` into a full stack.

```text
Stack:
[10][20][30][40][50]
                  ↑
                 top

push(60) → OVERFLOW
```

### Underflow

Trying to `pop()` from an empty stack.

```text
[ ][ ][ ][ ][ ]
 ↑
top = -1

pop() → UNDERFLOW
```

---

# 8. Assignment Question 1
## Reverse a String Using Stack

The assignment asks us to reverse a string using **push and pop**, without using a built-in reverse function. The example is:

```text
Input:  algorithm
Output: mtirogla
```

---

## Logic

Suppose:

```text
algorithm
```

Push every character:

```text
a → l → g → o → r → i → t → h → m
```

The stack becomes:

```text
TOP
 ↓
[m]
[h]
[t]
[i]
[r]
[o]
[g]
[l]
[a]
```

Now pop everything:

```text
m h t i r o g l a
```

Therefore:

```text
algorithm → mtirogla
```

---

## C++ Program

```cpp
#include <iostream>
#include <string>
using namespace std;

#define SIZE 100

class Stack {
    char arr[SIZE];
    int top;

public:
    Stack() {
        top = -1;
    }

    void push(char ch) {
        if (top == SIZE - 1)
            return;

        arr[++top] = ch;
    }

    char pop() {
        if (top == -1)
            return '\0';

        return arr[top--];
    }

    bool isEmpty() {
        return top == -1;
    }
};

int main() {
    string str;
    cin >> str;

    Stack s;

    for (char ch : str)
        s.push(ch);

    while (!s.isEmpty())
        cout << s.pop();

    return 0;
}
```

### Important idea

```cpp
for (char ch : str)
    s.push(ch);
```

puts every character into the stack.

Then:

```cpp
while (!s.isEmpty())
    cout << s.pop();
```

prints characters in reverse order.

### Complexity

```text
Time:  O(n)
Space: O(n)
```

---

# 9. Assignment Question 2
## Check Balanced Brackets

We need to determine whether:

```text
()
{}
[]
```

are correctly opened and closed.

Examples:

```text
{[()]}  → True
{[(])}  → False
```

---

## Logic

When we see an opening bracket:

```text
( { [
```

we **push** it.

When we see a closing bracket:

```text
) } ]
```

we check the top of the stack.

For example:

```text
{ [ ( ) ] }
```

Process:

```text
{  → push
[  → push
(  → push
)  → matches (
]  → matches [
}  → matches {
```

At the end, the stack must be empty.

---

## C++ Program

```cpp
#include <iostream>
#include <string>
using namespace std;

#define SIZE 100

class Stack {
    char arr[SIZE];
    int top;

public:
    Stack() {
        top = -1;
    }

    void push(char ch) {
        if (top < SIZE - 1)
            arr[++top] = ch;
    }

    char pop() {
        if (top == -1)
            return '\0';

        return arr[top--];
    }

    char peek() {
        if (top == -1)
            return '\0';

        return arr[top];
    }

    bool isEmpty() {
        return top == -1;
    }
};

bool matches(char open, char close) {
    return (open == '(' && close == ')') ||
           (open == '{' && close == '}') ||
           (open == '[' && close == ']');
}

int main() {
    string str;
    cin >> str;

    Stack s;

    for (char ch : str) {

        if (ch == '(' || ch == '{' || ch == '[') {
            s.push(ch);
        }

        else if (ch == ')' || ch == '}' || ch == ']') {

            if (s.isEmpty()) {
                cout << "False";
                return 0;
            }

            char open = s.pop();

            if (!matches(open, ch)) {
                cout << "False";
                return 0;
            }
        }
    }

    cout << (s.isEmpty() ? "True" : "False");

    return 0;
}
```

### Key condition

```cpp
if (!matches(open, ch))
```

checks whether the opening and closing brackets belong together.

### Complexity

```text
Time:  O(n)
Space: O(n)
```

---

# 10. Operator Precedence

For infix conversion, remember:

```text
Highest
   ^
   |
 *, /
   |
 +, -
   |
Lowest
```

So:

```text
^ > * / > + -
```

Parentheses have priority over normal operators.

---

# 11. Infix, Postfix and Prefix

### Infix

Operator is between operands.

```text
A + B
```

### Postfix

Operator comes after operands.

```text
A B +
```

### Prefix

Operator comes before operands.

```text
+ A B
```

---

# 12. Assignment Question 3
## Infix to Postfix

Expression:

```text
A + (B * C - (D / E ^ F) * G) * H
```

Expected postfix:

```text
A B C * D E F ^ / G * - H * +
```

---

## Basic Rules

### Operand

Immediately add it to output.

```text
A → output
B → output
```

### `(`

Push it into stack.

### `)`

Pop until `(` is found.

### Operator

Pop operators having higher precedence.

For operators with the same precedence, pop according to associativity.

`^` is **right-associative**, while `+`, `-`, `*`, `/` are left-associative.

---

## C++ Program

```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

#define SIZE 100

class Stack {
    char arr[SIZE];
    int top;

public:
    Stack() {
        top = -1;
    }

    void push(char ch) {
        if (top < SIZE - 1)
            arr[++top] = ch;
    }

    char pop() {
        if (top == -1)
            return '\0';

        return arr[top--];
    }

    char peek() {
        if (top == -1)
            return '\0';

        return arr[top];
    }

    bool isEmpty() {
        return top == -1;
    }
};

int precedence(char op) {
    if (op == '^')
        return 3;

    if (op == '*' || op == '/')
        return 2;

    if (op == '+' || op == '-')
        return 1;

    return 0;
}

bool isOperator(char ch) {
    return ch == '+' || ch == '-' ||
           ch == '*' || ch == '/' || ch == '^';
}

string infixToPostfix(string exp) {
    Stack s;
    string result;

    for (char ch : exp) {

        if (isalnum(ch)) {
            result += ch;
            result += ' ';
        }

        else if (ch == '(') {
            s.push(ch);
        }

        else if (ch == ')') {

            while (!s.isEmpty() && s.peek() != '(') {
                result += s.pop();
                result += ' ';
            }

            if (!s.isEmpty())
                s.pop();
        }

        else if (isOperator(ch)) {

            while (!s.isEmpty() &&
                   s.peek() != '(' &&
                   (precedence(s.peek()) > precedence(ch) ||
                   (precedence(s.peek()) == precedence(ch) && ch != '^'))) {

                result += s.pop();
                result += ' ';
            }

            s.push(ch);
        }
    }

    while (!s.isEmpty()) {
        result += s.pop();
        result += ' ';
    }

    return result;
}

int main() {
    string exp = "A+(B*C-(D/E^F)*G)*H";

    cout << infixToPostfix(exp);

    return 0;
}
```

### Output

```text
A B C * D E F ^ / G * - H * +
```

---

# 13. Dry Run of the Important Part

For:

```text
A + B * C
```

### Read `A`

```text
Output: A
Stack:  empty
```

### Read `+`

```text
Output: A
Stack: +
```

### Read `B`

```text
Output: A B
Stack: +
```

### Read `*`

`*` has higher precedence than `+`.

```text
Output: A B
Stack: + *
```

### Read `C`

```text
Output: A B C
Stack: + *
```

End of expression → pop stack:

```text
* then +
```

Final:

```text
A B C * +
```

---

# 14. Assignment Question 4
## Infix to Prefix

Expression:

```text
(A - B / C) * (A / K - L)
```

Expected prefix:

```text
* - A / B C - / A K L
```

The assignment specifically asks for the:

```text
Reverse Infix → Postfix → Reverse Result
```

method, with parentheses swapped during reversal.

---

# 15. Prefix Conversion Method

### Step 1 — Reverse the expression

Original:

```text
(A-B/C)*(A/K-L)
```

Reverse:

```text
)L-K/A(*)C/B-A(
```

### Step 2 — Swap parentheses

```text
(L-K/A)*(C/B-A)
```

### Step 3 — Convert this to postfix

```text
L K A / - C B / A - *
```

### Step 4 — Reverse the postfix

```text
* - A / B C - / A K L
```

That is the prefix expression.

---

## C++ Program

```cpp
#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>
using namespace std;

#define SIZE 100

class Stack {
    char arr[SIZE];
    int top;

public:
    Stack() {
        top = -1;
    }

    void push(char ch) {
        if (top < SIZE - 1)
            arr[++top] = ch;
    }

    char pop() {
        if (top == -1)
            return '\0';

        return arr[top--];
    }

    char peek() {
        if (top == -1)
            return '\0';

        return arr[top];
    }

    bool isEmpty() {
        return top == -1;
    }
};

int precedence(char op) {
    if (op == '^')
        return 3;

    if (op == '*' || op == '/')
        return 2;

    if (op == '+' || op == '-')
        return 1;

    return 0;
}

bool isOperator(char ch) {
    return ch == '+' || ch == '-' ||
           ch == '*' || ch == '/' || ch == '^';
}

string toPostfix(string exp) {
    Stack s;
    string result;

    for (char ch : exp) {

        if (isalnum(ch)) {
            result += ch;
            result += ' ';
        }

        else if (ch == '(') {
            s.push(ch);
        }

        else if (ch == ')') {

            while (!s.isEmpty() && s.peek() != '(') {
                result += s.pop();
                result += ' ';
            }

            if (!s.isEmpty())
                s.pop();
        }

        else if (isOperator(ch)) {

            while (!s.isEmpty() &&
                   s.peek() != '(' &&
                   precedence(s.peek()) >= precedence(ch)) {

                result += s.pop();
                result += ' ';
            }

            s.push(ch);
        }
    }

    while (!s.isEmpty()) {
        result += s.pop();
        result += ' ';
    }

    return result;
}

int main() {
    string exp = "(A-B/C)*(A/K-L)";

    reverse(exp.begin(), exp.end());

    for (char &ch : exp) {
        if (ch == '(')
            ch = ')';
        else if (ch == ')')
            ch = '(';
    }

    string postfix = toPostfix(exp);

    reverse(postfix.begin(), postfix.end());

    cout << postfix;

    return 0;
}
```

### Output

```text
* - A / B C - / A K L
```

---

# 16. Important Viva Questions

### Q1. What is a stack?

A stack is a linear data structure that follows **LIFO — Last In, First Out**.

### Q2. What is `top`?

`top` stores the index of the element currently at the top of the stack.

### Q3. Why is `top` initially `-1`?

Because the stack is initially empty and no array index is occupied.

### Q4. What is push?

`push()` inserts an element at the top.

### Q5. What is pop?

`pop()` removes the element from the top.

### Q6. What is peek?

`peek()` returns the top element without removing it.

### Q7. What is overflow?

Overflow occurs when we try to insert into a full fixed-size stack.

### Q8. What is underflow?

Underflow occurs when we try to remove an element from an empty stack.

### Q9. What does LIFO mean?

**Last In, First Out.**

### Q10. What is the time complexity of push and pop?

For an array stack:

```text
O(1)
```

### Q11. What is infix notation?

Operator is between operands:

```text
A + B
```

### Q12. What is postfix notation?

Operator comes after operands:

```text
A B +
```

### Q13. What is prefix notation?

Operator comes before operands:

```text
+ A B
```

### Q14. Why is a stack used in infix conversion?

The stack temporarily stores operators and parentheses while maintaining their required order.

---

# 17. One-Minute Revision

Memorize this:

```text
STACK
↓
LIFO
↓
top = -1 initially

PUSH:
check full
top++
arr[top] = value

POP:
check empty
value = arr[top]
top--
return value

PEEK:
arr[top]

OVERFLOW:
push into full stack

UNDERFLOW:
pop from empty stack
```

For expression conversion:

```text
Infix:
A + B

Postfix:
A B +

Prefix:
+ A B
```

Precedence:

```text
^
↓
* /
↓
+ -
```

Assignment programs:

```text
Q1 → Push characters → Pop characters → reverse string

Q2 → Push opening brackets
     Pop when closing bracket appears
     Check matching pairs

Q3 → Infix → Postfix using operator stack

Q4 → Reverse infix
     Swap ( and )
     Convert to postfix
     Reverse result
     → Prefix
```

---

# 18. Assignment Expected Answers

### Question 1

```text
Input:
algorithm

Output:
mtirogla
```

### Question 2

```text
{[()]}  → True
{[(])}  → False
```

### Question 3

```text
Input:
A + (B * C - (D / E ^ F) * G) * H

Postfix:
A B C * D E F ^ / G * - H * +
```

### Question 4

```text
Input:
(A - B / C) * (A / K - L)

Prefix:
* - A / B C - / A K L
```

---

## Final Tip

If you are writing this in a lab exam, **understand the `top` variable first**. Almost every stack program is just:

```text
push → move top up
pop  → move top down
peek → read top
```

Once this is clear, the four assignment programs become applications of the same stack.
