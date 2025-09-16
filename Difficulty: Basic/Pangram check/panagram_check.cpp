// User function Template for C++
#include <string>
#include <vector>
using namespace std;

bool checkPangram(string &s) {
    vector<bool> seen(26, false);
    for (char c : s) {
        // Convert to lowercase if uppercase
        if (c >= 'A' && c <= 'Z') {
            c = c - 'A' + 'a';
        }
        if (c >= 'a' && c <= 'z') {
            seen[c - 'a'] = true;
        }
    }

    // Check if all letters are present
    for (bool present : seen) {
        if (!present) return false;
    }
    return true;
}
