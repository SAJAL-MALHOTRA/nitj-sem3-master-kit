#include <bits/stdc++.h>
using namespace std;
struct Patient { string name; int pri; };
Patient pq[100];
int n = 0;

string level(int p) { return p == 1 ? "Emergency" : p == 2 ? "Serious" : "Normal"; }

void admit(string name, int p) {
    if (p < 1 || p > 3) { cout << "Priority must be 1, 2 or 3\n"; return; }
    if (n == 100) { cout << "Hospital queue full\n"; return; }
    int i = n - 1;
    while (i >= 0 && pq[i].pri > p) { pq[i + 1] = pq[i]; i--; }
    pq[i + 1] = {name, p};
    n++;
    cout << name << " admitted as " << level(p) << "\n";
}
void serve() {
    if (n == 0) { cout << "No patients waiting\n"; return; }
    cout << "Serving: " << pq[0].name << " [" << level(pq[0].pri) << "]\n";
    for (int i = 1; i < n; i++) pq[i - 1] = pq[i];
    n--;
}
void waiting() {
    if (n == 0) { cout << "No patients waiting\n"; return; }
    cout << "Waiting patients (in service order):\n";
    for (int i = 0; i < n; i++)
        cout << i + 1 << ". " << pq[i].name << " - " << level(pq[i].pri) << "\n";
}
void serveAll() {
    if (n == 0) { cout << "No patients waiting\n"; return; }
    cout << "Order in which patients are served:\n";
    int k = 1;
    while (n > 0) { cout << k++ << ". "; serve(); }
}
int main() {
    int ch, p; string name;
    do {
        cout << "\n1.Admit patient 2.Serve next 3.Show waiting 4.Serve all (show order) 5.Exit\nChoice: ";
        cin >> ch;
        switch (ch) {
            case 1: cout << "Name and priority (1/2/3): "; cin >> name >> p; admit(name, p); break;
            case 2: serve(); break;
            case 3: waiting(); break;
            case 4: serveAll(); break;
            case 5: break;
            default: cout << "Invalid choice\n";
        }
    } while (ch != 5);
}