class Solution {
    public static int arraySum(int[] arr) {
        // code here
        int summ = 0;
        for(int i = 0;i < arr.length;i++){
            summ += arr[i];
        }
        return summ;
    }
}
