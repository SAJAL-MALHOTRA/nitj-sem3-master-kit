#include <iostream>
#include <cstring>
using namespace std;

class Stack {
    char arr[100];
    int top;

public:
    Stack() {
        top = -1;
    }

    void push(char x) {
        if (top == 99)
            cout << "Stack Overflow\n";
        else
            arr[++top] = x;
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
    if (op == '+' || op == '-')
        return 1;
    if (op == '*' || op == '/')
        return 2;
    return 0;
}

int main() {
    char infix[] = "(A-B/C)*(A/K-L)";
    char reversed[100];
    char postfix[100];
    char prefix[100];

    int n = strlen(infix);

    for (int i = 0; i < n; i++) {
        reversed[i] = infix[n - i - 1];
    }
    reversed[n] = '\0';

    for (int i = 0; i < n; i++) {
        if (reversed[i] == '(')
            reversed[i] = ')';
        else if (reversed[i] == ')')
            reversed[i] = '(';
    }

    Stack s;
    int j = 0;

    for (int i = 0; i < n; i++) {
        char ch = reversed[i];

        if (isalnum(ch)) {
            postfix[j++] = ch;
        }

        else if (ch == '(') {
            s.push(ch);
        }

        else if (ch == ')') {
            while (!s.isEmpty() && s.peek() != '(') {
                postfix[j++] = s.pop();
            }
            s.pop(); 
        }

        else {
            while (!s.isEmpty() &&
                   s.peek() != '(' &&
                   precedence(s.peek()) >= precedence(ch)) {
                postfix[j++] = s.pop();
            }
            s.push(ch);
        }
    }

    while (!s.isEmpty()) {
        postfix[j++] = s.pop();
    }

    postfix[j] = '\0';

    int len = strlen(postfix);

    for (int i = 0; i < len; i++) {
        prefix[i] = postfix[len - i - 1];
    }
    prefix[len] = '\0';

    cout << "Infix Expression  : " << infix << endl;
    cout << "Prefix Expression : ";

    for (int i = 0; i < len; i++) {
        cout << prefix[i] << " ";
    }

    cout << endl;

    return 0;
}