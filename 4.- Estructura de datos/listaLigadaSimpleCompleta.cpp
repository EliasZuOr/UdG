#include <iostream>
#include <conio.h>

using namespace std;

class Nodo{
    public:
        Nodo *next;
        int value;
    Nodo(int value){this->value=value;}
};

class Lista{
    Nodo *head, *tail;
    public:
        List() { head = tail = nullptr; }
        void agregarDatoInicio(int);
        void agregarDatoFinal(string);
        void agregarDatoPosicion(string);
        void eliminarDatoInicio();
        void eliminarDatoFinal();
        void eliminarDatoPosicion();
        void eliminarTodo();
        void print();
        int temp;
    private:
};

int main(){
    Lista lista;

    lista.print();

    return 0;
};

void Lista::print() {
  if (head == nullptr) {
    cout << "Tu lista esta vacia" << endl;
    return;
  }
  Nodo *temp = head;
  cout << endl;
  while (temp != nullptr) {
    cout << temp->value << " ";
    temp = temp->next;
  }
  cout << endl;
}

void Lista::agregarDatoInicio(int value){
    Nodo *nodo = new Nodo(value);
    if (head == nullptr){
        head = tail = nodo;
        return;
    }
    tail->next=nodo;
    tail=nodo;
}

void Lista::agregarDatoFinal(int value){

}




