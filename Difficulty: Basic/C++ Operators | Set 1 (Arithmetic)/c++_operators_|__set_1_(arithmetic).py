class Solution {
  public:
    vector<int> cppOperators(int A, int B) {
        // code here
        vector<int> result;
        // Addition
        result.push_back(A + B);
        
        // Multiplication
        result.push_back(A * B);
        
        // Subtraction: larger - smaller
        int sub = (A > B) ? A - B : B - A;
        result.push_back(sub);
        
        // Division: larger / smaller
        int div = (A > B) ? A / B : B / A;
        result.push_back(div);
        
        return result;
    }
};
