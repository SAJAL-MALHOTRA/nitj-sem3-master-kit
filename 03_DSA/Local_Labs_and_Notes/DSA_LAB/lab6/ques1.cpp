#include<bits/stdc++.h>
using namespace std;

int main(){
  stack<char> s;
  string str;
  cout << "Enter the string to reverse : ";
  cin >> str;

  for (int i = 0; i < str.length(); i++) {
    s.push(str[i]);
  }
  cout << "Reversed string is : ";
  while (!s.empty()) {
    cout << s.top();
    s.pop();
  }
}