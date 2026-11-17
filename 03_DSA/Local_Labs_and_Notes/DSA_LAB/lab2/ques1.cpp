#include <bits/stdc++.h>
using namespace std;
vector<int> search_2d_matrix(vector<vector<int>> matrix, int target) {
    int n = matrix.size();
    for (int row_index = 0; row_index < n; row_index++) {
        for (int col_index = 0; col_index < matrix[row_index].size(); col_index++) {
            if (matrix[row_index][col_index] == target) {
                return {row_index, col_index};
            }
        }
    }
    return {-1, -1};
}

int main() {
    int rows, cols;
    cout << "Enter number of rows: ";
    cin >> rows;
    cout << "Enter number of columns: ";
    cin >> cols;
    vector<vector<int>> matrix(rows, vector<int>(cols));
    cout << "Enter matrix elements:\n";
    for (int row = 0; row < rows; row++) {
        for (int col = 0; col < cols; col++) {
            cin >> matrix[row][col];
        }
    }
    int target;
    cout << "Enter target: ";
    cin >> target;
    vector<int> result = search_2d_matrix(matrix, target);
    if (result[0] == -1) {
        cout << "Element not found";
    }
    else {
        cout << "result row " << result[0]
             << "result column " << result[1];
    }
    return 0;
}