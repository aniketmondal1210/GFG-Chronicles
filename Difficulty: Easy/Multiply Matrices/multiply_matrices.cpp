void multiply(int A[][100], int B[][100], int C[][100], int N) {
    int i, j, k;

    // Initialize all elements of C to 0
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            C[i][j] = 0;
        }
    }

    // Multiply A and B, store in C
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            for (k = 0; k < N; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}
