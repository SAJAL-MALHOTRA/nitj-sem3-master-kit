#include <iostream>
using namespace std;

class Rectangle {
private:
    double length;
    double width;

public:
    void setDimensions(double l, double w) {
        length = l;
        width = w;
    }

    // Declaring friend function
    friend double calculateArea(Rectangle r);
};

/*
Comment: Explain how the friend function was able to access private data without being a member of the class:
By declaring `friend double calculateArea(Rectangle r);` inside the Rectangle class definition,
the class explicitly grants this external non-member function privileged access to its private and protected members.
Friendship bypasses standard class access control mechanisms strictly for the declared function.
*/

double calculateArea(Rectangle r) {
    // Accessing private members length and width directly
    return r.length * r.width;
}

int main() {
    Rectangle rect;
    rect.setDimensions(8.5, 4.0);

    cout << "=== Rectangle Area via Friend Function ===" << endl;
    cout << "Length: 8.5, Width: 4.0" << endl;
    cout << "Calculated Area: " << calculateArea(rect) << endl;

    return 0;
}
