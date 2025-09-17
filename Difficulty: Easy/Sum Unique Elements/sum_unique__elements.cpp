// User function Template for C++

//Back-end complete function Template for C++

class Solution {
  public:
    int unique_elements(vector<int> &arr) {
        unordered_map<int, int> freq;
        for (int num : arr) {
            freq[num]++;
        }

        int sumUnique = 0;
        for (auto &p : freq) {
            if (p.second == 1) {
                sumUnique += p.first;
            }
        }

        return sumUnique;
    }
};
