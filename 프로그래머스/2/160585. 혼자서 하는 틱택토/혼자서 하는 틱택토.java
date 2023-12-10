import java.util.*;

class Solution {
    
    // 게임이 끝났는데 계속한지 확인하는 방법
    // O 가 끝났다면 X 갯수가 O보다 작아야 한다.
    // X 가 끝났다면 O 갯수가 X 랑 같아야 한다.
    
    static char[][] table = new char[3][3];
    public int solution(String[] board) {
        for (int i = 0; i < board.length; i++){
            for (int j = 0; j < board[0].length(); j++){
                table[i][j] = board[i].charAt(j);
            }
        }
        int oCount = calculateCount('O');
        int xCount = calculateCount('X');
        
        if (xCount > oCount){
            return 0;
        }
        if (oCount > xCount + 1){
            return 0;
        }
        if (checkEnd('O')){
            if (xCount >= oCount){
                return 0;
            }
        }
        
        if (checkEnd('X')){
            if (xCount != oCount){
                return 0;
            }
        }
        
        return 1;
    }
    int calculateCount(char std){
        int count = 0;
        for (char[] line: table){
            for (char c: line){
                if (c == std){
                    count++;
                }
            }
        }
        return count;
    }
    
    boolean checkEnd(char std){
        // 가로
        for (int i = 0; i < table.length; i++){
            boolean flag = false;
            for (int j = 0;j < table[i].length; j++){
                if (table[i][j] != std){
                    flag = true;
                    break;
                }
            }
            
            if (!flag){
                return true;
            }
        }
        
        // 세로
        for (int i = 0; i < table.length; i++){
            boolean flag = false;
            for (int j = 0;j < table[i].length; j++){
                if (table[j][i] != std){
                    flag = true;
                    break;
                }
            }
            
            if (!flag){
                return true;
            }
        }
        
        boolean flag = false;
        for (int i = 0; i < 3; i++){
            if (table[i][i] != std){
                flag = true;
                break;
            }
        }
        
        if (!flag){
            return true;
        }
        
        flag = false;
        for (int i = 0; i < 3; i++){
            if (table[i][2-i] != std){
                flag = true;
                break;
            }
        }
        
        if (!flag){
            return true;
        }
        return false;
    }
}

