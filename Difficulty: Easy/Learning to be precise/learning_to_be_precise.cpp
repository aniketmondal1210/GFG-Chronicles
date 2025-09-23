#include <iostream>
#include <iomanip>
using namespace std;

void precise(float a, float b) {
    float c = a / b;

    // First: default format
    // Second: fixed with 3 decimal places
    cout << c << " " << fixed << setprecision(3) << c << endl;
}
