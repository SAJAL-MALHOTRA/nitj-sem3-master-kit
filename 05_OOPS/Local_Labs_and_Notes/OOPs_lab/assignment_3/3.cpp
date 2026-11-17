#include <iostream>
using namespace std;

class Circle {
private:
    double radius;

public:
    // Member functions only declared inside the class body
    void setRadius(double r);
    double calculateArea();
};

// Defining member functions outside the class using Scope Resolution Operator (::)
void Circle::setRadius(double r) {
    radius = r;
}

double Circle::calculateArea() {
    return 3.14159 * radius * radius;
}

int main() {
    Circle c;
    c.setRadius(7.0);

    cout << "=== Circle Details ===" << endl;
    cout << "Radius: 7.0" << endl;
    cout << "Area of Circle: " << c.calculateArea() << endl;

    return 0;
}
