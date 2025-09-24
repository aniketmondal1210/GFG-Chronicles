// User function Template for C++
class Solution {
  public:
    string substring(string &s, int L, int R) {
        // Extract the substring from index L to R (inclusive)
        return s.substr(L, R - L + 1);
    }
};
