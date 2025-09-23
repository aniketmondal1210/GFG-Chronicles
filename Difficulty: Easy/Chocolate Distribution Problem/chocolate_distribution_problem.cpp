//Back-end complete function Template for C++
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

int minDiff(vector<int> &arr, int k) {
    if (k == 0 || arr.size() < k) return 0;

    // Step 1: Sort the array
    sort(arr.begin(), arr.end());

    int min_diff = INT_MAX;

    // Step 2: Find the min difference in any k-sized window
    for (int i = 0; i <= arr.size() - k; i++) {
        int current_diff = arr[i + k - 1] - arr[i];
        min_diff = min(min_diff, current_diff);
    }

    return min_diff;
}
