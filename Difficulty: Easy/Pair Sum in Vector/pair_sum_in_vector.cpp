/*the function contains vector of pairs*/
// Complete this function to print the sum
void sum(vector<pair<int, int>> v) {
    long long total = 0;

    for (auto &p : v) {
        total += static_cast<long long>(p.second); // only add second element
    }

    cout << total << endl;
}
