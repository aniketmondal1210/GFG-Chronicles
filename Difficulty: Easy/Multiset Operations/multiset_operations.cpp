#include <bits/stdc++.h>
using namespace std;

multiset<int> multisetInsert(int arr[], int n) {
    multiset<int> s;
    for (int i = 0; i < n; i++) {
        s.insert(arr[i]);
    }
    return s;
}

void multisetDisplay(multiset<int> s) {
    for (int elem : s) {
        cout << elem << " ";
    }
    cout << endl;
}

void multisetErase(multiset<int>& s, int x) {
    if (s.count(x) > 0) {
        s.erase(x);  // erase all occurrences of x
        cout << "erased " << x << endl;
    } else {
        cout << "not found" << endl;
    }
}
