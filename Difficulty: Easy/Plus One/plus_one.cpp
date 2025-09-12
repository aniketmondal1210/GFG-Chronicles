// User function Template for C++
class Solution {
  public:
    vector<int> increment(vector<int> arr, int N) {
        int carry = 1;  // We want to add 1
        for (int i = N - 1; i >= 0; i--) {
            int sum = arr[i] + carry;
            arr[i] = sum % 10;
            carry = sum / 10;
            
            if (carry == 0) break; // No further carry, stop early
        }
        
        // If carry is still 1 after processing all digits, insert it at front
        if (carry == 1) {
            arr.insert(arr.begin(), 1);
        }
        
        return arr;
    }
};
