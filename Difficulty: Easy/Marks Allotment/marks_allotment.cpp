// User function Template for C++

class Solution {
  public:
    int marks(int a) {
        try {
            if (a < 0 || a > 100) {
                throw a;   // throw invalid marks
            }
            return a;      // valid marks
        }
        catch (int) {
            return -1;     // invalid marks, return -1
        }
    }
};
