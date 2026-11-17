#include <bits/stdc++.h>
using namespace std;

struct DNode {
    int data;
    DNode* prev;
    DNode* next;
    DNode(int val) : data(val), prev(nullptr), next(nullptr) {}
};

pair<int,long long> countAndSum(DNode* head) {
    int count = 0;
    long long sum = 0;
    while (head) {
        count++;
        sum += head->data;
        head = head->next;
    }
    return {count, sum};
}

int main() {
    DNode* n1 = new DNode(10);
    DNode* n2 = new DNode(20);
    DNode* n3 = new DNode(30);
    DNode* n4 = new DNode(40);

    n1->next = n2; n2->prev = n1;
    n2->next = n3; n3->prev = n2;
    n3->next = n4; n4->prev = n3;

    auto [count, sum] = countAndSum(n1);
    cout << "Nodes: " << count << ", Sum: " << sum << endl;
    return 0;
}