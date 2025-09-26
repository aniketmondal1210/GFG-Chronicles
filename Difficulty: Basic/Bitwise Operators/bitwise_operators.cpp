// Function to perform bitwise manipulations
// a, b and c are input integers
void bitWiseOperation(int a, int b, int c) {
    int d = a ^ a;          // always 0
    int e = c ^ b;          // XOR of c and b
    int f = a & b;          // AND of a and b
    int g = c | (a ^ a);    // OR with (a^a = 0), so just c
    int h = ~e;             // bitwise NOT of e

    cout << d << endl;
    cout << e << endl;
    cout << f << endl;
    cout << g << endl;
    cout << h << endl;
}
