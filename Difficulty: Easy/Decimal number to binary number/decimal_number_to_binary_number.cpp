// User function Template for C++

#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    void toBinary(string N) {
        // convert string to integer
        long long num = stoll(N);

        // handle 0 separately
        if (num == 0) {
            cout << 0;
            return;
        }

        string binary = "";
        while (num > 0) {
            binary += (num % 2) + '0'; // store remainder
            num /= 2;
        }

        reverse(binary.begin(), binary.end()); // reverse to correct order
        cout << binary;
    }
};
