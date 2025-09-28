#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    void follPatt(string s) {
        int n = s.length();
        int i = 0;

        while (i < n) {
            // must start with x
            if (s[i] != 'x') {
                cout << 0 << endl;
                return;
            }

            // count x's
            int countX = 0;
            while (i < n && s[i] == 'x') {
                countX++;
                i++;
            }

            // count y's
            int countY = 0;
            while (i < n && s[i] == 'y') {
                countY++;
                i++;
            }

            // check if counts match
            if (countX != countY) {
                cout << 0 << endl;
                return;
            }
        }

        cout << 1 << endl;
    }
};
