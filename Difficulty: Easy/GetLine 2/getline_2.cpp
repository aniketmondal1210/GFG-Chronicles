// User function Template for C++

// Function to take input of string using getline
#include <iostream>
#include <string>
using namespace std;

void getLine() {
    string s;
    // Use getline with delimiter '@'
    getline(cin, s, '@');
    cout << s << endl;
}
