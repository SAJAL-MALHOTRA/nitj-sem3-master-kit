# Data Structures Notes: Linked List → Stack → Queue (C++)

> Based on Unit 2 & Unit 3 (Data Structures, ITDC0203). Covers Linked Lists, Stacks, and Queues with theory + C++ code for sem exams.

---

## 1. Linked List

### 1.1 Definition
A **linked list** is a linear data structure where elements ("nodes") are **not stored contiguously** in memory. Each node contains:
- **Data** field
- **Pointer (link)** to the next node

Unlike arrays, linked lists are **dynamic** — they grow/shrink at runtime and don't need memory to be pre-allocated or contiguous.

### 1.2 Array vs Linked List

| Array | Linked List |
|---|---|
| Fixed size (static) | Dynamic size |
| Contiguous memory | Non-contiguous memory |
| Insertion/Deletion is costly (shifting) | Insertion/Deletion is easy (pointer update) |
| Random access (O(1)) | Sequential access only (O(n)) |
| Extra memory not required | Extra memory needed for pointers |

### 1.3 Types of Linked Lists
1. **Singly Linked List (SLL)** – each node points only to the next node.
2. **Doubly Linked List (DLL)** – each node has pointers to both next and previous nodes.
3. **Circular Linked List (CLL)** – last node points back to the first node.
4. **Circular Doubly Linked List** – combines circular + doubly properties.

### 1.4 Singly Linked List — Node Structure (C++)

```cpp
struct Node {
    int data;
    Node* next;
};

Node* head = nullptr;   // empty list initially
```

### 1.5 Operations on Singly Linked List

#### (a) Insertion at the Beginning
```cpp
void insertAtBeginning(Node*& head, int value) {
    Node* newNode = new Node();
    newNode->data = value;
    newNode->next = head;
    head = newNode;
}
```

#### (b) Insertion at the End
```cpp
void insertAtEnd(Node*& head, int value) {
    Node* newNode = new Node();
    newNode->data = value;
    newNode->next = nullptr;

    if (head == nullptr) { head = newNode; return; }

    Node* temp = head;
    while (temp->next != nullptr)
        temp = temp->next;
    temp->next = newNode;
}
```

#### (c) Insertion at a Given Position
```cpp
void insertAtPosition(Node*& head, int value, int pos) {
    if (pos == 0) { insertAtBeginning(head, value); return; }

    Node* newNode = new Node();
    newNode->data = value;

    Node* temp = head;
    for (int i = 0; i < pos - 1 && temp != nullptr; i++)
        temp = temp->next;

    if (temp == nullptr) return; // invalid position
    newNode->next = temp->next;
    temp->next = newNode;
}
```

#### (d) Deletion (by value)
```cpp
void deleteNode(Node*& head, int key) {
    Node *temp = head, *prev = nullptr;

    if (temp != nullptr && temp->data == key) {
        head = temp->next;
        delete temp;
        return;
    }

    while (temp != nullptr && temp->data != key) {
        prev = temp;
        temp = temp->next;
    }

    if (temp == nullptr) return; // not found
    prev->next = temp->next;
    delete temp;
}
```

#### (e) Traversal
```cpp
void display(Node* head) {
    Node* temp = head;
    while (temp != nullptr) {
        cout << temp->data << " -> ";
        temp = temp->next;
    }
    cout << "NULL" << endl;
}
```

#### (f) Search
```cpp
bool search(Node* head, int key) {
    Node* temp = head;
    while (temp != nullptr) {
        if (temp->data == key) return true;
        temp = temp->next;
    }
    return false;
}
```

**Complexity summary (SLL):** Insert/Delete at head → O(1); at end/position/search → O(n).

### 1.6 Doubly Linked List (DLL)

Each node has **three fields**: `prev`, `data`, `next`.

```cpp
struct DNode {
    int data;
    DNode* prev;
    DNode* next;
};
```

**Insert at beginning:**
```cpp
void insertAtBeginning(DNode*& head, int value) {
    DNode* newNode = new DNode();
    newNode->data = value;
    newNode->prev = nullptr;
    newNode->next = head;
    if (head != nullptr) head->prev = newNode;
    head = newNode;
}
```

