// User function Template for C++

//Back-end complete function Template for C++

#include <vector>
#include <queue>
#include <unordered_map>
using namespace std;

class Solution {
  public:
    int maximum_sum(int k, vector<int> &arr) {
        unordered_map<int, int> freq;
        for (int num : arr) {
            freq[num]++;
        }

        // Max heap: pair(freq, val)
        priority_queue<pair<int,int>> pq;
        for (auto &p : freq) {
            pq.push({p.second, p.first});
        }

        int sum = 0;
        while (k > 0 && !pq.empty()) {
            auto [f, val] = pq.top();
            pq.pop();

            sum += val;
            f--;
            k--;

            if (f > 0) {
                pq.push({f, val});
            }
        }

        return sum;
    }
};
