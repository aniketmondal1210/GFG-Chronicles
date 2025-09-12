#include <algorithm>  // for sort and reverse

vector<int> sortVector(vector<int> v) {
    std::sort(v.begin(), v.end());
    return v;
}

vector<int> reverseVector(vector<int> v) {
    std::reverse(v.begin(), v.end());
    return v;
}
