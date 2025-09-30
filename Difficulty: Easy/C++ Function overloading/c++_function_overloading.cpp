#include <iostream>
using namespace std;

const double PI = 3.14159;

// Cube
void volume(int s) {
    cout << s * s * s << endl;
}

// Cylinder
void volume(int r, int h) {
    double vol = PI * r * r * h;
    cout << vol << endl;
}

// Rectangular Box
void volume(int l, int b, int h) {
    cout << l * b * h << endl;
}
