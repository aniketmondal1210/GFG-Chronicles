// User function Template for C++

/*
arr: insert the given array elements to vector
n: size of array
*/
#include <vector>
using namespace std;

vector<int> fillVector(int arr[], int n) {
    vector<int> v;
    for (int i = 0; i < n; ++i) {
        v.push_back(arr[i]);
    }
    return v;
}
