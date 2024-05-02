import java.util.*;

class Solution {
    public int solution(int n, int[] money) {
        // 1원으로 만들수 있는 경우 저장
        // 2원으로 만들수 있는 경우
            // 1원 으로 만들수 있는 경우에서 2를 뺀 경우의 수를 더하면 됨
        int[] dp = new int[n+1];
        dp[0] = 1;
        
        for (int m : money){
            for (int i = 1; i < n + 1; i++){
                if (i - m >= 0){
                    dp[i] += dp[i - m];
                }
            }
        }
        return dp[n];
    }
}