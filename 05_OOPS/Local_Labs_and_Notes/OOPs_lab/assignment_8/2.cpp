// Task 2: Parameterized constructor
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

    void display() const {
        cout << fixed << setprecision(2);   // show balance with 2 decimal places
        cout << "Account Number : " << accountNumber << endl;
        cout << "Account Holder : " << accountHolder << endl;
        cout << "Balance        : " << balance << endl;
    }
};

int main() {
    BankAccount acc1(101, 5000.50, "Rahul Sharma");
    BankAccount acc2(102, 12000.75, "Priya Singh");

    cout << "--- Account 1 ---" << endl;
    acc1.display();

    cout << "\n--- Account 2 ---" << endl;
    acc2.display();

    return 0;
}