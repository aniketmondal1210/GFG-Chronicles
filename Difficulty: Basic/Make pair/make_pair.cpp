// User function Template for C++
#include <iostream>
#include <utility>  // for std::pair, std::make_pair
using namespace std;

/*
X, Y: two numbers whose pair is to be returned
*/
pair<int, int> makePair(int x, int y) {
    return make_pair(x, y);
    // Or simply: return {x, y};
}
