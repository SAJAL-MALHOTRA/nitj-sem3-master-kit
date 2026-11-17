#include <iostream>
#include <string>
using namespace std;
struct Item { string data; int pri; };
Item pq[100];
int n = 0;

void insert(string d, int p) {
    if (n == 100) { cout << "Queue Overflow\n"; return; }
    int i = n - 1;
    while (i >= 0 && pq[i].pri > p) { pq[i + 1] = pq[i]; i--; }
    pq[i + 1] = {d, p};
    n++;
    cout << d << " inserted with priority " << p << "\n";
}
void del() {
    if (n == 0) { cout << "Queue Underflow\n"; return; }
    cout << "Deleted: " << pq[0].data << " (priority " << pq[0].pri << ")\n";
    for (int i = 1; i < n; i++) pq[i - 1] = pq[i];
    n--;
}
void peek() {
    if (n == 0) cout << "Queue is empty\n";
    else cout << "Highest priority: " << pq[0].data << " (priority " << pq[0].pri << ")\n";
}
void display() {
    if (n == 0) { cout << "Queue is empty\n"; return; }
    cout << "Data\tPriority\n";
    for (int i = 0; i < n; i++) cout << pq[i].data << "\t" << pq[i].pri << "\n";
}
int main() {
    int ch, p; string d;
    do {
        cout << "\n1.Insert 2.Delete 3.Peek 4.Display 5.Exit\nChoice: ";
        cin >> ch;
        switch (ch) {
            case 1: cout << "Data and priority: "; cin >> d >> p; insert(d, p); break;
            case 2: del(); break;
            case 3: peek(); break;
            case 4: display(); break;
            case 5: break;
            default: cout << "Invalid choice\n";
        }
    } while (ch != 5);
}