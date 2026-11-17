#include <iostream>
using namespace std;

int main() {
    int num, digit;
    int product = 1;

    cout << "Enter a number: ";
    cin >> num;

    if (num == 0) {
        product = 0;
    }
    else {
        if (num < 0)
            num = -num;

        while (num > 0) {
            digit = num % 10;
            product = product * digit;
            num = num / 10;
        }
    }

    cout << "Product of digits = " << product << endl;

    return 0;
}