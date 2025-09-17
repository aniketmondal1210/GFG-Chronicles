// User function Template for C++

#include <deque>
#include <vector>
using namespace std;

class Solution {
  public:
    // Function to insert all elements of the array in deque.
    deque<int> insertInDq(vector<int>& arr) {
        deque<int> dq;
        for (int num : arr) {
            dq.push_back(num);  // Insert at the back of the deque
        }
        return dq;
    }
};
