#include <iostream>
#include <vector>
using namespace std;

void ShrinkMe(vector<int> myvector, int newsize) {
    // Resize vector to newsize (removes elements if newsize < current size)
    if (newsize < (int)myvector.size()) {
        myvector.resize(newsize);
    }
    
    // Print capacity before shrink_to_fit
    cout << myvector.capacity() << endl;

    // Shrink capacity to fit current size
    myvector.shrink_to_fit();

    // Print capacity after shrink_to_fit
    cout << myvector.capacity();
}
