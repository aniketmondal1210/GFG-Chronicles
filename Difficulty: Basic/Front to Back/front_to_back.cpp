// Complete this function. it1 points to vector.begin(), it2 points to vector.end()
void iter(vector<int>::iterator it1, vector<int>::iterator it2) {
    for (auto it = it1; it != it2; ++it) {
        cout << *it << " ";
    }
    cout << endl;
}
