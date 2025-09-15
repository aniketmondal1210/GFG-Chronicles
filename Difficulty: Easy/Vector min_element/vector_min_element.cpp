// User function Template for C++

// Complete this function
#include <algorithm>

int vMin(vector<int>& arr) {
    if (arr.empty()) return -1; // handle empty vector case
    return *min_element(arr.begin(), arr.end());
}
