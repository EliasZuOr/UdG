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
  void Push(int value);
  Vertex* PopHead();
  void print();
  int temp;
  int getLength();
};
int main() {
  List lista;
  lista.print();
  lista.Push(5);
  lista.Push(10);
  lista.Push(15);
  lista.Push(20);
  lista.PopHead();
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

void List::Push(int value) {
  Vertex *vtx = new Vertex(value);
  if (head == nullptr) {
    head = tail = vtx;
    return;
  }

  vtx->next = head;
  head = vtx;
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