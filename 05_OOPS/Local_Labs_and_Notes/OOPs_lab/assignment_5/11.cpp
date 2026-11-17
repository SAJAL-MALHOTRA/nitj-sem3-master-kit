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

    void display() const {
        cout << "Length: " << length << ", Width: " << width << endl;
    }

    // Friend function to modify private data
    friend void resetLength(Rectangle &r);
};

// Friend function modifying private member 'length' directly
void resetLength(Rectangle &r) {
    r.length = 0.0;
}

/*
Comment: Discuss the trade-off: since a friend function can freely read and modify private data
from outside the class, does this weaken encapsulation? When might that trade-off still be worth it?

Trade-off Discussion:
1. Does it weaken encapsulation?
   Yes, friendship creates tight coupling between external functions and the internal data representation
   of a class. If private member variables change, friend functions must also be updated, which partially
   erodes the boundary of data hiding.
2. When is the trade-off worth it?
   - Operator Overloading: e.g., stream insertion/extraction operators `operator<<` and `operator>>`, where
     the left operand is `std::ostream` and cannot be a class member.
   - High-performance inter-class cooperation: When two closely related classes (e.g., Matrix and Vector,
     or Node and LinkedList) need direct access for performance without exposing public setters to the outside world.
*/

int main() {
    Rectangle rect;
    rect.setDimensions(12.0, 5.0);

    cout << "=== Before Friend Function Modification ===" << endl;
    rect.display();

    resetLength(rect);

    cout << "\n=== After Friend Function Modification (Length Reset to 0) ===" << endl;
    rect.display();

    return 0;
}
