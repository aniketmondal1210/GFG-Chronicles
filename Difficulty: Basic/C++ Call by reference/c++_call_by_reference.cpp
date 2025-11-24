void reverse_dig(int &a, int &b) {
    int rev_a = 0, rev_b = 0;
    int temp_a = a, temp_b = b;
    
    // Reverse a
    while(temp_a > 0) {
        rev_a = rev_a * 10 + temp_a % 10;
        temp_a /= 10;
    }
    
    // Reverse b
    while(temp_b > 0) {
        rev_b = rev_b * 10 + temp_b % 10;
        temp_b /= 10;
    }
    
    a = rev_a;
    b = rev_b;
}

void swap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}
