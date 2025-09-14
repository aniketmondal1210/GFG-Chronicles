// User function Template for C++
class Solution {
  public:
    vector<int> remove_special_consecutive(vector<int>& arr, int x, int y) {
        vector<int> result;
        
        for (int i = 0; i < arr.size(); ++i) {
            // If current element is special
            if ((arr[i] == x || arr[i] == y)) {
                // And it's the same as the last element in result, skip
                if (!result.empty() && result.back() == arr[i]) {
                    continue;
                }
            }
            // Add element to result
            result.push_back(arr[i]);
        }
        
        return result;
    }
};
