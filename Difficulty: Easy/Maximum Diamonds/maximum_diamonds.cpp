#include <vector>
#include <queue>
using namespace std;

class Solution {
  public:
    long long maxDiamonds(vector<int>& arr, int k) {
        priority_queue<int> pq(arr.begin(), arr.end());
        long long result = 0;

        for (int i = 0; i < k; i++) {
            if (pq.empty()) break; // no bags left
            
            int maxDiamonds = pq.top();
            pq.pop();

            result += maxDiamonds;
            int reduced = maxDiamonds / 2;

            if (reduced > 0) pq.push(reduced);
        }

        return result;
    }
};
