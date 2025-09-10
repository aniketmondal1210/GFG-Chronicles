#include <iostream>
#include <vector>
#include <map>
using namespace std;

map<int, int> mapInsert(vector<int>& arr) {
    map<int, int> mp;
    // Insert arr[i] as key and i as value
    for (int i = 0; i < (int)arr.size(); i++) {
        mp[arr[i]] = i;
    }
    return mp;
}

void mapDisplay(map<int, int>& mp) {
    // Print every key and value pair in a new line
    for (auto& [key, value] : mp) {
        cout << key << " " << value << endl;
    }
}

void mapErase(map<int, int>& mp, int x) {
    // Write the if and else condition to erase x from map
    if (mp.find(x) != mp.end()) {
        mp.erase(x);
        cout << "erased " << x << endl;
    } else {
        cout << "not found" << endl;
    }
}
