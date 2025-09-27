class Solution {
  public:
    vector<int> deleteElement(vector<int>& arr, int k) {
        vector<int> st; // acts as a stack

        for (int num : arr) {
            // delete while last element is smaller than current
            // and we still have deletions left
            while (!st.empty() && k > 0 && st.back() < num) {
                st.pop_back();
                k--;
            }
            st.push_back(num);
        }

        // IMPORTANT: do NOT delete from the end if k > 0.
        // The problem expects at most k deletions of elements
        // that are (become) smaller than their next element.
        return st;
    }
};
