#include <iostream>
using namespace std;

int q[100], front = 0, rear = -1, cnt = 0;

void enqueue(int x)
{
  if (cnt == 100)
  {
    cout << "Queue Overflow\n";
    return;
  }
  rear = (rear + 1) % 100;
  q[rear] = x;
  cnt++;
  cout << x << " enqueued\n";
}

void dequeue()
{
  if (cnt == 0)
  {
    cout << "Queue Underflow\n";
    return;
  }
  cout << q[front] << " dequeued\n";
  front = (front + 1) % 100;
  cnt--;
}

void peek()
{
  if (cnt == 0)
    cout << "Queue is empty\n";
  else
    cout << "Front element: " << q[front] << "\n";
}

void display()
{
  if (cnt == 0)
  {
    cout << "Queue is empty\n";
    return;
  }
  cout << "Queue: ";
  for (int i = 0, p = front; i < cnt; i++, p = (p + 1) % 100)
    cout << q[p] << " ";
  cout << "\n";
}

int main()
{
  int ch, x;
  while (true)
  {
    cout << "\n1.Enqueue 2.Dequeue 3.Peek 4.Display 5.Exit\nChoice: ";
    if (!(cin >> ch) || ch == 5)
      break;
    switch (ch)
    {
    case 1:
      cout << "Value: ";
      if (!(cin >> x)) return 0;
      enqueue(x);
      break;
    case 2:
      dequeue();
      break;
    case 3:
      peek();
      break;
    case 4:
      display();
      break;
    default:
      cout << "Invalid choice\n";
    }
  }
  return 0;
}