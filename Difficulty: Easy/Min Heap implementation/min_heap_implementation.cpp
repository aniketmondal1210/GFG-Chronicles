/* Function to implement push operation in priority_queue
 * pq : priority_queue
 * x : element to be pushed
 */
#include <queue>
using namespace std;

// Push element x into min-heap pq
void push(priority_queue<int, vector<int>, greater<int>> &pq, int x) {
    pq.push(x);
}

// Pop the top (smallest) element from min-heap pq
void pop(priority_queue<int, vector<int>, greater<int>> &pq) {
    if (!pq.empty())
        pq.pop();
    else
        return;
}

// Return the top (smallest) element from min-heap pq
int top(priority_queue<int, vector<int>, greater<int>> &pq) {
    if (!pq.empty())
        return pq.top();
    else
        return -1;  // or other error value indicating empty queue
}
