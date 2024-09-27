#include <iostream>
using namespace std;

struct node {
  int data;
  struct node *left, *right;
};

struct node* newNode(int data) {
  struct node* temp = new struct node;
  temp->data = data;
  temp->left = temp->right = NULL;
  return temp;
};
void PreOrder(struct node* node) {
  if(node==NULL)
    return;
  cout << node->data << " ";
  PreOrder(node->left);
  PreOrder(node->right);
};
void InOrder(struct node* node) {
  if(node == NULL)
    return;
  InOrder(node->left);
  cout << node->data << " ";
  InOrder(node->right);
};

void PostOrder(struct node* node){
      if (node == NULL)
          return;
      PostOrder(node->left);
      PostOrder(node->right);
      cout << node->data << " ";
  };

  int main() {
    struct node* root = newNode(8);
    root->left = newNode(6);
    root->right = newNode(13);
    root->left->left = newNode(4);
    root->left->right = newNode(5);

    cout << "PreOrder: ";
    PreOrder(root);
    cout << endl;

    cout << "InOrder: ";
    InOrder(root);
    cout << endl;

    cout << "PostOrder: ";
    PostOrder(root);
    cout << endl;

    return 0;
  };
