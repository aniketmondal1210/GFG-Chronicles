#include <vector>
#include <algorithm> // for std::find
using namespace std;

class Solution {
  public:
    bool vExists(vector<int> v, int x) {
        // std::find returns an iterator to the element if found, else v.end()
        return (find(v.begin(), v.end(), x) != v.end());
    }
};
