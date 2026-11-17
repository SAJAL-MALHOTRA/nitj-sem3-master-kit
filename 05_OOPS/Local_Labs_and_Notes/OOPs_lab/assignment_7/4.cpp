#include<bits/stdc++.h>
using namespace std;

class Employee {
public:
    int employeeId;
    string name;
    double salary;

    Employee(int id, string n, double sal) : employeeId(id), name(n), salary(sal) {}

    void display() const {
        cout << "ID: " << employeeId << " | Name: " << name << " | Salary: Rs. " << salary << endl;
    }
};

int main() {
    int N = 5;
    cout << "Allocating array of " << N << " Employee pointers" << endl;

    Employee** employees = new Employee*[N];

    employees[0] = new Employee(101, "Aarav", 55000.0);
    employees[1] = new Employee(102, "naman", 85000.0);  
    employees[2] = new Employee(103, "sajal", 72000.0);  
    employees[3] = new Employee(104, "Divyank", 68000.0);   
    employees[4] = new Employee(105, "pritansh", 42000.0);

    cout << " All Employee Records " << endl;
    for (int i = 0; i < N; i++) {
        employees[i]->display();
    }

    Employee* sortedList[5];
    for (int i = 0; i < N; i++) sortedList[i] = employees[i];
    sort(sortedList, sortedList + N, [](Employee* a, Employee* b) {
        return a->salary > b->salary;
    });

    cout << " Employee with Third-Highest Salary " << endl;
    sortedList[2]->display();

    double threshold = 50000.0;
    cout << "\nThreshold for deletion: Rs. " << threshold << endl;

    for (int i = 0; i < N; i++) {
        if (employees[i] != nullptr && employees[i]->salary < threshold) {
            cout << "Deleting employee " << employees[i]->name 
                 << " (Salary " << employees[i]->salary << " < " << threshold << ")" << endl;
            delete employees[i];
            employees[i] = nullptr; 
        }
    }

    cout << " Remaining Active Employees " << endl;
    for (int i = 0; i < N; i++) {
        if (employees[i] != nullptr) {
            employees[i]->display();
        }
    }

    for (int i = 0; i < N; i++) {
        if (employees[i] != nullptr) {
            delete employees[i];
            employees[i] = nullptr;
        }
    }
    delete[] employees;
    employees = nullptr;

    cout << "All remaining objects and pointer array deallocated safely without memory leaks." << endl;

    return 0;
}
