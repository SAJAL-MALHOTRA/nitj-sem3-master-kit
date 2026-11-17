#include<bits/stdc++.h>
using namespace std;

int main() {
    int N = 3;
    cout << "Initial number of employees: " << N << endl;

    double* salaries = new double[N];
    salaries[0] = 45000.0;
    salaries[1] = 60000.0;
    salaries[2] = 52000.0;

    cout << "Initial salaries: ";
    for (int i = 0; i < N; i++) {
        cout << salaries[i] << " ";
    }
    cout << endl;
    double incomingSalaries[] = {75000.0, 48000.0, 92000.0, -1.0};
    int inputIdx = 0;

    cout << "Adding New Employees Dynamically Without realloc()" << endl;
    while (true) {
        double newSalary = incomingSalaries[inputIdx++];
        cout << "Enter salary (-1 to stop): " << newSalary << endl;
        if (newSalary == -1.0) break;

        double* newArray = new double[N + 1];

        for (int i = 0; i < N; i++) {
            newArray[i] = salaries[i];
        }

        newArray[N] = newSalary;
        delete[] salaries;
        salaries = newArray;
        N++;

        cout << "Employee joined! New array size = " << N << ". Current salaries: [ ";
        for (int i = 0; i < N; i++) cout << salaries[i] << " ";
        cout << "]" << endl;
    }

    sort(salaries, salaries + N);

    cout << " Final Salaries in Ascending Order " << endl;
    for (int i = 0; i < N; i++) {
        cout << "Salary " << (i + 1) << ": Rs. " << salaries[i] << endl;
    }

    delete[] salaries;
    salaries = nullptr;
    cout << " Memory released successfully. No memory leaks." << endl;

    return 0;
}
