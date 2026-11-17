#include <iostream>
using namespace std;

class Box {
private:
    double length;
    double width;
    double height;

public:
    void setDimensions(double l, double w, double h) {
        length = l;
        width = w;
        height = h;
    }

    // Declaring friend function
    friend bool areVolumesEqual(Box b1, Box b2);
};

// Friend function definition
bool areVolumesEqual(Box b1, Box b2) {
    double vol1 = b1.length * b1.width * b1.height;
    double vol2 = b2.length * b2.width * b2.height;
    return (vol1 == vol2);
}

int main() {
    Box box1, box2, box3;

    box1.setDimensions(2.0, 3.0, 4.0); // Volume = 24
    box2.setDimensions(4.0, 3.0, 2.0); // Volume = 24
    box3.setDimensions(5.0, 2.0, 3.0); // Volume = 30

    cout << "=== Comparing Box Volumes using Friend Function ===" << endl;
    cout << "Are Box 1 and Box 2 equal in volume? " 
         << (areVolumesEqual(box1, box2) ? "Yes (Equal)" : "No (Not Equal)") << endl;

    cout << "Are Box 1 and Box 3 equal in volume? " 
         << (areVolumesEqual(box1, box3) ? "Yes (Equal)" : "No (Not Equal)") << endl;

    return 0;
}
