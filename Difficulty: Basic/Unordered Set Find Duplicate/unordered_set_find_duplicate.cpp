// User function Template for C++
#include <vector>
#include <set>
using namespace std;

vector<int> DuplicateMe(vector<int>& arr) {
    set<int> seen;
    set<int> duplicates;

    for (int num : arr) {
        if (seen.find(num) != seen.end()) {
            // Already seen before → duplicate
            duplicates.insert(num);
        } else {
            seen.insert(num);
        }
    }

    // Convert duplicates set to vector
    return vector<int>(duplicates.begin(), duplicates.end());
}
