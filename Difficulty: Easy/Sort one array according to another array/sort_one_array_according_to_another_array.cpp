// User function Template for C++
#include <bits/stdc++.h>
using namespace std;

void sortArray(int a[], char b[], int n) {
    // store pairs (a[i], b[i])
    vector<pair<int,char>> v;
    for (int i = 0; i < n; i++) {
        v.push_back({a[i], b[i]});
    }

    // sort by integer value
    sort(v.begin(), v.end(), [](pair<int,char> &p1, pair<int,char> &p2) {
        return p1.first < p2.first;   // ascending order of a[]
    });

    // copy sorted chars back to b[]
    for (int i = 0; i < n; i++) {
        b[i] = v[i].second;
    }
}