**Insert at end:**
```cpp
void insertAtEnd(DNode*& head, int value) {
    DNode* newNode = new DNode();
    newNode->data = value;
    newNode->next = nullptr;

    if (head == nullptr) { newNode->prev = nullptr; head = newNode; return; }

    DNode* temp = head;
    while (temp->next != nullptr) temp = temp->next;
    temp->next = newNode;
    newNode->prev = temp;
}
```

**Deletion (given node):**
```cpp
void deleteDNode(DNode*& head, DNode* delNode) {
    if (head == delNode) head = delNode->next;
    if (delNode->next != nullptr) delNode->next->prev = delNode->prev;
    if (delNode->prev != nullptr) delNode->prev->next = delNode->next;
    delete delNode;
}
```

**Advantage over SLL:** Can traverse both directions; deletion doesn't need a "previous" pointer search.
**Disadvantage:** Extra memory for the `prev` pointer.

### 1.7 Circular Linked List (CLL)

The **last node's `next` points back to the head** instead of `NULL`, forming a ring.

```cpp
struct Node {
    int data;
    Node* next;
};

void insertAtEnd(Node*& head, int value) {
    Node* newNode = new Node();
    newNode->data = value;

    if (head == nullptr) {
        newNode->next = newNode;   // points to itself
        head = newNode;
        return;
    }
    Node* temp = head;
    while (temp->next != head) temp = temp->next;
    temp->next = newNode;
    newNode->next = head;
}

void display(Node* head) {
    if (head == nullptr) return;
    Node* temp = head;
    do {
        cout << temp->data << " -> ";
        temp = temp->next;
    } while (temp != head);
    cout << "(back to head)" << endl;
}
```

**Advantages:** Useful for round-robin scheduling, traversal from any node, no NULL check needed for "end".
**Disadvantage:** Risk of infinite loop if not handled carefully; reverse traversal is hard (singly circular).

### 1.7.1 Doubly Circular Linked List (DCLL)

Combines **doubly linked** (has `prev` and `next`) + **circular** (last node's `next` points to head, head's `prev` points to last node).

```cpp
struct DCNode {
    int data;
    DCNode* prev;
    DCNode* next;
};
```

**Insertion at the beginning:**
```cpp
void insertAtBeginning(DCNode*& head, int value) {
    DCNode* newNode = new DCNode();
    newNode->data = value;

    if (head == nullptr) {
        newNode->next = newNode;
        newNode->prev = newNode;
        head = newNode;
        return;
    }

    DCNode* last = head->prev;      // last node (since circular)
    newNode->next = head;
    newNode->prev = last;
    last->next = newNode;
    head->prev = newNode;
    head = newNode;                 // new node becomes head
}
```

**Insertion at the end:**
```cpp
void insertAtEnd(DCNode*& head, int value) {
    if (head == nullptr) { insertAtBeginning(head, value); return; }

    DCNode* newNode = new DCNode();
    newNode->data = value;

    DCNode* last = head->prev;
    last->next = newNode;
    newNode->prev = last;
    newNode->next = head;
    head->prev = newNode;
    // head stays the same
}
```

**Deletion from the beginning:**
```cpp
void deleteFromBeginning(DCNode*& head) {
    if (head == nullptr) return;

    if (head->next == head) {       // only one node
        delete head;
        head = nullptr;
        return;
    }

    DCNode* last = head->prev;
    DCNode* newHead = head->next;
    newHead->prev = last;
    last->next = newHead;
    delete head;
    head = newHead;
}
```

**Deletion from the end:**
```cpp
void deleteFromEnd(DCNode*& head) {
    if (head == nullptr) return;

    if (head->next == head) {       // only one node
        delete head;
        head = nullptr;
        return;
    }

    DCNode* last = head->prev;
    DCNode* secondLast = last->prev;
    secondLast->next = head;
    head->prev = secondLast;
    delete last;
}
```

**Why DCLL is preferred over plain circular list:** O(1) access to the last node via `head->prev` (no traversal needed to find it), and deletion/insertion at both ends is O(1) — this is exactly why it's used to implement **deques**.

**Worked Example:** Start with empty DCLL. `insertAtEnd(10)` → `insertAtEnd(20)` → `insertAtEnd(30)` gives:
```
head → 10 ⇄ 20 ⇄ 30 → (back to 10)
       ↑___________________|  (30.prev = 10 initially's... after insert, 10.prev = 30)
```
List (forward): 10, 20, 30 → back to 10. `head->prev` = 30 (last node) directly, no traversal needed.
Now `deleteFromBeginning()` → removes 10, new head = 20. List: 20, 30 → back to 20.
Now `deleteFromEnd()` → removes 30 (found via `head->prev`). List: just 20 → points to itself.

