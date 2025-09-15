// User function Template for C++

//Back-end complete function Template for C++
class Solution {
  public:
    vector<int> list_less_than_k(vector<int> &arr, int k) {
        vector<int> result;
        for (int num : arr) {
            if (num < k) {
                result.push_back(num);
            }
        }
        return result;
    }
};
