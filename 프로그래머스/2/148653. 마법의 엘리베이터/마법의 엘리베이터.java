import java.util.*;

class Solution {
    
    static int answer = 0;
    public int solution(int storey) {     
        // 4 이하 일때는 내려가기
        // 6 이상 일때는 올라가기
        // 5 일때는 상위 값을 보고 올라가거나 내려가거나 판단한다.
            // 상위값이 4 이상 -> 내려간다 5 이상-> 올라간다 판단해서 결정
        while(storey > 0){
            int num = storey % 10;
            storey = storey / 10;
            
            if (num == 5){
                if (storey % 10 < 5){
                    answer += num;
                }
                else{
                    answer += 10 - num;
                    storey++;
                }
            }
            else if (num <=4){
                answer += num;
            }
            else {
                answer += 10 - num;
                storey++;
            }
        }
        
        return answer;
    }
    
}