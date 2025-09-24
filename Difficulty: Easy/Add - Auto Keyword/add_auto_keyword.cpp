#include <iostream>
using namespace std;

int main() {
    int a;
    float b;
    long c;

    // Take input for a, b, and c
    cin >> a >> b >> c;

    // Declare a variable to hold the sum
    // To avoid data type issues, we use 'double' to store the result.
    double ans = a + b + c;

    // Print the result
    cout << ans << endl;
    return 0;
}
