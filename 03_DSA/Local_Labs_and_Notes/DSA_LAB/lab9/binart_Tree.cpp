/*
            1
           / \
          2   3
         / \ / \
        4  5 6  7
*/

#include<bits/stdc++.h>
using namespace std;

struct Node {
    int value;      // the data 
    Node* left;     // pointer to the left child 
    Node* right;    // pointer to the right child

    Node(int v) {
        value = v;
        left = nullptr;
        right = nullptr;
    }
};

void preOrder(Node* node) {
    if (node == nullptr) return;       
    cout << node->value << " ";        
    preOrder(node->left);              
    preOrder(node->right);             
}

void inOrder(Node* node) {
    if (node == nullptr) return;
    inOrder(node->left);
    cout << node->value << " ";
    inOrder(node->right);
}

void postOrder(Node* node) {
    if (node == nullptr) return;
    postOrder(node->left);
    postOrder(node->right);
    cout << node->value << " ";
}

int height(Node* node) {
    if (node == nullptr) return 0;
    int leftHeight  = height(node->left);
    int rightHeight = height(node->right);
    return 1 + max(leftHeight, rightHeight);
}

int countNodes(Node* node) {
    if (node == nullptr) return 0;
    return 1 + countNodes(node->left) + countNodes(node->right);
}

int countLeaves(Node* node) {
    if (node == nullptr) return 0;
    if (node->left == nullptr && node->right == nullptr) {
        return 1;                       
    }
    return countLeaves(node->left) + countLeaves(node->right);
}

int countInternal(Node* node) {
    if (node == nullptr) return 0;
    if (node->left == nullptr && node->right == nullptr) {
        return 0;                      
    }
    return 1 + countInternal(node->left) + countInternal(node->right);
}

bool contains(Node* node, int target) {
    if (node == nullptr) return false;         
    if (node->value == target) return true;    
    return contains(node->left, target) || contains(node->right, target);
}

void printTree(Node* node, int depth, string label) {
    if (node == nullptr) return;
    for (int i = 0; i < depth; i++) cout << "    ";     
    cout << label << ": " << node->value << "\n";
    printTree(node->left,  depth + 1, "Left");
    printTree(node->right, depth + 1, "Right");
}


void deleteTree(Node* node) {
    if (node == nullptr) return;
    deleteTree(node->left);
    deleteTree(node->right);
    delete node;
}

int main() {
    Node* root = new Node(1);

    root->left  = new Node(2);
    root->right = new Node(3);
    root->left->left   = new Node(4);   // children of 2
    root->left->right  = new Node(5);
    root->right->left  = new Node(6);   // children of 3
    root->right->right = new Node(7);

    cout << "Shape of the tree:\n";
    printTree(root, 0, "Root");
    cout << endl ;
    cout << "Pre-order  (node, left, right): ";  preOrder(root);   cout << "\n";
    cout << "In-order   (left, node, right): ";    inOrder(root);    cout << "\n";
    cout << "Post-order (left, right, node): ";    postOrder(root);  cout << "\n";

    cout << "\nHeight:         " << height(root)        << "\n";   // 3
    cout << "Total nodes:    " << countNodes(root)    << "\n";   // 7
    cout << "Leaf nodes:     " << countLeaves(root)   << "\n";   // 4 (4,5,6,7)
    cout << "Internal nodes: " << countInternal(root) << "\n";   // 3 (1,2,3)

    cout << boolalpha;  
    cout << "\nContains 4? " << contains(root, 4) << "\n";   
    cout << "Contains 8? " << contains(root, 8) << "\n";     

    deleteTree(root);    //free all nodes

    return 0;
}