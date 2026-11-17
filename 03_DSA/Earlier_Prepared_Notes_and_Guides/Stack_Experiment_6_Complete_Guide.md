# Data Structures Lab — Experiment 6
## Stack Using Array: Complete Study Guide

This guide is based on the assignment sheet. Experiment 6 asks you to implement a stack using an array of `n` values and perform `push()` and `pop()` operations. The assignment then asks four programs: string reversal, bracket validation, infix-to-postfix conversion, and infix-to-prefix conversion. fileciteturn0file0L2-L7

---

# 1. What is a Stack?

A **stack** is a linear data structure that follows:

> **LIFO = Last In, First Out**

Think of a stack of plates:

```text
        TOP
       ┌─────┐
       │  C  │  ← last inserted, first removed
       ├─────┤
       │  B  │
       ├─────┤
       │  A  │
       └─────┘
```

If you insert:

```text
A → B → C
```

then removal happens:

```text
C → B → A
```

All insertion and deletion happen at one end called the **top**. The assignment also notes that basic stack operations such as push, pop, peek, and checking whether the stack is empty take `O(1)` time. fileciteturn0file0L5-L16

---

# 2. The Operations You Must Know

## PUSH

**Push = add an element to the top.**

Example:

```text
Before:
[A, B]

push(C)

After:
[A, B, C]
```

Python:

```python
stack.append("C")
```

## POP

**Pop = remove the top element.**

```text
Before:
[A, B, C]

pop()

After:
[A, B]
```

Python:

```python
x = stack.pop()
```

## PEEK / TOP

Peek means looking at the top element without removing it.

```python
print(stack[-1])
```

## isEmpty

Checks whether there are no elements.

```python
if len(stack) == 0:
    print("Stack is empty")
```

---

# 3. Overflow and Underflow

These two words are extremely important for the lab.

## Overflow

Overflow occurs when you try to push into a **full fixed-size stack**.

If:

```text
MAX_SIZE = 3
```

and:

```text
[A, B, C]
```

then:

```text
push(D)
```

causes:

```text
STACK OVERFLOW
```

The assignment demonstrates exactly this condition. fileciteturn0file0L33-L54

## Underflow

Underflow occurs when you try to pop from an **empty stack**.

```text
[]
```

then:

```text
pop()
```

causes:

```text
STACK UNDERFLOW
```

The assignment demonstrates this after all three elements have been popped. fileciteturn0file0L55-L74

### Remember

```text
FULL  + PUSH → OVERFLOW
EMPTY + POP  → UNDERFLOW
```

---

# 4. Array-Based Stack

For your assignment, the easiest Python implementation is:

```python
stack = []
MAX_SIZE = 5
```

## Push function

```python
def push(item):
    if len(stack) == MAX_SIZE:
        print("Stack Overflow")
    else:
        stack.append(item)
```

## Pop function

```python
def pop():
    if len(stack) == 0:
        print("Stack Underflow")
    else:
        return stack.pop()
```

The assignment's examples use the same basic approach: check the size before pushing and check for an empty stack before popping. fileciteturn0file0L39-L64

---

# 5. Question 1 — Reverse a String Using Stack

## Question

Reverse a given string using stack `push()` and `pop()` operations.

Example:

```text
Input:  algorithm
Output: mtirogla
```

The assignment explicitly requires that you do not use a built-in reverse function. fileciteturn0file0L76-L78

## The idea

Suppose:

```text
algorithm
```

Push every character:

```text
a l g o r i t h m
```

The stack becomes:

```text
TOP
 m
 h
 t
 i
 r
 o
 g
 l
 a
```

Now pop everything.

Because a stack is LIFO, you get:

```text
m t i r o g l a
```

## Code

```python
def reverse_string(text):
    stack = []

    for ch in text:
        stack.append(ch)

    result = ""

    while len(stack) > 0:
        result += stack.pop()

    return result


text = input("Enter a string: ")
print("Reversed:", reverse_string(text))
```

### Important logic

```python
for ch in text:
    stack.append(ch)
```

means **push every character**.

Then:

```python
while len(stack) > 0:
    result += stack.pop()
```

