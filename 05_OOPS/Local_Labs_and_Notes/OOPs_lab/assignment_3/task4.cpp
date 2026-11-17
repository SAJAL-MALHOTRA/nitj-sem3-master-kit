#include <iostream>
using namespace std;
int value = 100; 
void displayValues() {
    int value = 25;
    cout << "Local Variable Value: " << value << endl;
    cout << "Global Variable Value: " << ::value << endl;
}

int main() {
    displayValues();
    // cout<<value;
    return 0;
}