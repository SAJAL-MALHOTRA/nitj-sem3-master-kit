#include <iostream>
#include <string>
using namespace std;

class Book {
private:
    string title;
    string author;
    int availableCopies;

public:
    // Member functions declaration
    void setDetails(string t, string a, int copies);
    void displayDetails();
    void issueCopy();
};

// Defining member functions outside the class using Scope Resolution Operator (::)
void Book::setDetails(string t, string a, int copies) {
    title = t;
    author = a;
    availableCopies = copies;
}

void Book::displayDetails() {
    cout << "Title: " << title 
         << " | Author: " << author 
         << " | Available Copies: " << availableCopies << endl;
}

void Book::issueCopy() {
    if (availableCopies > 0) {
        availableCopies--;
        cout << "Successfully issued 1 copy of \"" << title << "\". Copies left: " << availableCopies << endl;
    } else {
        cout << "Sorry, \"" << title << "\" is currently out of stock!" << endl;
    }
}

int main() {
    Book b1, b2;

    b1.setDetails("The C++ Programming Language", "Bjarne Stroustrup", 2);
    b2.setDetails("Clean Code", "Robert C. Martin", 1);

    cout << "=== Initial Book Records ===" << endl;
    b1.displayDetails();
    b2.displayDetails();

    cout << "\n=== Issuing Copies ===" << endl;
    b1.issueCopy();
    b1.issueCopy();
    b1.issueCopy(); // Attempt to issue when 0 copies left

    cout << endl;
    b2.issueCopy();
    b2.issueCopy(); // Attempt to issue when 0 copies left

    cout << "\n=== Final Book Records ===" << endl;
    b1.displayDetails();
    b2.displayDetails();

    return 0;
}
