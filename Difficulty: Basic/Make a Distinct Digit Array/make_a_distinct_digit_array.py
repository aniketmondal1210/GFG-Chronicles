class Solution {
  public:
    vector<int> distDigit(vector<int>& arr) {
        // Code here
        bool present[10] = {false};
        for (int num : arr) {
            while (num > 0) {
                present[num % 10] = true;
                num /= 10;
            }
        }
        vector<int> result;
        for (int d = 0; d <= 9; ++d) {
            if (present[d]) {
                result.push_back(d);
            }
        }
        return result;
    }
};
