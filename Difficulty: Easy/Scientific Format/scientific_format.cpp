#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double a;
    cin >> a;

    // Set output to scientific notation with 4 digits after the decimal
    cout << scientific << setprecision(4) << a << endl;

    return 0;
}
