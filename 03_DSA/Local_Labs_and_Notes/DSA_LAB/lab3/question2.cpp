#include <bits/stdc++.h>
using namespace std;
int main() {
    int matrix[4][4] = {
        {0, 50, 0, 0},
        {0, 0, 12, 0},
        {0, 0, 0, 0},
        {75, 0, 50, 0}
    };
    int triplet[16][3];
    int c = 0;

    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (matrix[i][j] != 0) {
                triplet[c][0] = i;
                triplet[c][1] = j;
                triplet[c][2] = matrix[i][j];
                c++;
            }
        }
    }

    cout << "Triplet List:\n";

    for (int i = 0; i < c; i++) {
        cout << " " << triplet[i][0] << " "<< triplet[i][1] << " "<< triplet[i][2] << " "<<endl;
    }

    int target = 50;
    int count = 0;

    cout << "Positions of " << target << endl;

    for (int i = 0; i < c; i++) {
        if (triplet[i][2] == target) {
            cout << "Row = " << triplet[i][0]<< ", Column = " << triplet[i][1] << endl;
            count++;
        }
    }

    cout << "Total occurrences = " << count << endl;

    return 0;
}