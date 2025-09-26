// User function Template for C++
#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    void speedBreaker(double a, int b) {
        ostringstream oss;
        oss << fixed << setprecision(b) << a;
        cout << oss.str() << '\n';
    }
};
