#include <iostream>
using namespace std;

int main() {
    int a;
    float b;
    double c;
    long long d;

    cin >> a >> b >> c >> d;

    // print sizes on the same line separated by spaces
    cout << sizeof(a) << " " << sizeof(b) << " " 
         << sizeof(c) << " " << sizeof(d) << endl;

    return 0;
}
