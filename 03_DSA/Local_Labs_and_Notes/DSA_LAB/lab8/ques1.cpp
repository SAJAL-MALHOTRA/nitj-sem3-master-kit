#include <bits/stdc++.h>
using namespace std;
int q[100], front = 0, rear = -1;

void enqueue(int x) {
    if (rear == 99) { cout << "Queue Overflow"<<endl; return; }
    q[++rear] = x;
    cout << x << " enqueued"<<endl;
}
void dequeue() {
    if (front > rear) { cout << "Queue Underflow"<<endl; return; }
    cout << q[front++] << " dequeued"<<endl;
    if (front > rear) { front = 0; rear = -1; } 
}
void peek() {
    if (front > rear) {cout << "Queue is empty"<<endl; }
    else{cout << "Front element: " << q[front] << endl; }
}
void display() {
    if (front > rear) { cout << "Queue is empty"<<endl; return; }
    cout << "Queue: ";
    for (int i = front; i <= rear; i++) cout << q[i] << " ";
    cout << "\n";
}
int main() {   
   int ch, x;
    do {
        cout << "\n1.Enqueue 2.Dequeue 3.Peek 4.Display 5.Exit\nChoice: ";
        cin >> ch;
        switch (ch) {
            case 1: cout << "Value: "; cin >> x; enqueue(x); break;
            case 2: dequeue(); break;
            case 3: peek(); break;
            case 4: display(); break;
            case 5: break;
            default: cout << "Invalid choice\n";
        }
    } while (ch != 5);
}
