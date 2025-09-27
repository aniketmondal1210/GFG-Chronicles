/*struct area
{
    int sd;
    int len, wid;
}*/
void find_area(int side, int le, int wd) {
    long long square_area = 1LL * side * side;
    long long rect_area   = 1LL * le * wd;

    // Print in required format
    cout << square_area << " " << rect_area;
}
