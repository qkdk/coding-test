import java.util.*;

class Solution {
    
    static int[][] vector = {{-1,0},{0,1},{1,0},{0,-1}};
    
    public int solution(String[] board) {
        char[][] table = new char[board.length][board[0].length()];
        for (int i = 0; i < table.length; i++){
            for (int j = 0; j < table[0].length; j++){
                table[i][j] = board[i].charAt(j);
            }
        }
        
        return bfs(findStart(table), table);
    }
    
    public int bfs(int[] starts, char[][] table){
        boolean[][] visited = new boolean[table.length][table[0].length];
        ArrayDeque<int[]> q = new ArrayDeque<>();
        visited[starts[0]][starts[1]] = true;
        
        int[] s = new int[3];
        for (int i = 0; i< 2; i++){
            s[i] = starts[i];
        }
        s[2] = 0;
        q.add(s);
        
        while(!q.isEmpty()){
            int[] cur = q.poll();
            if (table[cur[0]][cur[1]] == 'G'){
                return cur[2];
            }
            
            for (int[] dir : vector){
                // 끝점을 찾는 기능
                int[] end = findEnd(table, dir, cur);
                
                if (visited[end[0]][end[1]]){
                    continue;
                }
                
                visited[end[0]][end[1]] = true;
                
                q.add(new int[]{end[0], end[1], cur[2] + 1});
            }
        }
        return -1;
    }
    
    // 끝점을 찾는 기능
    public int[] findEnd(char[][] table, int[] dir, int[] cur){
        int y = cur[0];
        int x = cur[1];
        
        while(true){
            int ny = y + dir[0];
            int nx = x + dir[1];
            
            if (ny < 0 || nx < 0 || ny >= table.length || nx >= table[0].length){
                break;
            }
            
            if (table[ny][nx] == 'D'){
                break;
            }
            
            y = ny;
            x = nx;
        }
        
        return new int[]{y,x};
    }
    
    // 시작점을 찾는 기능
    public int[] findStart(char[][] board){
        for (int i =0; i < board.length; i++){
            for (int j = 0; j < board[0].length; j++){
                if (board[i][j] == 'R'){
                    return new int[]{i,j};
                }
            }
        }
        return null;
    }
}