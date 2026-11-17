#include <bits/stdc++.h>
using namespace std;

int main() {

    stack<char> s;
    string str;

    cout << "Enter the string to check for balanced parentheses: ";
    cin >> str;

    for (int i = 0; i < str.length(); i++) {

        char ch = str[i];

        if (ch == '(' || ch == '{' || ch == '[') {
            s.push(ch);
        }

        else if (ch == ')' || ch == '}' || ch == ']') {

            if (s.empty()) {
                cout << "False";
                return 0;
            }

            char open = s.top();
            s.pop();

            if ((open == '(' && ch != ')') ||
                (open == '{' && ch != '}') ||
                (open == '[' && ch != ']')) {

                cout << "False";
                return 0;
            }
        }
    }

    cout << (s.empty() ? "True" : "False");

    return 0;
}