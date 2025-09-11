#include <forward_list>
using namespace std;

forward_list<int> eraseMe(forward_list<int> fwdlist) {
    // Check if the list has at least two elements
    auto it = fwdlist.begin();
    if (it != fwdlist.end()) {
        auto next_it = next(it);
        if (next_it != fwdlist.end()) {
            // Erase the element after the first element (i.e., second element)
            fwdlist.erase_after(it);
        }
    }
    return fwdlist;
}
