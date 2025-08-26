int stringComparsion(string s1, string s2) {
    int i = 0;
    while (i < s1.length() && i < s2.length()) {
        if (s1[i] != s2[i]) {
            return s1[i] > s2[i] ? 1 : -1;
        }
        i++;
    }
    return s1.length() > s2.length() ? 1 : (s1.length() < s2.length() ? -1 : 0);
}
