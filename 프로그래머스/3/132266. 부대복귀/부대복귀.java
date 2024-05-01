// 도착지에서 탐색을 하면 된다...

import java.util.*;

class Solution {
    static final int INF = Integer.MAX_VALUE / 2;
    
    public int[] solution(int n, int[][] roads, int[] sources, int destination) {
        int[] answer = new int[sources.length];
        Map<Integer, List<Integer>> graph = new HashMap<>();
    
        for (int i = 1; i < n + 1; i++){
            graph.put(i, new ArrayList<>());
        }
        
        for (int[] road: roads){
            graph.get(road[0]).add(road[1]);
            graph.get(road[1]).add(road[0]);
        }
        
        int[] result = bfs(graph, destination, n);
        for (int i = 0; i < sources.length; i++){
            int source = sources[i];
            answer[i] = result[source] == INF? -1 : result[source];
        }
        
        return answer;
    }
    
    static class Pair{
        int e;
        int depth;
        
        Pair(int e, int depth){
            this.e = e;
            this.depth = depth;
        }
    }
    
    public int[] bfs(Map<Integer, List<Integer>> graph, int start, int n){
            
        Deque<Pair> q = new ArrayDeque<>();
        q.add(new Pair(start, 0));
        
        boolean[] visited = new boolean[n + 1];
        int[] dist = new int[n + 1];
        Arrays.fill(dist,INF);
        visited[start] = true;
        
        while(!q.isEmpty()){
            Pair cur = q.poll();
            
            dist[cur.e] = cur.depth;
            
            List<Integer> nexts = graph.get(cur.e);
            for (int next: nexts){
                if (visited[next]){
                    continue;
                }
                
                visited[next] = true;
                
                q.add(new Pair(next, cur.depth + 1));
            }
            
        }
        
        // System.out.println(Arrays.toString(dist));
        return dist;
        
    }

}











// import java.util.*;

// class Solution {
//     static final int INF = Integer.MAX_VALUE / 2;
    
//     static class Vertex implements Comparable<Vertex>{
//         int e;
//         int cost;
        
//         public int compareTo(Vertex o){
//             return this.cost - o.cost;
//         }
        
//         Vertex(int e, int cost){
//             this.e = e;
//             this.cost = cost;
//         }
//     }
    
//     public int[] solution(int n, int[][] roads, int[] sources, int destination) {
//         int[] answer = new int[sources.length];
        
//         Map<Integer, List<Vertex>> graph = new HashMap<>();
    
//         for (int i = 1; i < n + 1; i++){
//             graph.put(i, new ArrayList<>());
//         }
//         for (int[] road: roads){
//             graph.get(road[0]).add(new Vertex(road[1], 1));
//             graph.get(road[1]).add(new Vertex(road[0], 1));
//         }
        
//         for (int i = 0; i < sources.length; i++){
//             int start = sources[i];
//             answer[i] = dijk(graph, start, n, destination);
//         }
                
//         return answer;
//     }
    
//     public int dijk(Map<Integer, List<Vertex>> graph, int start, int n, int destination){
//         int[] dist = new int[n + 1];
//         boolean[] visited = new boolean[n + 1];
        
//         Arrays.fill(dist, INF);
//         PriorityQueue<Vertex> q = new PriorityQueue<>();
        
//         q.add(new Vertex(start, 0));
//         dist[start] = 0;
        
//         while (!q.isEmpty()){
//             Vertex cur = q.poll();
            
//             if (visited[cur.e]){
//                 continue;
//             }
            
//             visited[cur.e] = true;
            
//             List<Vertex> nexts = graph.get(cur.e);
//             for (Vertex next : nexts){
//                 if (dist[next.e] > dist[cur.e] + next.cost){
//                     dist[next.e] = dist[cur.e] + next.cost;
//                     q.add(new Vertex(next.e, dist[next.e]));
//                 }
//             }
//         }
        
//         // System.out.println(Arrays.toString(dist));
//         return dist[destination] == INF? -1: dist[destination];
//     }
// }