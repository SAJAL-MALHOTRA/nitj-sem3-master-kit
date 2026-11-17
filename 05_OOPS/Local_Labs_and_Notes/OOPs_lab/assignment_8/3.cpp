// Task 3: Copy constructor
#include<bits/stdc++.h>
using namespace std;

class BankAccount {
private:
    int accountNumber;
    double balance;
    string accountHolder;

public:
    // Parameterized constructor
    BankAccount(int accNo, double bal, string holder) {
        accountNumber = accNo;
        balance = bal;
        accountHolder = holder;
    }

    // Copy constructor
    BankAccount(const BankAccount &other) {
        accountNumber = other.accountNumber;
        balance = other.balance;
        accountHolder = other.accountHolder;
    }

    void display() const {
        cout << fixed << setprecision(2);   // show balance with 2 decimal places
        cout << "Account Number : " << accountNumber << endl;
        cout << "Account Holder : " << accountHolder << endl;
        cout << "Balance        : " << balance << endl;
    }
};

int main() {
    BankAccount acc1(101, 5000.50, "Rahul Sharma");
    BankAccount acc2(acc1);   // copy constructor is called here

    cout << "--- Original Account (acc1) ---" << endl;
    acc1.display();

    cout << "\n--- Copied Account (acc2) ---" << endl;
    acc2.display();

    return 0;
}