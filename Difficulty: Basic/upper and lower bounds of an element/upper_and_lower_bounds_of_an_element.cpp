// User function Template for C++
#include <vector>
using namespace std;

int lowBound(vector<int>& arr, int k) {
    int left = 0, right = (int)arr.size() - 1;
    int ans = (int)arr.size();
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] >= k) {
            ans = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    // Return value at the lower bound index or -1 if none
    return (ans == arr.size()) ? -1 : arr[ans];
}

int upBound(vector<int>& arr, int k) {
    int left = 0, right = (int)arr.size() - 1;
    int ans = (int)arr.size();
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] > k) {
            ans = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    // Return value at the upper bound index or -1 if none
    return (ans == arr.size()) ? -1 : arr[ans];
}
