#include <iostream>
using namespace std;
class Circle {
private:
    double radius;

public:
    void setRadius(double r);
    double getArea() const;
};

void Circle::setRadius(double r) {
    radius = r;
}

double Circle::getArea() const {
    return 3.14 * radius * radius;
}

int main() {
    Circle c;
    c.setRadius(5.0);
    cout << "Circle Area: " << c.getArea() << std::endl;
    return 0;
}