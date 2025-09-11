#include <vector>
#include <algorithm>
using namespace std;

int vMax(vector<int>& arr) {
    if (arr.empty()) {
        // If empty, you can decide what to return; here, returning INT_MIN as no max
        return INT_MIN;
    }
    return *max_element(arr.begin(), arr.end());
}
