#include <queue>
using namespace std;

/* Inserts an element x at the back of the queue q */
void push(queue<int> &q, int x) {
    q.push(x);
}

/* Pops out the front element from the queue q and returns it */
int pop(queue<int> &q) {
    if (q.empty()) {
        return -1; // or throw an exception, depending on the problem statement
    }
    int front = q.front();
    q.pop();
    return front;
}

/* Returns the size of the queue q */
int getSize(queue<int> &q) {
    return q.size();
}

/* Returns the last element of the queue */
int getBack(queue<int> &q) {
    if (q.empty()) {
        return -1; // or throw an exception
    }
    return q.back();
}

/* Returns the first element of the queue */
int getFront(queue<int> &q) {
    if (q.empty()) {
        return -1; // or throw an exception
    }
    return q.front();
}
