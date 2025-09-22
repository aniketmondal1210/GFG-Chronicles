// User function Template for C++
class Solution {
  public:
    int binary_to_decimal(int n) {
        int decimal = 0;
        int base = 1;  // 2^0

        while (n > 0) {
            int last_digit = n % 10;
            decimal += last_digit * base;
            base *= 2;
            n /= 10;
        }

        return decimal;
    }
};
