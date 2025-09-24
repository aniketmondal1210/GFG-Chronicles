// User function Template for C++
int posAverage(int arr[], int size) {
    int sum = 0;
    int count = 0;

    // Iterate through the array to find non-negative integers
    for (int i = 0; i < size; i++) {
        if (arr[i] >= 0) {  // Check if the number is non-negative
            sum += arr[i];   // Add to sum
            count++;          // Increment the count of non-negative numbers
        }
    }

    // If there are non-negative numbers, return the floor of the average
    if (count > 0) {
        return sum / count;  // Integer division gives the floor value automatically
    } else {
        return 0;  // If no non-negative numbers, return 0
    }
}
