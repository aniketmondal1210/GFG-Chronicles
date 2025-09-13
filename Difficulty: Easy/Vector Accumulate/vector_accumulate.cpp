#include <vector>
#include <numeric>  // for accumulate
using namespace std;

class Solution {
  public:
    int vAccu(vector<int>& arr) {
        return accumulate(arr.begin(), arr.end(), 0);
    }
};
