// Task 4: Dynamic constructor and destructor
#include<bits/stdc++.h>
using namespace std;

class BankAccount {
private:
    int accountNumber;
    string accountHolder;
    double *balance;   // pointer to dynamically allocated balance

public:
    // Dynamic constructor: allocates memory for balance using new
    BankAccount(int accNo, string holder, double bal) {
        accountNumber = accNo;
        accountHolder = holder;
        balance = new double;
        *balance = bal;
    }

    void display() const {
        cout << fixed << setprecision(2);   // show balance with 2 decimal places
        cout << "Account Number : " << accountNumber << endl;
        cout << "Account Holder : " << accountHolder << endl;
        cout << "Balance        : " << *balance << endl;
    }

    // Destructor: releases the dynamically allocated memory using delete
    ~BankAccount() {
        delete balance;
        cout << "\nDestructor called: memory for balance released." << endl;
    }

    // Copying would make two objects share one pointer (double delete),
    // so it is disabled.
    BankAccount(const BankAccount &) = delete;
    BankAccount &operator=(const BankAccount &) = delete;
};

int main() {
    BankAccount acc(201, "Amit Verma", 25000.0);

    cout << "--- Account Details ---" << endl;
    acc.display();

    return 0;   // acc goes out of scope here, so the destructor runs
}