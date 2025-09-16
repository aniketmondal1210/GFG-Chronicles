#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
  public:
    bool isArr2PermutationOfArr1(vector<int>& arr1, vector<int>& arr2) {
        if (arr1.size() != arr2.size()) return false;

        unordered_map<int, int> freq;
        for (int num : arr1) {
            freq[num]++;
        }

        for (int num : arr2) {
            if (freq.find(num) == freq.end() || freq[num] == 0)
                return false;
            freq[num]--;
        }

        return true;
    }
};
