import java.util.*;

class Solution {
    public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {
        Map<String, Integer> table = new HashMap<>();
        
        table.put("code", 0);
        table.put("date", 1);
        table.put("maximum", 2);
        table.put("remain", 3);
        
        List<int[]> tmp = new ArrayList<>();
        
        for (int[] d : data){
            if (d[table.get(ext)] < val_ext){
                tmp.add(d);
            }
        }
        
        Collections.sort(tmp, (o1, o2) -> o1[table.get(sort_by)] - o2[table.get(sort_by)]);
        
        int[][] answer = new int[tmp.size()][4];

        for (int i = 0; i < tmp.size(); i++){
            answer[i] = tmp.get(i);
        }
        
        
        return answer;
    }
}