// User function Template for C++
#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    void isInRange(int n) {
        static const string words[] = {
            "", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine", "ten"
        };

        if (n >= 1 && n <= 10) cout << words[n] << '\n';
        else cout << "not in range\n";
    }
};
