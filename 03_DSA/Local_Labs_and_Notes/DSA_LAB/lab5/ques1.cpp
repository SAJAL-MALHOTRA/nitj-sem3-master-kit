#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cout << "Enter N (number of days): ";
    cin >> n;

  int books_borrowed[n];
    for (int i = 0; i < n; i++){ 
      cin >> books_borrowed[i];
    }
    cout << endl;

    double totalSum = 0;
    for (int i = 0; i < n; i++){
       totalSum += books_borrowed[i]; 
      }
    cout << "Total books borrowed " << n << " days = " << totalSum << endl;

    double minVal = books_borrowed[0];
    int minIdx = 0;
    for (int i = 1; i < n; i++) {
        if (books_borrowed[i] < minVal) {
            minVal = books_borrowed[i];
            minIdx = i;
        }
    }
    cout << "Smallest value = " << minVal << " at day index " << minIdx << "\n";

    int deleteIndex;
    cout << "Enter index to delete (0 to " << n - 1 << "): "<< endl;
    cin >> deleteIndex;

    for (int i = deleteIndex; i < n - 1; i++) {
        books_borrowed[i] = books_borrowed[i + 1];
    }
    int newSize = n - 1;  

    cout << "Array after deletion  : ";
    for (int i = 0; i < newSize; i++){ 
      cout << books_borrowed[i] << " "; 
    }
    cout << "\n";

    int k;
    cout << "Enter window size k: "<<endl;
    cin >> k;

    cout << "Reverse order traversal: ";
    for (int i = newSize - 1; i >= 0; i--) cout << books_borrowed[i] << " ";
    cout << "\n";

    if (k <= 0 || k > newSize) {
        cout << "k is invalid , no valid window size exists for the given array"<<endl;
        return 0;
    }

    double windowSum = 0;
    for (int i = newSize - k; i <= newSize - 1; i++) {
        windowSum += books_borrowed[i];
    }
    double minWindowSum = windowSum;

    int i = newSize - 1;
    int j = newSize - k;


    while (j - 1 >= 0) {
        windowSum -= books_borrowed[i];   
        j--;
        i--;
        windowSum += books_borrowed[j];  
        minWindowSum = min(minWindowSum, windowSum);
    }

    cout << "Minimum sum in any continuous " << k << "-day window = " << minWindowSum << "\n";
    return 0;
}