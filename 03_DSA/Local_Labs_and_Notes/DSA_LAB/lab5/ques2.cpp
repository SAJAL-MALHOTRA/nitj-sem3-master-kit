#include <bits/stdc++.h>
using namespace std;

struct Node {
    int id, priority;
    Node *prev = nullptr, *next = nullptr;
    Node(int id, int priority) : id(id), priority(priority) {}
};

class Event {
    Node *head = nullptr, *tail = nullptr;
    unordered_map<int, Node*> byId;

    Node* find(int id) {
        return byId.count(id) ? byId[id] : nullptr;
    }

    void add(Node*& first, Node*& last, Node* node) {
        node->prev = last;
        node->next = nullptr;
        if (last) last->next = node;
        else first = node;
        last = node;
    }

public:
    ~Event() {
        while (head) removeById(head->id);
    }

    void insertAtBeginning(int id, int priority) {
        Node* node = new Node(id, priority);
        node->next = head;
        if (head) head->prev = node;
        else tail = node;
        head = byId[id] = node;
    }

    void insertAtEnd(int id, int priority) {
        Node* node = new Node(id, priority);
        node->prev = tail;
        if (tail) tail->next = node;
        else head = node;
        tail = byId[id] = node;
    }

    bool insertAfter(int afterId, int id, int priority) {
        Node* after = find(afterId);
        if (!after) return false;

        Node* node = new Node(id, priority);
        node->prev = after;
        node->next = after->next;
        if (after->next) after->next->prev = node;
        else tail = node;
        after->next = byId[id] = node;
        return true;
    }

    bool removeById(int id) {
        Node* node = find(id);
        if (!node) return false;

        if (node->prev) node->prev->next = node->next;
        else head = node->next;
        if (node->next) node->next->prev = node->prev;
        else tail = node->prev;

        byId.erase(id);
        delete node;
        return true;
    }

    bool reverseSlot(int startId, int endId) {
        Node *start = find(startId), *end = find(endId);
        if (!start || !end) return false;

        Node* p = start;
        while (p && p != end) p = p->next;
        if (!p) return false; 

        Node *before = start->prev, *after = end->next;
        for (p = start;; p = p->prev) {
            swap(p->prev, p->next);
            if (p == end) break;
        }

        if (before) before->next = end;
        else head = end;
        end->prev = before;

        if (after) after->prev = start;
        else tail = start;
        start->next = after;
        return true;
    }

    void reverseInBatches(int k) {
        for (Node* first = head; k > 1 && first;) {
            Node* last = first;
            for (int i = 1; i < k && last; i++) last = last->next;
            if (!last) break;
            if (!last->next) break;
            Node* nextBatch = last->next;
            reverseSlot(first->id, last->id);
            first = nextBatch;
        }
    }

    vector<int> partitionByPriority(int threshold) {
        Node *highHead = nullptr, *highTail = nullptr;
        Node *lowHead = nullptr, *lowTail = nullptr;

        for (Node* p = head; p;) {
            Node* next = p->next;
            add(p->priority >= threshold ? highHead : lowHead,
                p->priority >= threshold ? highTail : lowTail, p);
            p = next;
        }

        if (highTail) highTail->next = lowHead;
        if (lowHead) lowHead->prev = highTail;
        head = highHead ? highHead : lowHead;
        tail = lowTail ? lowTail : highTail;

        vector<int> ids;
        for (Node* p = head; p; p = p->next) ids.push_back(p->id);
        return ids;
    }

    void printLineup() const {
        for (Node* p = head; p; p = p->next)
            cout << "(id=" << p->id << ",p=" << p->priority << ") ";
        cout << '\n';
    }
};

int main() {
    Event event;
    event.insertAtEnd(1, 5);
    event.insertAtEnd(2, 3);
    event.insertAtEnd(3, 8);
    event.insertAtEnd(4, 2);
    event.insertAtEnd(5, 7);

    cout << "Initial lineup:"<<endl;
    event.printLineup();

    cout << "Reversing slots between id=2 and id=4:"<<endl;
    if (event.reverseSlot(2, 4)) {
        event.printLineup();
    } else {
        cout << "Failed to reverse slots"<<endl;
    }

    cout << "Reversing in batches of size 2:"<<endl;
    event.reverseInBatches(2);
    event.printLineup();

    cout << "Partitioning by priority >= 5:"<<endl;
    vector<int> partitionedIds = event.partitionByPriority(5);
    cout << "Partitioned lineup ids: ";
    for (int id : partitionedIds) cout << id << " ";
    cout << "\n";

    return 0;
}