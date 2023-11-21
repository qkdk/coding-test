import java.util.*;

class Solution {
    
    private static final int[][] vector = {{-1,0},{0,1},{1,0},{0,-1}};
    
    static class Pair{
        public int y;
        public int x;
        public int depth;
        
        Pair(int y, int x, int depth){
            this.y = y;
            this.x = x;
            this.depth = depth;
        }
    }
    
    public int solution(String[] maps) {
        char[][] matrix = new char[maps.length][maps[0].length()];
        
        // 맵 전처리
        Pair start = null;
        for (int i = 0; i < maps.length; i++){
            for (int j = 0; j < maps[0].length(); j++){
                matrix[i][j] = maps[i].charAt(j);
                if(matrix[i][j] == 'S'){
                    start = new Pair(i, j, 0);
                }
            }
        }
      
        Pair lever = bfs(matrix, start, 'L');
        if(lever == null){
            return -1;
        }
        
        Pair exit = bfs(matrix, lever, 'E');
        if(exit == null){
            return -1;
        }
        return exit.depth;
    }
    
    public Pair bfs(char[][] matrix, Pair start, char target){
        Deque<Pair> q = new ArrayDeque<>();
        boolean[][] visited = new boolean[matrix.length][matrix[0].length];
        q.add(start);
        visited[start.y][start.x] = true;
        
        Pair lever = null;
        L:while(!q.isEmpty()){
            Pair cur = q.poll();
            for (int d= 0; d < 4; d++){
                int ny = cur.y + vector[d][0];
                int nx = cur.x + vector[d][1];
                
                if (ny < 0 || nx < 0 || ny >= matrix.length || nx >= matrix[0].length){
                    continue;
                }
                
                if (visited[ny][nx]){
                    continue;
                }
                
                if (matrix[ny][nx] == 'X'){
                    continue;
                }
                
                if (matrix[ny][nx] == target){
                    return new Pair(ny,nx, cur.depth + 1);
                }
                
                q.add(new Pair(ny,nx, cur.depth + 1));
                visited[ny][nx] = true;
            }
        }
        return null;
    }
}