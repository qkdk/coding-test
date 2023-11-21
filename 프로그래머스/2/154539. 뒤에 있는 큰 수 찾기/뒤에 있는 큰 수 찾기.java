import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = new int[numbers.length];
        
        Deque<Integer> q = new ArrayDeque<>();
        
        for (int i = numbers.length - 1; i >= 0 ;i--){
            int target = numbers[i];
            
            while(!q.isEmpty()){
                if (q.peek() > target){
                    answer[i] = q.peek();
                    break;
                }
                else{
                    q.poll();
                }
            }
            
            if (q.isEmpty()){
                answer[i] = -1;
            }
            
            
            q.addFirst(target);
        }
        return answer;
    }
}