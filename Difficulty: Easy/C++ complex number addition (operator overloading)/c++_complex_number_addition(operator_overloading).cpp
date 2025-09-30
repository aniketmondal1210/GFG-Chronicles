#include <iostream>
using namespace std;

class complex {
    int x, y; // real and imaginary

  public:
    complex() {}

    complex(int real, int imag) {
        x = real;
        y = imag;
    }

    complex operator+(const complex &c) {
        return complex(x + c.x, y + c.y);
    }

    void display() {
        cout << x << " + " << y << "i" << endl;
    }
};
