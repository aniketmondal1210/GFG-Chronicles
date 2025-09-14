class Solution {
  public:
    vector<int> maxOfSubarrays(vector<int>& arr, int k) {
        deque<int> dq;
        vector<int> result;
        int n = arr.size();

        for (int i = 0; i < n; ++i) {
            // Remove elements out of the current window
            if (!dq.empty() && dq.front() <= i - k) {
                dq.pop_front();
            }

            // Remove all smaller elements from the back
            while (!dq.empty() && arr[dq.back()] < arr[i]) {
                dq.pop_back();
            }

            // Add current element at the back
            dq.push_back(i);

            // Starting from i = k - 1, we start recording results
            if (i >= k - 1) {
                result.push_back(arr[dq.front()]);
            }
        }

        return result;
    }
};
