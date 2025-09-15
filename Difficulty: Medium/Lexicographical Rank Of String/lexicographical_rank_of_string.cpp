// User function Template for C++

// Complete the function
#include <algorithm>

int RankMe(string &s) {
    string t = s;        // Copy of original string
    sort(t.begin(), t.end());  // Start from the smallest lex permutation

    int rank = 1;
    // Generate permutations until we reach s
    do {
        if (t == s) {
            return rank;
        }
        rank++;
    } while (next_permutation(t.begin(), t.end()));

    return rank;  // If s is not found (should not happen if s is a permutation)
}
