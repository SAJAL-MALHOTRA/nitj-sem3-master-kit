#include <bits/stdc++.h>
using namespace std;

struct DNode {
    int data;
    DNode* prev;
    DNode* next;
    DNode(int val) : data(val), prev(nullptr), next(nullptr) {}
};

DNode* insertAfter(DNode* head, int afterValue, int newValue) {
    DNode* curr = head;
    while (curr && curr->data != afterValue) curr = curr->next;

    if (!curr) {
        cout << "Value " << afterValue << " not found." << endl;
        return head;
    }

    DNode* newNode = new DNode(newValue);
    newNode->next = curr->next;
    newNode->prev = curr;
    if (curr->next) curr->next->prev = newNode;
    curr->next = newNode;

    return head;
}

void printDList(DNode* head) {
    while (head) {
        cout << head->data;
        if (head->next) cout << " <-> ";
        head = head->next;
    }
    cout << endl;
}

int main() {
    DNode* n1 = new DNode(10);
    DNode* n2 = new DNode(20);
    DNode* n3 = new DNode(30);

    n1->next = n2; n2->prev = n1;
    n2->next = n3; n3->prev = n2;

    cout << "Before: "; printDList(n1);
    n1 = insertAfter(n1, 20, 25);
    cout << "After: "; printDList(n1);
    return 0;
}