// User function Template for C++
#include <iostream>
#include <vector>
using namespace std;

void eraseAt(vector<int> &arr, int pos) {
    if (pos >= 0 && pos < (int)arr.size()) {
        arr.erase(arr.begin() + pos);
    }
}

void eraseInRange(vector<int> &arr, int start, int end) {
    if (start >= 0 && end <= (int)arr.size() && start < end) {
        arr.erase(arr.begin() + start, arr.begin() + end);
    }
}

void clearAll(vector<int> &arr) {
    arr.clear();
}

// Helper function to print vector elements
void printVector(const vector<int>& arr) {
    for (int val : arr) {
        cout << val << " ";
    }
    cout << "\n";
}
