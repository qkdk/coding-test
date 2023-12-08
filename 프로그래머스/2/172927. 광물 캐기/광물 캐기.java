import java.util.*;

class Solution {
    
    static int answer = Integer.MAX_VALUE;
    public int solution(int[] picks, String[] minerals) {
        dfs(picks, minerals, 0, 0);
        return answer;
    }
    
    public static void dfs(int[] picks, String[] minerals, int index, int piro){
        if (index >= minerals.length){
            answer = Math.min(answer, piro);
            return;
        }
        
        boolean flag = false;
        for (int p: picks){
            if (p != 0){
                flag = true;
            }
        }
        
        if (!flag){
            answer = Math.min(answer, piro);
            return;
        }
        
        for (int i = 0; i < 3; i++){
            if(picks[i] != 0){
                int tmp = 0;
                for (int j = index; j < index + 5; j++){
                    if (j >= minerals.length){
                        break;
                    }                    
                    if (i == 0){
                        tmp++;
                    }
                    if (i == 1){
                        if (minerals[j].equals("diamond")){
                            tmp += 5;
                        }
                        if (minerals[j].equals("iron")){
                            tmp += 1;
                        }
                        if (minerals[j].equals("stone")){
                            tmp += 1;
                        }
                    }
                    if (i == 2){
                        if (minerals[j].equals("diamond")){
                            tmp += 25;
                        }
                        if (minerals[j].equals("iron")){
                            tmp += 5;
                        }
                        if (minerals[j].equals("stone")){
                            tmp += 1;
                        }
                    }
                }
                picks[i]--;
                dfs(picks, minerals, index + 5, piro + tmp);
                picks[i]++;                 
            }
        }
    }
}

