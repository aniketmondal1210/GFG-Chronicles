#include <unordered_set>
using namespace std;

/* Inserts an element x to the unordered set s */
void insert(unordered_set<int> &s, int x) {
    s.insert(x);
}

/* Erases an element x from the unordered set s */
void erase(unordered_set<int> &s, int x) {
    s.erase(x);
}

/* Returns the size of the unordered set s */
int size(unordered_set<int> &s) {
    return s.size();
}

/* Returns 1 if the element x is present in unordered set s, else returns -1 */
int find(unordered_set<int> &s, int x) {
    return s.find(x) != s.end() ? 1 : -1;
}
