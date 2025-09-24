#include <iostream>
using namespace std;

int main() {
    int a, b;
    
    // Reading the input values for a and b
    cin >> a >> b;

    // Compare a and b
    if (a > b) {
        cout << 1;  // a is greater than b
    } else {
        cout << 0;  // a is not greater than b
    }

    return 0;
}