means **pop until the stack is empty**.

### Dry run

For:

```text
ABC
```

Push:

```text
A
AB
ABC
```

Pop:

```text
C
B
A
```

Answer:

```text
CBA
```

---

# 6. Question 2 — Balanced Brackets

## Question

Given a string containing:

```text
()
{}
[]
```

determine whether brackets are correctly opened and closed.

Examples from the assignment:

```text
{[()]} → True
{[(])} → False
```

fileciteturn0file0L79-L80

---

# 7. The Main Idea Behind Bracket Matching

Whenever you see an **opening bracket**, push it.

```text
(
{
[
```

Whenever you see a **closing bracket**, check the top of the stack.

Matching pairs:

```text
( )
[ ]
{ }
```

The closing bracket must match the most recently opened bracket.

---

# 8. Algorithm for Balanced Brackets

Use:

```python
pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
}
```

Then scan the string character by character.

### If opening bracket:

```text
push it
```

### If closing bracket:

1. Stack must not be empty.
2. Top of stack must be the corresponding opening bracket.
3. Otherwise → False.
4. If it matches → pop it.

At the end:

```text
stack empty → True
stack not empty → False
```

---

# 9. Code for Balanced Brackets

```python
def is_balanced(expression):
    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in expression:

        if ch in "([{":
            stack.append(ch)

        elif ch in ")]}":

            if len(stack) == 0:
                return False

            if stack[-1] != pairs[ch]:
                return False

            stack.pop()

    return len(stack) == 0


expression = input("Enter expression: ")

if is_balanced(expression):
    print("True")
else:
    print("False")
```

---

# 10. Dry Run — `{[()]}`

Start:

```text
stack = []
```

Read `{`:

```text
[{]
```

Read `[`:

```text
[{, []
```

Read `(`:

```text
[{, [, (]
```

Read `)`:

```text
top = (
)
matches (
→ pop
```

Read `]`:

```text
top = [
]
matches [
→ pop
```

Read `}`:

```text
top = {
}
matches {
→ pop
```

End:

```text
stack = []
```

Therefore:

```text
True
```

---

# 11. Dry Run — `{[(])}`

Opening:

```text
{
[
(
```

Stack:

```text
{ [ (
```

Next character:

```text
]
```

Top is:

```text
(
```

But `]` needs:

```text
[
```

Mismatch!

Therefore:

```text
False
```

### Key trick

You do **not** compare brackets randomly.

Always compare the closing bracket with:

```python
stack[-1]
```

---

# 12. Question 3 — Infix to Postfix

The assignment asks you to convert:

```text
A + (B * C - (D / E ^ F) * G) * H
```

to postfix using an array-based stack and operator precedence. The expected result is:

```text
A B C * D E F ^ / G * - H * +
```

fileciteturn0file0L81-L83

---

# 13. What is Infix?

Normal mathematical notation is **infix**:

```text
A + B
```

The operator is between operands.

Examples:

```text
A + B
A * B
A + B * C
```

---

# 14. What is Postfix?

Postfix puts the operator **after** its operands.

```text
A B +
```

For:

```text
A + B
```

postfix is:

```text
A B +
```

For:

```text
A + B * C
```

postfix is:

```text
A B C * +
```

Why?

Because multiplication has higher precedence than addition.

---

# 15. Operator Precedence

For this assignment:

```text
Highest
   ^
   *
   /
   +
   -
Lowest
```

Usually write it as:

```text
^ > * = / > + = -
```

The assignment describes the ordering as `^ > *, / > +, -`. fileciteturn0file0L81-L82

### Easy memory trick

```text
Power
Multiply / Divide
Add / Subtract
```

---

# 16. Why Do We Need a Stack?

Operands can directly go to the output.

Operators need to wait until it is their correct time to appear.

So:

```text
OPERAND → output
OPERATOR → stack
```

Parentheses also use the stack.

This is the central idea of infix-to-postfix conversion.

---

# 17. Rules for Infix → Postfix

Scan the expression from left to right.

## Rule 1 — Operand

If it is a letter/number:

```text
put it directly into output
```

Example:

```text
A
```

Output:

```text
A
```

---

