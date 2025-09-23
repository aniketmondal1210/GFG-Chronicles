// Function to find size of different data types
void dataTypes(int a, float b, double c, long long l, string d) {
    // Step 1: b / c -> cast c to float for float / float = float (4 bytes)
    cout << sizeof(b / (float)c) << " ";  // float

    // Step 2: b / a -> cast b to double for double / int = double (8 bytes)
    cout << sizeof((double)b / a) << " ";  // double

    // Step 3: c / a -> cast c to float for float / int = float (4 bytes)
    cout << sizeof((float)c / a) << " ";  // float

    // Step 4: (c / a) + l -> cast c to double (default), so double + long long = double (8 bytes)
    cout << sizeof(c / a + l) << "\n";

    // Step 5: string size and character size
    cout << sizeof(d) << " " << sizeof(d[3]) << "\n";
}
