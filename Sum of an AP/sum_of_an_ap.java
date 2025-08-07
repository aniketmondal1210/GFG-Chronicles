// User function Template for Java
class Solution {
    public int sum_of_ap(int n, int a, int d) {
        // Code here
        int sum = 0;
        for(int i = 1;i<=n;i++){
            sum += (a + (i-1)*d);
        }
        return sum;
    }
}