### 1.8 Applications of Linked Lists
- Implementing stacks & queues
- Dynamic memory allocation (free lists)
- Polynomial representation & arithmetic
- Sparse matrix representation
- Round-robin CPU scheduling (circular list)
- Undo functionality in editors (doubly linked list)

---

## 2. Stack

### 2.1 Definition
A **stack** is a linear data structure that follows **LIFO (Last In, First Out)** order. Insertion and deletion happen only from one end, called the **top**.

### 2.2 Basic Operations
| Operation | Description |
|---|---|
| `push(x)` | Insert element `x` at the top |
| `pop()` | Remove and return the top element |
| `peek()/top()` | View the top element without removing |
| `isEmpty()` | Check if stack is empty |
| `isFull()` | Check if stack is full (array implementation) |

### 2.3 Array-based Stack (C++)

```cpp
#define MAX 100

class Stack {
    int arr[MAX];
    int top;

public:
    Stack() { top = -1; }

    bool isEmpty() { return top == -1; }
    bool isFull()  { return top == MAX - 1; }

    void push(int value) {
        if (isFull()) { cout << "Stack Overflow\n"; return; }
        arr[++top] = value;
    }

    int pop() {
        if (isEmpty()) { cout << "Stack Underflow\n"; return -1; }
        return arr[top--];
    }

    int peek() {
        if (isEmpty()) { cout << "Stack is empty\n"; return -1; }
        return arr[top];
    }
};
```

### 2.4 Linked List-based Stack (C++)

```cpp
struct Node {
    int data;
    Node* next;
};

class Stack {
    Node* top;

public:
    Stack() { top = nullptr; }

    void push(int value) {
        Node* newNode = new Node();
        newNode->data = value;
        newNode->next = top;
        top = newNode;
    }

    int pop() {
        if (top == nullptr) { cout << "Stack Underflow\n"; return -1; }
        int val = top->data;
        Node* temp = top;
        top = top->next;
        delete temp;
        return val;
    }

    int peek() {
        if (top == nullptr) return -1;
        return top->data;
    }

    bool isEmpty() { return top == nullptr; }
};
```

### 2.5 Infix, Prefix, Postfix Expressions

| Type | Format | Example |
|---|---|---|
| Infix | operator between operands | `A + B` |
| Prefix (Polish) | operator before operands | `+AB` |
| Postfix (Reverse Polish) | operator after operands | `AB+` |

**Why postfix?** No need for parentheses or precedence rules → easy for machines to evaluate left-to-right using a stack.

### 2.6 Infix → Postfix Algorithm (using Stack)
1. Scan the infix expression left to right.
2. If operand → add to output.
3. If `(` → push onto stack.
4. If `)` → pop and output until `(` is found; discard the `(`.
5. If operator →
   - Pop and output operators from the stack **while** they have **higher or equal precedence** (respecting associativity), then push the current operator.
6. At the end, pop all remaining operators to output.

**C++ Implementation:**
```cpp
#include <bits/stdc++.h>
using namespace std;

int precedence(char c) {
    if (c == '^') return 3;
    if (c == '*' || c == '/') return 2;
    if (c == '+' || c == '-') return 1;
    return -1;
}

string infixToPostfix(string expr) {
    stack<char> st;
    string result;

    for (char c : expr) {
        if (isalnum(c)) {
            result += c;
        } else if (c == '(') {
            st.push(c);
        } else if (c == ')') {
            while (!st.empty() && st.top() != '(') {
                result += st.top();
                st.pop();
            }
            st.pop(); // remove '('
        } else { // operator
            while (!st.empty() && precedence(st.top()) >= precedence(c)) {
                result += st.top();
                st.pop();
            }
            st.push(c);
        }
    }
    while (!st.empty()) {
        result += st.top();
        st.pop();
    }
    return result;
}
```

### 2.7 Evaluating a Postfix Expression (using Stack)
1. Scan left to right.
2. If operand → push onto stack.
3. If operator → pop two operands, apply the operator, push the result back.
4. Final value left in the stack is the answer.

