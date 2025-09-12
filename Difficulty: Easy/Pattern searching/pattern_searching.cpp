// User function Template for C++

/*
str: string in which pattern we have to find pattern.
pat: pattern needs to searched.
*/

bool searchPattern(string &txt, string &pat) {
    return txt.find(pat) != string::npos;
}