## Rule 2 — `(`

Push it onto the stack.

```text
(
```

---

## Rule 3 — `)`

Pop operators until `(` is found.

Then remove `(`.

---

## Rule 4 — Operator

Suppose the current operator is `*`.

Look at the top of the stack.

If the stack operator has **higher or equal precedence**, pop it.

Then push the current operator.

---

## Rule 5 — End of expression

Pop all remaining operators from the stack.

---

# 18. Simple Example

Convert:

```text
A + B * C
```

### Read A

Output:

```text
A
```

### Read +

Stack:

```text
+
```

### Read B

Output:

```text
A B
```

### Read *

`*` has higher precedence than `+`.

Push:

```text
+
*
```

### Read C

Output:

```text
A B C
```

End.

Pop:

```text
*
+
```

Final:

```text
A B C * +
```

---

# 19. Precedence Function

A clean implementation uses:

```python
def precedence(op):
    if op == '^':
        return 3
    elif op == '*' or op == '/':
        return 2
    elif op == '+' or op == '-':
        return 1
    return 0
```

---

# 20. Infix-to-Postfix Code

```python
def precedence(op):
    if op == '^':
        return 3
    elif op == '*' or op == '/':
        return 2
    elif op == '+' or op == '-':
        return 1
    return 0


def infix_to_postfix(expression):
    stack = []
    output = []

    for ch in expression:

        if ch.isalnum():
            output.append(ch)

        elif ch == '(':
            stack.append(ch)

        elif ch == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())

            stack.pop()

        else:
            while (stack and stack[-1] != '(' and
                   precedence(stack[-1]) >= precedence(ch)):
                output.append(stack.pop())

            stack.append(ch)

    while stack:
        output.append(stack.pop())

    return " ".join(output)


expression = "A+(B*C-(D/E^F)*G)*H"

print(infix_to_postfix(expression))
```

Expected:

```text
A B C * D E F ^ / G * - H * +
```

---

# 21. Understanding the Big Expression

Expression:

```text
A + (B * C - (D / E ^ F) * G) * H
```

Break it into pieces:

```text
B * C
```

becomes:

```text
B C *
```

Then:

```text
E ^ F
```

becomes:

```text
E F ^
```

Then:

```text
D / (E ^ F)
```

becomes:

```text
D E F ^ /
```

Then:

```text
(D / E ^ F) * G
```

becomes:

```text
D E F ^ / G *
```

Then:

```text
B * C - (D / E ^ F) * G
```

becomes:

```text
B C * D E F ^ / G * -
```

Then multiply the whole bracket by `H`:

```text
B C * D E F ^ / G * - H *
```

Finally add `A`:

```text
A B C * D E F ^ / G * - H * +
```

---

# 22. Question 4 — Infix to Prefix

The assignment asks you to convert:

```text
(A - B / C) * (A / K - L)
```

to prefix.

Expected:

```text
* - A / B C - / A K L
```

fileciteturn0file0L84-L86

---

# 23. What is Prefix?

Prefix puts the operator **before** its operands.

Infix:

```text
A + B
```

Prefix:

```text
+ A B
```

Postfix:

```text
A B +
```

Remember:

```text
INFIX   → A + B
PREFIX  → + A B
POSTFIX → A B +
```

---

# 24. Prefix Conversion Trick

The assignment specifically asks for:

> Reverse → swap parentheses → convert to postfix → reverse result

This is the method you should learn for Question 4. fileciteturn0file0L84-L86

---

# 25. Prefix Conversion Steps

Given:

```text
(A - B / C) * (A / K - L)
```

## Step 1 — Reverse the expression

Conceptually reverse:

```text
) L - K / A ( * ) C / B - A (
```

---

## Step 2 — Swap parentheses

Every:

```text
(
```

becomes:

```text
)
```

and every:

```text
)
```

becomes:

```text
(
```

So:

```text
( L - K / A ) * ( C / B - A )
```

---

## Step 3 — Convert this to postfix

Using the same infix-to-postfix algorithm.

---

## Step 4 — Reverse the postfix result

That gives prefix.

---

# 26. Prefix Code

For a lab implementation, you can write:

