//Back-end complete function Template for C++

// Function to merge two sorted arrays in
// constant space
#include <vector>
#include <cmath>
using namespace std;

void mergeArrays(vector<int> &a, vector<int> &b) {
    int n = a.size();
    int m = b.size();
    int gap = (n + m + 1) / 2;  // initial gap

    while (gap > 0) {
        int i = 0;
        int j = gap;

        while (j < n + m) {
            // i-th element
            int val_i;
            if (i < n) val_i = a[i];
            else val_i = b[i - n];

            // j-th element
            int val_j;
            if (j < n) val_j = a[j];
            else val_j = b[j - n];

            if (val_i > val_j) {
                // Swap
                if (i < n && j < n) {
                    swap(a[i], a[j]);
                } else if (i < n && j >= n) {
                    swap(a[i], b[j - n]);
                } else {
                    swap(b[i - n], b[j - n]);
                }
            }

            i++;
            j++;
        }

        if (gap == 1)
            gap = 0;
        else
            gap = (gap + 1) / 2;
    }
}
