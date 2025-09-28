/*Function to count number of characters
 * to make s1 and s2 equal
 * s1 : first string
 * s2 : second string
 */
#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    int countChars(string s1, string s2) {
        vector<int> freq1(26, 0), freq2(26, 0);

        // count frequency of chars in s1
        for (char c : s1) {
            freq1[c - 'a']++;
        }

        // count frequency of chars in s2
        for (char c : s2) {
            freq2[c - 'a']++;
        }

        int count = 0;
        // find absolute difference for each character
        for (int i = 0; i < 26; i++) {
            count += abs(freq1[i] - freq2[i]);
        }

        return count;
    }
};
