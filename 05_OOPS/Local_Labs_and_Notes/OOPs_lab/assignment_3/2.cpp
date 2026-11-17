#include <iostream>
using namespace std;

class Rectangle {
private:
    double length;
    double width;

public:
    // Member function to set both values
    void setDimensions(double l, double w) {
        length = l;
        width = w;
    }

    // Member function to calculate and return the area
    double getArea() {
        return length * width;
    }
};

int main() {
    Rectangle rect;
    rect.setDimensions(10.5, 4.0);

    cout << "=== Rectangle Details ===" << endl;
    cout << "Length: 10.5, Width: 4.0" << endl;
    cout << "Calculated Area: " << rect.getArea() << endl;

    return 0;
}