```cpp
int evaluatePostfix(string expr) {
    stack<int> st;
    for (char c : expr) {
        if (isdigit(c)) {
            st.push(c - '0');
        } else {
            int b = st.top(); st.pop();
            int a = st.top(); st.pop();
            switch (c) {
                case '+': st.push(a + b); break;
                case '-': st.push(a - b); break;
                case '*': st.push(a * b); break;
                case '/': st.push(a / b); break;
            }
        }
    }
    return st.top();
}
```

### 2.7.1 Postfix → Prefix Conversion (using Stack)

**Algorithm:**
1. Scan the postfix expression **left to right**.
2. If the symbol is an **operand**, push it onto the stack.
3. If the symbol is an **operator**:
   - Pop the top element → call it `op2` (this is the **second** operand, popped first).
   - Pop the next element → call it `op1` (this is the **first** operand).
   - Form the new string: `operator + op1 + op2` (operator goes in **front**).
   - Push this new string back onto the stack.
4. Repeat until the expression ends. The stack will contain exactly **one string** — the prefix expression.

> ⚠️ Order matters: prefix form is `operator op1 op2`, where `op1` was pushed **before** `op2`. Getting the pop order backwards is the most common exam mistake.

**C++ Implementation:**
```cpp
#include <bits/stdc++.h>
using namespace std;

bool isOperator(char c) {
    return c == '+' || c == '-' || c == '*' || c == '/' || c == '^';
}

string postfixToPrefix(string postfix) {
    stack<string> st;

    for (char c : postfix) {
        if (isOperator(c)) {
            string op2 = st.top(); st.pop();
            string op1 = st.top(); st.pop();
            string combined = c + op1 + op2;   // operator + op1 + op2
            st.push(combined);
        } else {
            st.push(string(1, c));             // operand
        }
    }
    return st.top();
}
```

**Worked Example:** Convert postfix `AB+CD-*` to prefix.

| Step | Symbol | Action | Stack (bottom → top) |
|---|---|---|---|
| 1 | A | push | A |
| 2 | B | push | A, B |
| 3 | + | pop B(op2), pop A(op1) → push `+AB` | +AB |
| 4 | C | push | +AB, C |
| 5 | D | push | +AB, C, D |
| 6 | - | pop D(op2), pop C(op1) → push `-CD` | +AB, -CD |
| 7 | * | pop -CD(op2), pop +AB(op1) → push `*+AB-CD` | *+AB-CD |

**Prefix result:** `*+AB-CD`

### 2.8 Applications of Stacks
- Expression evaluation & conversion (infix/prefix/postfix)
- Function call management (call stack, recursion)
- Undo/Redo operations
- Backtracking (maze solving, N-Queens)
- Balanced parentheses checking
- Browser back/forward navigation (DFS-style)

---

## 3. Queue

### 3.1 Definition
A **queue** is a linear data structure that follows **FIFO (First In, First Out)** order. Insertion happens at the **rear**, deletion at the **front**.

### 3.2 Basic Operations
| Operation | Description |
|---|---|
| `enqueue(x)` | Insert `x` at the rear |
| `dequeue()` | Remove element from the front |
| `front()` | View front element |
| `isEmpty()` / `isFull()` | Status checks |

### 3.3 Array-based Simple Queue (C++)

```cpp
#define MAX 100

class Queue {
    int arr[MAX];
    int front, rear;

public:
    Queue() { front = -1; rear = -1; }

    bool isEmpty() { return front == -1; }
    bool isFull()  { return rear == MAX - 1; }

    void enqueue(int value) {
        if (isFull()) { cout << "Queue Overflow\n"; return; }
        if (front == -1) front = 0;
        arr[++rear] = value;
    }

    int dequeue() {
        if (isEmpty()) { cout << "Queue Underflow\n"; return -1; }
        int val = arr[front];
        if (front == rear) front = rear = -1; // queue becomes empty
        else front++;
        return val;
    }
};
```

