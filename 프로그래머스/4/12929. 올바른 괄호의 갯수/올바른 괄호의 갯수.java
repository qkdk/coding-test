// ()를 세우고 안에 넣고 밖에 넣고 
import java.util.*;

class Solution {
    public int solution(int n) {
        
        int[] dp = new int[n + 1];
        dp[0] = 1;
            
        for (int i = 1; i < n + 1; i++){
            int k = i - 1;
            for (int j = 0; j <= k ; j++){
                dp[i] += (dp[k - j] * dp[j]);
                // System.out.println(k + " " + j);
            }
        }
        
        return dp[n];
    }
}