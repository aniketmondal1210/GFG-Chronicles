// User function Template for C++

#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

vector<string> login_system(vector<string> &arr) {
    unordered_map<string, int> counts;
    vector<string> result;
    
    for (auto &username : arr) {
        if (counts.find(username) == counts.end()) {
            // New username, no suffix needed
            result.push_back(username);
            counts[username] = 1;  // Start count at 1 for next duplicates
        } else {
            // Username exists, append suffix
            int suffix = counts[username];
            string new_username;
            
            // Find smallest suffix that is not used
            while(true) {
                new_username = username + to_string(suffix);
                if(counts.find(new_username) == counts.end()) {
                    result.push_back(new_username);
                    counts[new_username] = 1;  // Mark new_username as used
                    counts[username]++;         // Increment suffix for original username
                    break;
                }
                suffix++;
            }
        }
    }
    
    return result;
}
