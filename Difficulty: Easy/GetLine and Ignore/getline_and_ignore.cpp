//Back-end complete function Template for C++

// Function to take input of string using getline
#include <iostream>
#include <string>
using namespace std;

void getLineAndIgnore() {
    string a, d;
    int b;

    // Read first string line
    getline(cin, a);

    // Read integer
    cin >> b;

    // Clear the newline left by cin >> b before getline
    cin.ignore();

    // Read second string line
    getline(cin, d);

    cout << a << endl;
    cout << b << endl;
    cout << d << endl;
}
