#include <iostream>
using namespace std;

class Temperature {
private:
    double celsius;

public:
    // Member function to set Celsius value
    void setCelsius(double c) {
        celsius = c;
    }

    // Member function to convert and return value in Fahrenheit
    // Uses default argument: isCelsiusInput = true assumes the stored/passed value is in Celsius
    double toFahrenheit(double temp = -1000.0, bool isCelsiusInput = true) {
        double cVal = (temp == -1000.0) ? celsius : temp;
        if (isCelsiusInput) {
            return (cVal * 9.0 / 5.0) + 32.0;
        } else {
            return cVal; // already in Fahrenheit
        }
    }
};

int main() {
    Temperature t;
    t.setCelsius(37.0);

    cout << "=== Temperature Conversion ===" << endl;
    cout << "Stored Temperature in Celsius: 37 C" << endl;
    cout << "Converted to Fahrenheit (using default argument): " 
         << t.toFahrenheit() << " F" << endl;

    cout << "\nConverting 100 C explicitly: " 
         << t.toFahrenheit(100.0) << " F" << endl;
    cout << "Converting 0 C explicitly: " 
         << t.toFahrenheit(0.0) << " F" << endl;

    return 0;
}
