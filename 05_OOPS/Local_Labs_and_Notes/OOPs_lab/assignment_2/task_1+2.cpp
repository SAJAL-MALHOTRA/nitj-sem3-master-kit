#include<bits/stdc++.h>
using namespace std;

inline long long square(int n) {
    return (long long)n * n;
}
inline long long cube(int n) {
    return (long long)n * n * n;
}
inline double areaCircle(double r) {
    return 3.14159 * r * r;
}
inline bool isEvene(int n) {
    return n % 2 == 0;
}
inline bool pallindrome(int num) {
    int original = num, rev = 0;
    while (num > 0) {
        rev = rev * 10 + num % 10;
        num = num/10;
    }
    return original == rev;
}
int main(){
  cout << "Square of 5: " << square(5) << endl;
  cout << "Square of 4: " << square(4) << endl;
  cout << "Square of 3: " << square(3) << endl;

  cout << "Cube of 3: " << cube(3) << endl;
  cout << "Cube of 4: " << cube(4) << endl;
  cout << "Cube of 5: " << cube(5) << endl;

  cout << "Area of circle with radius 2.5: " << areaCircle(2.5) << endl;
  cout << "Area of circle with radius 3.5: " << areaCircle(3.5) << endl;
  cout << "Area of circle with radius 4.5: " << areaCircle(4.5) << endl;
  cout << "Is 4 even? " << (isEvene(4) ? "Yes" : "No") << endl;
  cout << "Is 8 even? " << (isEvene(8) ? "Yes" : "No") << endl;
  cout << "Is 11 even? " << (isEvene(11) ? "Yes" : "No") << endl;
  cout << "Is 121 a palindrome? " << (pallindrome(121) ? "Yes" : "No") << endl;
  cout << "Is 1345 a palindrome? " << (pallindrome(1345) ? "Yes" : "No") << endl;
  cout << "Is 1003930 a palindrome? " << (pallindrome(1003930) ? "Yes" : "No") << endl;

}



// Since this function contains a loop, marking it inline may not provide much benefit;
// the compiler can decide whether inlining is worthwhile. Keep inline only if it is
// compiler dekhega if function worth hai being an inline function or not.
