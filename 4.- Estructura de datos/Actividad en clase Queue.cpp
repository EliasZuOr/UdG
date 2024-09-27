#include <iostream>
using namespace std;
class Vertex {
public:
  Vertex *next;
  int value;


  Vertex(int value) { this->value = value; }
};

class List {

  Vertex *head, *tail;

public:
  List() { head = tail = nullptr; }
  Vertex* PopHead();
  void print();
  void PopTail();
  void PushTail(int value);
  int temp;
  int getLength();
};
int main() {
  List lista;
  lista.print();
  lista.PushTail(5);
  lista.PushTail(10);
  lista.PushTail(15);
  lista.PushTail(20);
  lista.PopHead();
  lista.PopTail();
  lista.print();
  lista.getLength();
}
int List::getLength() {

  if (head == nullptr) {
    cout << "Tu lista esta vacia" << endl;
    return 0;
  }

  Vertex *temp = head;
  int i = 0;
  while (temp != nullptr) {
    temp = temp->next;
    i++;
  }
  return i;
}

void List::print() {
  if (head == nullptr) {
    cout << "Tu lista esta vacia" << endl;
    return;
  }
  Vertex *temp = head;
  cout << endl;
  while (temp != nullptr) {
    cout << temp->value << " ";

    temp = temp->next;
  }
  cout << endl;
}


void List:: PopTail(){
  if (head == nullptr) {
    cout << "Tu lista esta vacia\n";
    return;
  }
  
  Vertex *temp = head;
  head = head->next;
  delete temp;
}

Vertex* List:: PopHead(){
  
  if (head == nullptr) {
    cout << "Tu lista esta vacia\n";
    return 0;
  }
  
  Vertex *temp = head;
  Vertex *pre = nullptr;
  while (temp != nullptr){
    pre = temp;
    temp = temp -> next;

    if (temp == nullptr){
      head = tail = nullptr;
      delete temp;
      return pre;
    }

    if (temp -> next == nullptr){
      pre -> next = nullptr;
      tail = pre;
      return temp;
    }
  }  
}

void List::PushTail(int value) {
  Vertex *vtx = new Vertex(value);
  if (head == nullptr) {
    head = tail = vtx;
    return;
  }
  tail->next = vtx;
  tail = vtx;
}