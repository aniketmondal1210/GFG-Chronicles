#include <vector>
#include <forward_list>
using namespace std;

forward_list<int> insertIntoFL(vector<int>& arr) {
    forward_list<int> fl;
    for (int x : arr) {
        fl.push_front(x);
    }
    return fl;
}
