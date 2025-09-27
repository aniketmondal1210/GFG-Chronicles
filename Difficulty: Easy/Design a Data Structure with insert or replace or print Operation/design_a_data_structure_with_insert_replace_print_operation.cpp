// User function Template for C++

list<int> l;

// inserts an integer at the end of the data structure.
void insert(int x) {
    l.push_back(x);
}

// prints the elements of the data structure
// the new line is given by the driver's code
void print() {
    for (auto it : l) {
        cout << it << " ";
    }
    cout << endl;
}

// replaces the first occurrence of x with sequence
void replace(int x, vector<int> sequence) {
    for (auto it = l.begin(); it != l.end(); ++it) {
        if (*it == x) {
            // erase the element x
            it = l.erase(it);
            // insert the sequence at that position
            l.insert(it, sequence.begin(), sequence.end());
            break;  // only first occurrence replaced
        }
    }
}
