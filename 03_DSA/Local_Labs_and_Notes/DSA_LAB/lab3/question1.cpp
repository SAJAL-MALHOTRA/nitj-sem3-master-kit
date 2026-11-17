#include<bits/stdc++.h>
using namespace std;
int main() {
    int matrix[3][4] = {
        {0, 0, 0, 15},
        {8, 0, 0, 0},
        {0, 0, 30, 0}
    };
    int c = 0 ;
    int triplet[12][3];
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
            if (matrix[i][j] != 0) {
                triplet[c][0] = i;
                triplet[c][1] = j;
                triplet[c][2] = matrix[i][j];
                c++;
            }
        }
    }
    cout << "Triplet List:"<<" ";
    for (int i = 0; i < c; i++) {
        cout << " " << triplet[i][0] << " "<< triplet[i][1] <<" "<< triplet[i][2] <<" "<<endl;
    }
    int target = 8;
    bool found = false;
    for (int i = 0; i < c; i++) {
        if (triplet[i][2] == target) {
            cout << "Value " << target<< " found at row "<< triplet[i][0]<< ", column "<< triplet[i][1] << endl;
            found = true;
        }
    }
    if (!found) {
        cout << "Value not found\n";
    }
    return 0;
}