#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    string isPrime(int n) {
        if (n <= 1) return "No";   // 0 and 1 are not prime
        if (n == 2) return "Yes";  // 2 is prime
        if (n % 2 == 0) return "No"; // even numbers > 2 are not prime

        for (int i = 3; i <= sqrt(n); i += 2) { // check only odd divisors
            if (n % i == 0) {
                return "No";
            }
        }
        return "Yes";
    }
};
