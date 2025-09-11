#include <stack>
using namespace std;

/* the function pushes an element x into the stack s */
void push(stack<int> &s, int x) {
    s.push(x);
}

/* pops the top element of the stack and returns it */
int pop(stack<int> &s) {
    if (s.empty()) {
        return -1;  // return -1 if stack is empty
    }
    int topElement = s.top();
    s.pop();
    return topElement;
}

/* returns the size of the stack */
int getSize(stack<int> &s) {
    return s.size();
}

/* returns the top element of the stack */
int getTop(stack<int> &s) {
    if (s.empty()) {
        return -1;  // return -1 if stack is empty
    }
    return s.top();
}
