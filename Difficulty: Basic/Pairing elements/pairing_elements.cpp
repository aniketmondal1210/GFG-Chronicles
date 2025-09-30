// User function Template for C++

/*
array_of_Pairs(arr, n, res, m): function has arr[]: contains elements of given array
n: sze of array
res: stores the pair of integers
m: size of res.
*/
#include <utility>
using namespace std;

void arrayOfPairs(int arr[], int n, pair<int, int> res[], int m) {
    int k = 0; // index for res[]
    for (int i = 0; i < (n + 1) / 2; i++) {
        if (k < m) {
            res[k] = make_pair(arr[i], arr[n - 1 - i]);
            k++;
        }
    }
}
