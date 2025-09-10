#include <vector>
#include <algorithm> // for make_heap
using namespace std;

void heapify(vector<int> &arr) {
    make_heap(arr.begin(), arr.end());
}
