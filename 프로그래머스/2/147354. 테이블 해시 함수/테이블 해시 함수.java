import java.util.*;

class Solution {
    public int solution(int[][] data, int col, int row_begin, int row_end) {
        Arrays.sort(data, (o1,o2) -> o1[col - 1] == o2[col - 1] ? o2[0] - o1[0] : o1[col - 1] - o2[col - 1]);
        
        int answer = 0;        
        for (int i = row_begin; i <= row_end; i++){
            int tmpSum = 0;
            for (int v : data[i-1]){
                tmpSum += v % i;
            }
            answer = answer ^ tmpSum;
        }
        return answer;
    }
}