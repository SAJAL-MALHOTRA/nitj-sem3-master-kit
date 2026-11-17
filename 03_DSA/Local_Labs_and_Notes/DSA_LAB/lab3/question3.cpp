#include <iostream>
using namespace std;

int main() {

    int triplet[][3] = {
        {0, 1, 45},
        {1, 3, 90},
        {2, 0, 15},
        {2, 2, 90},
        {2, 4, 30},
        {4, 1, 60}
    };

    int n = 6;

    int maxValue = triplet[0][2];

    for (int i = 1; i < n; i++) {
        if (triplet[i][2] > maxValue) {
            maxValue = triplet[i][2];
        }
    }
    cout << "Maximum value = " << maxValue << endl;
    cout << "Coordinates of maximum value:"<<endl;

    for (int i = 0; i < n; i++) {
        if (triplet[i][2] == maxValue) {
            cout << " " << triplet[i][0]
                 << " " << triplet[i][1] << " " << endl;
        }
      }

    int rowCount[6] = {0};

    for (int i = 0; i < n; i++) {
        int row = triplet[i][0];
        rowCount[row]++;
    }

    int maxCount = 0;
    int maxRow = 0;

    for (int i = 0; i < 6; i++) {
        if (rowCount[i] > maxCount) {
            maxCount = rowCount[i];
            maxRow = i;
        }
    }
    cout << "Row with most non-zero values = " << maxRow << endl;
    cout << "Number of non-zero values = "<< maxCount << endl;
    return 0;
}