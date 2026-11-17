#include <bits/stdc++.h>
using namespace std;



class Student {

private:
    string name;
    float marks[5];
    static int count;

public:

    void input_details() {

        cout << "Enter student name: ";
        cin >> name;

        cout << "Enter marks in 5 subjects: ";

        for (int i = 0; i < 5; i++) {
            cin >> marks[i];
        }

        count++;
    }


    void change_mark(int index, float newMark) {
        if (index >= 0 && index < 5) {
            marks[index] = newMark;
        }
    }


    // Task 1
    float calculate_average() {

        float sum = 0;

        for (int i = 0; i < 5; i++) {
            sum += marks[i];
        }

        return sum / 5;
    }


    void display() {

        cout << "Name: " << name << endl;

        cout << "Marks: ";

        for (int i = 0; i < 5; i++) {
            cout << marks[i] << " ";
        }

        cout << endl;

        cout << "Average: "
             << calculate_average()
             << endl;
    }


    static void display_count() {
        cout << "Number of Student objects: "
             << count << endl;
    }
};


int Student::count = 0;

void changeByValue(Student s) {

    s.change_mark(0, 100);
}


void changeByReference(Student &s) {

    s.change_mark(0, 100);
}


void changeByPointer(Student *s) {


    s->change_mark(1, 95);
}


float classAverage(Student arr[], int size) {

    float total = 0;

    for (int i = 0; i < size; i++) {
        total += arr[i].calculate_average();
    }

    return total / size;
}

class Product {

private:
    string productName;
    int stock[7];

public:

    void input_product() {

        cout << "Enter product name: ";
        cin >> productName;

        cout << "Enter stock for 7 days: ";

        for (int i = 0; i < 7; i++) {
            cin >> stock[i];
        }
    }


    int highestStockDay() {

        int highest = 0;

        for (int i = 1; i < 7; i++) {

            if (stock[i] > stock[highest]) {
                highest = i;
            }
        }

        return highest + 1;
    }


    void display_product() {

        cout << "Product: " << productName << endl;

        cout << "Highest stock was on Day "
             << highestStockDay()
             << endl;
    }
};


class Warehouse {

private:
    Product products[10];
    int count;

public:

    Warehouse() {
        count = 0;
    }


    void addProduct(Product p) {

        if (count < 10) {

            products[count] = p;
            count++;

            cout << "Product added successfully." << endl;
        }
        else {
            cout << "Warehouse is full." << endl;
        }
    }


    void displayAllProducts() {
        if (count == 0) {
            cout << "No products in warehouse." << endl;
            return;
        }

        for (int i = 0; i < count; i++) {

            cout << "Product " << i + 1 << endl;
            products[i].display_product();
        }
    }
};

void addOneProduct(Warehouse &w) {

    Product p;

    p.input_product();

    w.addProduct(p);
}


int main() {

    cout << " TASK 1 "<<endl;

    Student s1;

    s1.input_details();

    cout << "Average: "
         << s1.calculate_average()
         << endl;

 cout << " TASK 2 "<<endl;
    Student arr[3];

    for (int i = 0; i < 3; i++) {

        cout << "\nStudent " << i + 1 << endl;

        arr[i].input_details();
    }


    cout << "\nStudent Summary\n";

    for (int i = 0; i < 3; i++) {

        cout << "\nStudent " << i + 1 << endl;

        arr[i].display();
    }


 cout << " TASK 3 "<<endl;
    cout << "Average before change: "
         << s1.calculate_average()
         << endl;

    changeByValue(s1);

    cout << "Average after change: "
         << s1.calculate_average()
         << endl;

    
 cout << " TASK 4 "<<endl;
    cout << "Average before change: "
         << s1.calculate_average()
         << endl;

    changeByReference(s1);

    cout << "Average after change: "
         << s1.calculate_average()
         << endl;


 cout << " TASK 5 "<<endl;
    cout << "Average before change: "
         << s1.calculate_average()
         << endl;

    changeByPointer(&s1);

    cout << "Average after change: "
         << s1.calculate_average()
         << endl;


 cout << " TASK 6 "<<endl;
    float overallAverage = classAverage(arr, 3);

    cout << "Overall Class Average: "
         << overallAverage
         << endl;

 cout << " TASK 7 "<<endl;
    Product products[3];

    for (int i = 0; i < 3; i++) {

        cout << "\nProduct " << i + 1 << endl;

        products[i].input_product();
    }


    cout << "\nProduct Summary\n";

    for (int i = 0; i < 3; i++) {

        cout << "Product " << i + 1 << endl;

        products[i].display_product();
    }


 cout << " TASK 8 "<<endl;
    Warehouse warehouse;

    cout << "\nEnter a product to add to warehouse:\n";

    addOneProduct(warehouse);

    cout << "\nWarehouse Products:\n";

    warehouse.displayAllProducts();

    cout << " TASK 9 "<<endl;

    Student::display_count();

    return 0;
}