// User function Template for C++
#include <string>
using namespace std;

string lexi_string(string &s) {
    int n = s.size();
    string ss = s + s;  // concatenate string to itself

    int i = 0, j = 1, k = 0;
    while (i < n && j < n && k < n) {
        if (ss[i + k] == ss[j + k]) {
            k++;
        } else if (ss[i + k] > ss[j + k]) {
            i = i + k + 1;
            if (i <= j) i = j + 1;
            k = 0;
        } else {
            j = j + k + 1;
            if (j <= i) j = i + 1;
            k = 0;
        }
    }

    int start = min(i, j);
    return ss.substr(start, n);
}
