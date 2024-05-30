import java.util.*;

class Solution {
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        int d = 0;
        int p = 0;
        
        long answer = 0;
        
        for (int i = deliveries.length - 1; i > -1; i--){
            d += deliveries[i];
            p += pickups[i];
            
            while(d > 0 || p > 0){
                d -= cap;
                p -= cap;
                
                answer += (i + 1) * 2;
            }
        }
        return answer;
    }
}