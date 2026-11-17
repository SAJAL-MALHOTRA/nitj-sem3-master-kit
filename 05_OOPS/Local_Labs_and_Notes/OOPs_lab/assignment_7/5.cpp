#include<bits/stdc++.h>
using namespace std;

struct Product {
    string name;
    double price;
};

int main() {
    int N = 6;
    cout << "Number of products: " << N << endl;

    Product* products = new Product[N];
    products[0] = {"Wireless Mouse", 850.0};
    products[1] = {"Mechanical Keyboard", 3200.0};
    products[2] = {"USB-C Hub", 1500.0};
    products[3] = {"Gaming Monitor", 18500.0};
    products[4] = {"Noise-Canceling Headset", 6500.0};
    products[5] = {"Mousepad", 400.0};

    cout << " Product Catalog " << endl;
    double sum = 0.0;
    for (int i = 0; i < N; i++) {
        cout << (i + 1) << ". " << products[i].name << " : Rs. " << products[i].price << endl;
        sum += products[i].price;
    }

    double averagePrice = sum / N;
    cout << "\nTotal Catalog Price = Rs. " << sum << endl;
    cout << "Average Product Price = Rs. " << averagePrice << endl;

    Product* sortedProducts = new Product[N];
    for (int i = 0; i < N; i++) sortedProducts[i] = products[i];
    sort(sortedProducts, sortedProducts + N, [](const Product& a, const Product& b) {
        return a.price > b.price;
    });

    cout << " Top 3 Most Expensive Products " << endl;
    for (int i = 0; i < 3 && i < N; i++) {
        cout << (i + 1) << ". " << sortedProducts[i].name << " - Rs. " << sortedProducts[i].price << endl;
    }
    delete[] sortedProducts; 

    int countAbove = 0;
    for (int i = 0; i < N; i++) {
        if (products[i].price > averagePrice) countAbove++;
    }

    Product* aboveAverage = new Product[countAbove];
    int idx = 0;
    for (int i = 0; i < N; i++) {
        if (products[i].price > averagePrice) {
            aboveAverage[idx++] = products[i];
        }
    }

    cout << " Products Priced Above Average (> Rs. " << averagePrice << ")" << endl;
    for (int i = 0; i < countAbove; i++) {
        cout << (i + 1) << ". " << aboveAverage[i].name << " - Rs. " << aboveAverage[i].price << endl;
    }

    delete[] products;
    delete[] aboveAverage;
    products = nullptr;
    aboveAverage = nullptr;

    cout << "Both product arrays properly deallocated." << endl;

    return 0;
}
