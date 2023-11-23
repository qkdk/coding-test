import java.util.*;

class Solution {
    
    // 각 번호마다 dfs를 실시
    // 하나의 그룹마다 list 에 저장
    // 여기서 두개 뽑음
    
    public int solution(int[] cards) {
        boolean[] visited = new boolean[cards.length];
        
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < cards.length; i++){
            
            if (visited[i]){
                continue;
            }
            
            ans.add(dfs(cards, visited, i, 0));
        }
        ans.add(0);
        Collections.sort(ans);
        return ans.get(ans.size() - 1) * ans.get(ans.size() - 2);
    }
    
    public int dfs(int[] cards ,boolean[] visited, int index, int count){
        if (isOutOfIndex(index, cards)){
            return count;
        }
        if (visited[index]){
            return count;
        }

        visited[index] = true;
        int next = getIndex(cards[index]);
        
        return dfs(cards, visited, next, count+1);
    }
    
    public int getIndex(int num){
        return num - 1;
    }
    
    public boolean isOutOfIndex(int index, int[] cards){
        if (index >= cards.length){
            return true;
        }
        return false;
    }
}