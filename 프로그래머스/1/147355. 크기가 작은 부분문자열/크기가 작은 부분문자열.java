import java.util.*;

class Solution {
    public int solution(String t, String p) {
        long target = Long.parseLong(p);
        int sz = p.length();
        int answer = 0;
        
        for (int i = 0; i < t.length() - sz + 1; i++){
            // i ~ i + sz
            String flag = t.substring(i, i + sz);
            if (Long.parseLong(flag) <= target){
                answer += 1;
            }
        }
        
        return answer;
    }
}