**Problem with simple queue:** Once `rear` hits `MAX-1`, the queue reports "full" even if front slots are free (unused space isn't reclaimed). This is solved by a **Circular Queue**.

### 3.4 Circular Queue

Front and rear wrap around using **modulo arithmetic**, so freed space at the beginning is reused.

```cpp
#define MAX 5

class CircularQueue {
    int arr[MAX];
    int front, rear;

public:
    CircularQueue() { front = -1; rear = -1; }

    bool isEmpty() { return front == -1; }
    bool isFull()  { return (rear + 1) % MAX == front; }

    void enqueue(int value) {
        if (isFull()) { cout << "Queue is Full\n"; return; }
        if (front == -1) front = 0;
        rear = (rear + 1) % MAX;
        arr[rear] = value;
    }

    int dequeue() {
        if (isEmpty()) { cout << "Queue is Empty\n"; return -1; }
        int val = arr[front];
        if (front == rear) front = rear = -1; // last element removed
        else front = (front + 1) % MAX;
        return val;
    }
};
```

**Application:** Traffic light control systems, round-robin CPU scheduling, circular buffers.

### 3.5 Deque (Double-Ended Queue)

Insertion and deletion allowed at **both ends** (front and rear).

- **Input-restricted deque:** insertion only at one end, deletion at both ends.
- **Output-restricted deque:** deletion only at one end, insertion at both ends.

```cpp
#include <deque>
using namespace std;

deque<int> dq;
dq.push_front(10);
dq.push_back(20);
dq.pop_front();
dq.pop_back();
```

### 3.6 Priority Queue

Each element has a **priority**; the element with the **highest priority is served first** (not strictly FIFO).

- **Ascending priority queue:** smallest element has highest priority (min-heap behavior).
- **Descending priority queue:** largest element has highest priority (max-heap behavior).

```cpp
#include <queue>
using namespace std;

// Max-priority queue (default)
priority_queue<int> maxPQ;
maxPQ.push(10);
maxPQ.push(30);
maxPQ.push(20);
cout << maxPQ.top(); // 30 (highest first)

// Min-priority queue
priority_queue<int, vector<int>, greater<int>> minPQ;
minPQ.push(10);
minPQ.push(30);
minPQ.push(20);
cout << minPQ.top(); // 10 (lowest first)
```

### 3.7 Linked List-based Queue (C++)

```cpp
struct Node {
    int data;
    Node* next;
};

class Queue {
    Node *front, *rear;

public:
    Queue() { front = rear = nullptr; }

    void enqueue(int value) {
        Node* newNode = new Node();
        newNode->data = value;
        newNode->next = nullptr;
        if (rear == nullptr) { front = rear = newNode; return; }
        rear->next = newNode;
        rear = newNode;
    }

    int dequeue() {
        if (front == nullptr) { cout << "Queue Underflow\n"; return -1; }
        int val = front->data;
        Node* temp = front;
        front = front->next;
        if (front == nullptr) rear = nullptr;
        delete temp;
        return val;
    }
};
```

### 3.8 Applications of Queues
- CPU/disk scheduling (round-robin)
- Handling requests on a shared resource (printer spooling)
- Breadth-First Search (BFS) in graphs/trees
- Buffering for data streams (IO buffers)
- Priority queues → Prim's/Dijkstra's algorithm, A* search, Huffman coding
- Call center / customer service systems

---

## 4. Quick Comparison Table

| Feature | Stack | Queue |
|---|---|---|
| Order | LIFO | FIFO |
| Insertion | `push` (top) | `enqueue` (rear) |
| Deletion | `pop` (top) | `dequeue` (front) |
| Use case | Recursion, undo, expression eval | Scheduling, BFS, buffering |
| Variants | — | Circular, Priority, Deque |

---

## 5. Solved Mid-Sem Questions (Sept 2025 Paper)

### Q3(a) — Trace a Singly Linked List Rearrange Function

```c
struct node { int value; struct node *next; };
void rearrange(struct node *list) {
    struct node *p, *q;
    int temp;
    if (!list || !list->next) return;
    p = list; q = list->next;
    while (q) {
        temp = p->value; p->value = q->value; q->value = temp;
        p = q->next;
        q = p ? p->next : 0;
    }
}
```
List given: `1 → 2 → 3 → 4 → 5 → 6 → 7`

**Trace (positions/nodes stay fixed; only `value` fields swap):**

| Iteration | p | q | Action | List state after |
|---|---|---|---|---|
| 1 | N1(1) | N2(2) | swap N1,N2 → p=N3, q=N4 | 2,1,3,4,5,6,7 |
| 2 | N3(3) | N4(4) | swap N3,N4 → p=N5, q=N6 | 2,1,4,3,5,6,7 |
| 3 | N5(5) | N6(6) | swap N5,N6 → p=N7, q=N7->next=NULL | 2,1,4,3,6,5,7 |
| — | N7 | 0 | loop ends (`q` is NULL) | — |

**Answer:** The function swaps values **pairwise** (1st↔2nd, 3rd↔4th, 5th↔6th) and leaves an unpaired last element untouched.
**Final list:** `2 → 1 → 4 → 3 → 6 → 5 → 7`

---

### Q3(b) — Convert Postfix to Prefix

**Given postfix:** `AB+C*DE-/FGH*+IJ^+KL/-+`

Applying the postfix→prefix stack algorithm (Section 2.7.1) token by token:

| Step | Symbol | Stack after action |
|---|---|---|
| A, B | push | A, B |
| + | pop B,A → `+AB` | +AB |
| C | push | +AB, C |
| * | pop C, +AB → `*+ABC` | *+ABC |
| D, E | push | *+ABC, D, E |
| - | pop E,D → `-DE` | *+ABC, -DE |
| / | pop -DE, *+ABC → `/*+ABC-DE` | /*+ABC-DE |
| F, G, H | push | ..., F, G, H |
| * | pop H,G → `*GH` | ..., F, *GH |
| + | pop *GH, F → `+F*GH` | /*+ABC-DE, +F*GH |
| I, J | push | ..., +F*GH, I, J |
| ^ | pop J,I → `^IJ` | ..., +F*GH, ^IJ |
| + | pop ^IJ, +F*GH → `++F*GH^IJ` | /*+ABC-DE, ++F*GH^IJ |
| K, L | push | ..., K, L |
| / | pop L,K → `/KL` | ..., ++F*GH^IJ, /KL |
| - | pop /KL, ++F*GH^IJ → `-++F*GH^IJ/KL` | /*+ABC-DE, -++F*GH^IJ/KL |
| + | pop both → final | `+/*+ABC-DE-++F*GH^IJ/KL` |

**Answer (Prefix):** `+/*+ABC-DE-++F*GH^IJ/KL`

---

### Q3(c) — Evaluate a Prefix Expression

**Given:** `* + 12 / * 4 3 2 / * * 1 4 6 8`

Prefix expressions are evaluated by scanning **right to left**, pushing operands, and on hitting an operator popping `op1` then `op2` and computing `op1 OP op2`:

| Step | Token (R→L) | Stack after |
|---|---|---|
| 8, 6, 4, 1 | push | 8, 6, 4, 1 |
| * | 1 * 4 = 4 | 8, 6, 4 |
| * | 4 * 6 = 24 | 8, 24 |
| / | 24 / 8 = 3 | 3 |
| 2, 3, 4 | push | 3, 2, 3, 4 |
| * | 4 * 3 = 12 | 3, 2, 12 |
| / | 12 / 2 = 6 | 3, 6 |
| 12 | push | 3, 6, 12 |
| + | 12 + 6 = 18 | 3, 18 |
| * | 18 * 3 = 54 | 54 |

**Answer: 54**

*(Cross-check by parse-tree method: `+12 (/(*43) 2)` = 12 + 6 = 18; `/(*(* 1 4) 6) 8` = 24/8 = 3; final `18 * 3 = 54`. ✅ Matches.)*

---

### Q2(c) — Insertion & Deletion in Doubly Circular Linked List
See **Section 1.7.1** above for full C++ code (`insertAtBeginning`, `insertAtEnd`, `deleteFromBeginning`, `deleteFromEnd`) plus a worked trace example (10 → 20 → 30 → back to 10, with head/tail links shown).

---

## 6. Likely Exam Questions
1. Write a C++ program to implement a singly/doubly linked list with insert, delete, and display.
2. Differentiate between array and linked list.
3. Convert a given infix expression to postfix/prefix using stack (show step-by-step stack trace).
4. Evaluate a given postfix expression using stack.
5. Write an algorithm/program for circular queue insertion and deletion; explain why simple queue is inefficient.
6. Explain applications of stack and queue with real-life examples.
7. Differentiate: Circular Queue vs Priority Queue vs Deque.
8. Write insertion/deletion algorithms for a circular linked list.
9. Trace stack/queue contents step-by-step for a given sequence of operations.
