#include <bits/stdc++.h>
using namespace std;

vector<int> first_unique_element(vector<int> arr) {
    vector<int> temp = arr;

    sort(temp.begin(), temp.end());

    vector<int> unique;

    for (int i = 0; i < temp.size(); ) {
        int count = 1;        while (i + count < temp.size() && temp[i] == temp[i + count]) {
            count++;
        }
        if (count == 1) {
            unique.push_back(temp[i]);
        }
        i += count;
    }
    for (int x : arr) {
        for (int u : unique) {
            if (x == u) {
                return {x};
            }
        }
    }
    return {-1};
}

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    vector<int> result = first_unique_element(arr);
    cout << result[0] << endl;
}