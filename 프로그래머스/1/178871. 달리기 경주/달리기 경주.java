import java.util.*;


class Solution {
    public String[] solution(String[] players, String[] callings) {
        Map<String, Integer> table = new HashMap<>();
        
        for (int i = 0; i < players.length; i++){
            table.put(players[i], i);
        }
        
        for (String name: callings){
            int idx = table.get(name);
            String tmp = players[idx - 1];
            players[idx - 1] = name;
            players[idx] = tmp;
            
            table.compute(name, (k, v) -> idx - 1);
            table.compute(tmp, (k, v) -> idx);
        }
        
        return players;
    }
}