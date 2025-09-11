#include <unordered_map>
using namespace std;

/* Inserts an entry with key x and value y in map */
void add_value(unordered_map<int, int> &m, int x, int y) {
    m[x] = y;  // Insert or update the key with value y
}

/* Returns the value with key x from the map */
int find_value(unordered_map<int, int> &m, int x) {
    if (m.find(x) != m.end()) {
        return m[x];  // Key found, return its value
    } else {
        return -1;    // Key not found, return -1
    }
}

/* Returns the size of the map */
int getSize(unordered_map<int, int> &m) {
    return m.size();
}

/* Removes the entry with key x from the map */
void removeKey(unordered_map<int, int> &m, int x) {
    m.erase(x);
}
