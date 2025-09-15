#include <iostream>
#include <vector>
#include <map>
using namespace std;

// Insert elements of arr into multimap (key = element, value = index)
multimap<int, int> multimapInsert(vector<int>& arr) {
    multimap<int, int> mp;
    for (int i = 0; i < (int)arr.size(); i++) {
        mp.insert({arr[i], i});
    }
    return mp;
}

// Print all key-value pairs of multimap, each on new line
void multimapDisplay(const multimap<int, int>& mp) {
    for (const auto& p : mp) {
        cout << p.first << " " << p.second << "\n";
    }
}

// Erase all entries with key = x, print status
void multimapErase(multimap<int, int>& mp, int x) {
    auto count = mp.count(x);
    if (count > 0) {
        mp.erase(x);
        cout << "erased " << x << "\n";
    } else {
        cout << "not found\n";
    }
}
