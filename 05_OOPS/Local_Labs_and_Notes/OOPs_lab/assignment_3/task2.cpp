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

    double getArea() const {
        return length * width;
    }
};

int main() {
    Rectangle rect;
    rect.setDimensions(10.5, 4.0);
    cout << "Rectangle Area: " << rect.getArea() <<endl;
    return 0;
}