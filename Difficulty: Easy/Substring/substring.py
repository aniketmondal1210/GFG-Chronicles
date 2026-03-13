// User function Template for Java
class Solution {
    String substring(String S, int L, int R) {
        // code here
        String new_s = "";
        for(int i = L; i <= R; i++) {
            new_s += S.charAt(i);
        }
        return new_s;
    }
}


class Solution {
    String substring(String S, int L, int R) {
        return S.substring(L, R + 1);
    }
}
