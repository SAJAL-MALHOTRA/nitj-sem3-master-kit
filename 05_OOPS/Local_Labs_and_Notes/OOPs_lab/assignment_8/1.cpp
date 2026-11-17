// Task 1: Default constructor
#include<bits/stdc++.h>
using namespace std;

class BankAccount {
private:
    int accountNumber;
    double balance;
    string accountHolder;

public:
    // Default constructor
    BankAccount() {
        accountNumber = 0;
        balance = 0.0;
        accountHolder = "Unknown";
    }

    void display() const {
        cout << fixed << setprecision(2);   // show balance with 2 decimal places
        cout << "Account Number : " << accountNumber << endl;
        cout << "Account Holder : " << accountHolder << endl;
        cout << "Balance        : " << balance << endl;
    }
};

int main() {
    BankAccount acc;   // default constructor is called here
    cout << "--- Account Details ---" << endl;
    acc.display();
    return 0;
}