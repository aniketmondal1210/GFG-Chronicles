#include <iostream>
#include <deque>
#include <algorithm>
using namespace std;

/* Prints space-separated elements of the deque A */
void print(deque<int> &A) {
    if (A.empty()) {
        cout << -1 << endl;
    } else {
        for (int x : A) {
            cout << x << " ";
        }
        cout << endl;
    }
}

/* Inserts an element x at the front of the deque A */
void add_in_front(deque<int> &A, int x) {
    A.push_front(x);
}

/* Inserts an element x at the back of the deque A */
void add_in_back(deque<int> &A, int x) {
    A.push_back(x);
}

/* Removes an element from the back of the deque A */
void remove_from_back(deque<int> &A) {
    if (!A.empty()) {
        A.pop_back();
    }
}

/* Removes an element from the front of the deque A */
void remove_from_front(deque<int> &A) {
    if (!A.empty()) {
        A.pop_front();
    }
}

/* Sorts the deque A in ascending order */
void sort(deque<int> &A) {
    std::sort(A.begin(), A.end());
}

/* Reverses the deque A */
void reverse(deque<int> &A) {
    std::reverse(A.begin(), A.end());
}

/* Returns the size of the deque A */
int size(deque<int> &A) {
    return A.size();
}

/* Returns the element at the front of the deque */
int element_at_front(deque<int> &A) {
    return A.empty() ? -1 : A.front();
}

/* Returns the element at the back of the deque */
int element_at_back(deque<int> &A) {
    return A.empty() ? -1 : A.back();
}
