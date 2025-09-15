/*Function to sort students with respect to their marks
 * v : vector input with student name and their marks
 * N : size of vector
 * Your need to implement comparator to sort on the basis of marks.
 */
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<pair<string, int>> sortMarks(vector<pair<string, int>> v, int N) {
    sort(v.begin(), v.end(), [](const pair<string,int> &a, const pair<string,int> &b) {
        if (a.second != b.second)
            return a.second > b.second;  // descending order by marks
        return a.first < b.first;        // gascending order by name
    });
    return v;
}
