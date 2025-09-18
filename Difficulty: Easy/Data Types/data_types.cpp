#include <iostream>
#include <typeinfo>
using namespace std;

int main() {
    int a;          // integer
    float b;        // floating point
    double c;       // double precision floating point
    long long d;    // long long integer

    // variables declaration checking
    if ((typeid(a) == typeid(int)) and (typeid(b) == typeid(float)) and
        (typeid(c) == typeid(double)) and (typeid(d) == typeid(long long)))
        cout << "verified\n";

    return 0;
}
