#include <bits/stdc++.h>
using namespace std;

class Stack {
     char elements[100];
     int top;

public:
    Stack() {
        top = -1;
    }

    void push(char ch) {
        elements[++top] = ch;
    }

    char pop() {
        return elements[top--];
    }

    char peek() {
        return elements[top];
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

bool checkOperator(char ch) {
    return ch == '+' || ch == '-' ||
           ch == '*' || ch == '/' || ch == '^';
}

string infix2postfix(string exp) {
    Stack s;
    string result;

    for (int i =0 ; i < exp.length(); i++) {
        char ch = exp[i];

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

        else if (checkOperator(ch)) {

            while (!s.isEmpty() && s.peek() != '(' &&(precedence(s.peek()) > precedence(ch) ||(precedence(s.peek()) == precedence(ch) && ch != '^'))) {

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
    string exp;

    cout << "Enter infix expression: ";
    cin >> exp;

    cout << "Postfix expression: "
         << infix2postfix(exp) << endl;

    return 0;
}