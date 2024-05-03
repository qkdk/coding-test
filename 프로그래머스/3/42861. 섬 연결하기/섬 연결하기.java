import java.util.*;

class Solution {
    static class Vertex implements Comparable<Vertex>{
        int e, cost;
        
        Vertex(int e, int cost){
            this.e = e;
            this.cost = cost;
        }
        
        public int compareTo(Vertex o){
            return this.cost - o.cost;
        }
    }
    
    public int solution(int n, int[][] costs) {
        Map<Integer, List<Vertex>> graph = new HashMap<>();
        
        for (int i = 0; i < n; i++){
            graph.put(i, new ArrayList<>());
        }
        
        for (int[] cost : costs){
            int start = cost[0];
            int end = cost[1];
            int c = cost[2];
            
            graph.get(start).add(new Vertex(end, c));
            graph.get(end).add(new Vertex(start, c));
        }
        
        // 시작점 하나를 잡고, 계속 낮은 값을 뽑는다.
        PriorityQueue<Vertex> q = new PriorityQueue<>();
        boolean[] visited = new boolean[n];
        // visited[0] = true;
        
        q.add(new Vertex(0,0));
        int answer = 0;
        while(!q.isEmpty()){
            Vertex cur = q.poll();    
            
            if (visited[cur.e]){
                continue;
            }
            visited[cur.e] = true;
            answer += cur.cost;
            
            for (Vertex next: graph.get(cur.e)){
                if (visited[next.e]){
                    continue;
                }
                
                q.add(next);
            }
        }
        
        return answer;
    }
}