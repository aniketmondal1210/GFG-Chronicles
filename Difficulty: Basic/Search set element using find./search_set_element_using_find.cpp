class Solution {
  public:
    bool sExists(set<int> &s, int x) {
        // Check if x exists in the set s
        return s.find(x) != s.end();
    }
};
