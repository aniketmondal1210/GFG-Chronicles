// User function Template for C++

/*create binary tree struct node*/
// your code here
// Solution.cpp - NODE definition with default constructor

#include <cstddef> // for nullptr

struct NODE {
    bool isLeaf; // true -> data is valid, false -> children are valid

    union {
        double data; // used when isLeaf == true
        struct {
            NODE* left;
            NODE* right;
        } children; // used when isLeaf == false
    };

    // default ctor (makes a leaf with value 0.0)
    NODE() {
        isLeaf = true;
        data = 0.0;
    }

    // leaf constructor
    NODE(double val) {
        isLeaf = true;
        data = val;
    }

    // internal node constructor
    NODE(NODE* l, NODE* r) {
        isLeaf = false;
        children.left = l;
        children.right = r;
    }
};
