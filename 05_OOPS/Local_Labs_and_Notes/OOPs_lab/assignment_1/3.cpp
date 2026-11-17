#include <iostream>
using namespace std;

int main() {
    int N;

    cout << "Enter N: ";
    cin >> N;

    cout << "Prime numbers between 1 and " << N << " are: ";

    for (int num = 2; num <= N; num++) {
        int count = 0;

        for (int i = 1; i <= num; i++) {
            if (num % i == 0)
                count++;
        }

        if (count == 2)
            cout << num << " ";
    }

    return 0;
}