class Solution {
    public int solution(int n, int m) {
        return comb(n + m, n);
    }
    private int comb(int n, int r) {
        if(r==0||n== r){
            return 1;
        }
        return comb(n - 1, r - 1) + comb(n - 1, r);
    }
}