```python
def precedence(op):
    if op == '^':
        return 3
    elif op == '*' or op == '/':
        return 2
    elif op == '+' or op == '-':
        return 1
    return 0


def infix_to_postfix(expression):
    stack = []
    output = []

    for ch in expression:

        if ch.isalnum():
            output.append(ch)

        elif ch == '(':
            stack.append(ch)

        elif ch == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())

            if stack:
                stack.pop()

        else:
            while (stack and stack[-1] != '(' and
                   precedence(stack[-1]) >= precedence(ch)):
                output.append(stack.pop())

            stack.append(ch)

    while stack:
        output.append(stack.pop())

    return output


def infix_to_prefix(expression):

    reversed_expression = expression[::-1]

    swapped = ""

    for ch in reversed_expression:
        if ch == '(':
            swapped += ')'
        elif ch == ')':
            swapped += '('
        else:
            swapped += ch

    postfix = infix_to_postfix(swapped)

    prefix = postfix[::-1]

    return " ".join(prefix)


expression = "(A-B/C)*(A/K-L)"

print(infix_to_prefix(expression))
```

Expected:

```text
* - A / B C - / A K L
```

---

# 27. One Important Detail: `^`

Exponentiation is usually **right-associative**.

Example:

```text
A ^ B ^ C
```

means:

```text
A ^ (B ^ C)
```

not:

```text
(A ^ B) ^ C
```

For the exact expressions in your assignment, the standard precedence implementation above is enough to understand the required conversion, but if your teacher asks about associativity, remember:

```text
^ → right associative
+, -, *, / → generally left associative
```

---

# 28. Built-in Functions You Should Avoid for the Assignment

The point of this experiment is to demonstrate stacks.

For Question 1, don't do:

```python
text[::-1]
```

or:

```python
text.reverse()
```

Instead:

```python
stack.append(ch)
```

and:

```python
stack.pop()
```

The assignment specifically asks for stack push/pop rather than a built-in reverse function. fileciteturn0file0L76-L78

---

# 29. Array Stack Without Python's `append()` / `pop()`

If your teacher means a literal fixed-size array implementation, you can implement the stack using an array and a `top` variable.

```python
MAX = 5
stack = [None] * MAX
top = -1
```

Why:

```text
top = -1
```

means:

```text
stack is empty
```

When you push:

```python
top += 1
stack[top] = item
```

When you pop:

```python
item = stack[top]
top -= 1
```

This is closer to the traditional **array stack** taught in data structures.

---

# 30. Traditional Array Stack — Complete Code

```python
MAX = 5
stack = [None] * MAX
top = -1


def push(item):
    global top

    if top == MAX - 1:
        print("Stack Overflow")
        return

    top += 1
    stack[top] = item


def pop():
    global top

    if top == -1:
        print("Stack Underflow")
        return None

    item = stack[top]
    top -= 1
    return item


def peek():
    if top == -1:
        print("Stack is empty")
        return None

    return stack[top]
```

---

# 31. Understand `top`

This is one of the most important concepts.

For:

```text
stack = [10, 20, 30, _, _]
```

we have:

```text
top = 2
```

because index `2` contains `30`.

Array indexes:

```text
0    1    2    3    4
10   20   30   _    _
          ↑
         top
```

After pop:

```text
top = 1
```

After another pop:

```text
top = 0
```

After another:

```text
top = -1
```

Stack is now empty.

---

# 32. Overflow Condition

With:

```python
MAX = 5
```

valid indexes are:

```text
0 1 2 3 4
```

Therefore the stack is full when:

```python
top == MAX - 1
```

which means:

```python
top == 4
```

---

# 33. Underflow Condition

The stack is empty when:

```python
top == -1
```

Therefore:

```python
if top == -1:
    print("Stack Underflow")
```

---

# 34. What You Need to Memorize for the Viva

## Stack

```text
LIFO
```

## Push

```text
Insert at TOP
```

## Pop

```text
Delete from TOP
```

## Peek

```text
View TOP without deleting
```

## Overflow

```text
Push when FULL
```

## Underflow

```text
Pop when EMPTY
```

## Time complexity

