#include <vector>
#include <algorithm> // for std::fill
using namespace std;

class Solution {
  public:
    vector<int> vFill(vector<int>& arr) {
        // Fill the entire vector with 0
        fill(arr.begin(), arr.end(), 0);
        return arr;
    }
};
