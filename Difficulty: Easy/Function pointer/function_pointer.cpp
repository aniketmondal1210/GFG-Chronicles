// User function Template for C
int sub(int a, int b) {
    return a - b;
}

int add(int a, int b) {
    return a + b;
}

void compute(int a, int b, int (*func)(int, int)) {
    int result = func(a, b);
    printf("%d\n", result);
}
