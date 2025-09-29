class Solution {
  public:
    bool binarySearch(vector<int>& arr, int k) {
        int low = 0, high = arr.size() - 1;

        while (low <= high) {
            int mid = low + (high - low) / 2;  // avoid overflow

            if (arr[mid] == k) return true;      // element found
            else if (arr[mid] < k) low = mid + 1; // search right half
            else high = mid - 1;                  // search left half
        }

        return false; // element not found
    }
};
