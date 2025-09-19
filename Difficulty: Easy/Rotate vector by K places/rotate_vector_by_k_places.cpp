#include <vector>
#include <algorithm>
using namespace std;

class Solution {
  public:
    vector<int> leftRotate(vector<int> &arr, int k) {
        int n = arr.size();
        k = k % n;  // Handle if k > n
        rotate(arr.begin(), arr.begin() + k, arr.end());
        return arr;
    }
};
