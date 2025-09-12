#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    string common_String(string s1, string s2) {
        // Frequency arrays for uppercase and lowercase letters
        // We'll mark which characters are present in each string
        bool presentS1[52] = {false};
        bool presentS2[52] = {false};
        
        // Helper lambda to get index for 'A'-'Z' and 'a'-'z'
        auto getIndex = [](char c) -> int {
            if (c >= 'A' && c <= 'Z') return c - 'A';       // 0 to 25
            else return 26 + (c - 'a');                     // 26 to 51
        };
        
        // Mark presence of characters in s1
        for (char c : s1) {
            presentS1[getIndex(c)] = true;
        }
        
        // Mark presence of characters in s2
        for (char c : s2) {
            presentS2[getIndex(c)] = true;
        }
        
        string result;
        
        // First, add uppercase letters common in both
        for (char c = 'A'; c <= 'Z'; c++) {
            int idx = getIndex(c);
            if (presentS1[idx] && presentS2[idx]) {
                result.push_back(c);
            }
        }
        
        // Then, add lowercase letters common in both
        for (char c = 'a'; c <= 'z'; c++) {
            int idx = getIndex(c);
            if (presentS1[idx] && presentS2[idx]) {
                result.push_back(c);
            }
        }
        
        if (result.empty()) return "nil";
        return result;
    }
};
