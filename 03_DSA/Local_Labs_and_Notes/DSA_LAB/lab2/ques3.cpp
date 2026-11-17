#include <bits/stdc++.h>
using namespace std;

int search_insert(vector<int> arr, int target) {
    int left = 0;
    int right = arr.size() - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) {
            return mid;
        }
        else if (arr[mid] < target) {
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
    }

    return left;
}
int main() {
    vector<int> sorted_array = {1, 3, 5, 6};

    int target;
    cin >> target;
    cout << search_insert(sorted_array, target);
    return 0;
}