// User function Template for C

/* Function to take input for 2D array elements
 * N : size of matrix
 */
#include <stdio.h>

void twoDimensional(int N, int A[][N]) {
    for (int i = 0; i < N; i++) {           // Row-wise
        for (int j = 0; j < N; j++) {       // Column-wise
            printf("%d ", A[i][j]);         // Print element
        }
        printf("\n");                       // Newline after each row
    }
}
