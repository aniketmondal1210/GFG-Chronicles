// User function Template for C++

/*
struct Complex
{
    int real;
    int img;
};
*/

Complex add(Complex c1, Complex c2) {
    Complex result;
    result.real = c1.real + c2.real;
    result.img = c1.img + c2.img;
    return result;
}
