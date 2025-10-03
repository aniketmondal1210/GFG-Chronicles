#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    // Function to return the name of candidate that received maximum votes.
    vector<string> winner(vector<string> &arr) {
        unordered_map<string, int> votes;
        
        // Count votes
        for (auto &name : arr) {
            votes[name]++;
        }
        
        string winnerName;
        int maxVotes = 0;
        
        for (auto &entry : votes) {
            string candidate = entry.first;
            int count = entry.second;
            
            if (count > maxVotes) {
                maxVotes = count;
                winnerName = candidate;
            } else if (count == maxVotes && candidate < winnerName) {
                // Tie → pick lexicographically smaller
                winnerName = candidate;
            }
        }
        
        return {winnerName, to_string(maxVotes)};
    }
};
