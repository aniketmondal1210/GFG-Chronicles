double posAverage(int arr[], int size) {
    double sum = 0;
    int count = 0;

    for (int i = 0; i < size; i++) {
        if (arr[i] >= 0) { // include zero
            sum += arr[i];
            count++;
        }
    }

    if (count == 0) return 0.0; // avoid division by zero

    return sum / count;
}