```text
Push → O(1)
Pop  → O(1)
Peek → O(1)
```

The assignment itself identifies these basic operations as `O(1)`. fileciteturn0file0L8-L16

---

# 35. Infix / Prefix / Postfix Cheat Sheet

| Notation | Operator Position | Example |
|---|---|---|
| Infix | Between operands | `A + B` |
| Prefix | Before operands | `+ A B` |
| Postfix | After operands | `A B +` |

---

# 36. Operator Precedence Cheat Sheet

```text
^       → 3
* /     → 2
+ -     → 1
(       → special
```

Higher number = higher priority.

---

# 37. The Four Assignment Questions — What You Actually Need to Do

## Q1 — Reverse String

Remember:

```text
FOR each character:
    PUSH

WHILE stack not empty:
    POP
```

Pattern:

```python
for ch in text:
    stack.append(ch)

while stack:
    result += stack.pop()
```

---

## Q2 — Balanced Brackets

Remember:

```text
OPENING  → PUSH
CLOSING  → CHECK TOP + POP
END      → STACK MUST BE EMPTY
```

---

## Q3 — Infix → Postfix

Remember:

```text
Operand → output
(       → push
)       → pop until (
Operator → compare precedence
End     → pop everything
```

Expected:

```text
A B C * D E F ^ / G * - H * +
```

---

## Q4 — Infix → Prefix

Remember:

```text
1. Reverse
2. Swap ( and )
3. Convert to postfix
4. Reverse result
```

Expected:

```text
* - A / B C - / A K L
```

---

# 38. Best Way to Practice

Don't memorize the full programs.

Memorize these **four patterns**:

### Pattern 1

```python
stack.append(x)
```

means:

```text
PUSH
```

### Pattern 2

```python
x = stack.pop()
```

means:

```text
POP
```

### Pattern 3

```python
stack[-1]
```

means:

```text
TOP
```

### Pattern 4

```python
while stack:
```

means:

```text
while stack is not empty
```

If you understand these four things, most of this assignment becomes much easier.

---

# 39. Final Exam/Viva Revision

### What is a stack?

A linear data structure following LIFO.

### What does LIFO mean?

Last In, First Out.

### Where are insertion and deletion performed?

At the top.

### What is push?

Adding an element to the top.

### What is pop?

Removing the top element.

### What is overflow?

Trying to push into a full fixed-size stack.

### What is underflow?

Trying to pop from an empty stack.

### What is postfix?

Operator comes after operands.

```text
A B +
```

### What is prefix?

Operator comes before operands.

```text
+ A B
```

### Why is a stack useful for expression conversion?

Because operators must temporarily wait until their precedence and parentheses determine their correct position.

### Which has higher precedence?

```text
^
```

then:

```text
* /
```

then:

```text
+ -
```

### What is the prefix conversion method in this assignment?

```text
Reverse → Swap parentheses → Postfix → Reverse
```

---

# 40. One-Page Memory Map

```text
                    STACK
                      |
                    LIFO
                      |
          ┌───────────┴───────────┐
          ↓                       ↓
        PUSH                     POP
          |                       |
       INSERT                  DELETE
          |                       |
          └─────── TOP ───────────┘

FULL + PUSH  = OVERFLOW
EMPTY + POP  = UNDERFLOW

             EXPRESSION CONVERSION
                     |
          ┌──────────┴──────────┐
          ↓                     ↓
       POSTFIX                PREFIX
          |                     |
   Operator AFTER         Operator BEFORE
      operands               operands
          |                     |
 A B C * +               + * ? ...

PREFIX METHOD:
Reverse
   ↓
Swap brackets
   ↓
Postfix
   ↓
Reverse

PRECEDENCE:
^
↓
* /
↓
+ -
```

---

# 41. Most Important Thing

For this assignment, don't think of the stack as a complicated data structure.

Think:

```text
STACK = a box where you can only access the TOP
```

If you put in:

```text
A
B
C
```

you can only take out:

```text
C
B
A
```

That single idea explains:

- reversing a string
- matching brackets
- converting infix to postfix
- converting infix to prefix

because all four problems need **LIFO behavior**.
