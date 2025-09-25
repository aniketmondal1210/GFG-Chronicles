// User function Template for C++
#include <iostream>
using namespace std;

void utility() {
    // declare the variable count here
    static int count = 0;  // initialized only once

    // increases the value of count by 1
    count++;

    // print count
    cout << count;
}
