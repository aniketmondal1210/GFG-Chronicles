#include <string>
#include <cctype>
using namespace std;

class Solution {
  public:
    int BasicDataType(string s) {
        int n = s.size();
        if (n == 0) return sizeof(char); // defensive

        // Single-character case:
        if (n == 1) {
            if (isdigit(static_cast<unsigned char>(s[0]))) return sizeof(int); // "7" -> int
            return sizeof(char); // "a", "@", "+" -> char
        }

        // Handle optional sign
        int start = 0;
        if (s[0] == '+' || s[0] == '-') start = 1;
        if (start == n) return sizeof(char); // string was just "+" or "-"

        bool hasDot = false;
        int dotPos = -1;

        for (int i = start; i < n; ++i) {
            char c = s[i];
            if (c == '.') {
                if (hasDot) return sizeof(char); // malformed: multiple dots
                hasDot = true;
                dotPos = i;
            } else if (!isdigit(static_cast<unsigned char>(c))) {
                // invalid character (not digit and not dot)
                return sizeof(char);
            }
        }

        if (!hasDot) {
            // all remaining chars are digits -> integer
            return sizeof(int);
        }

        // has dot: number of digits after dot
        int fractional = n - dotPos - 1; // can be 0 for "5."
        // NEW RULE: fractional <= 5 -> float (4). fractional >= 6 -> double (8).
        return (fractional <= 5) ? sizeof(float) : sizeof(double);
    }
};
