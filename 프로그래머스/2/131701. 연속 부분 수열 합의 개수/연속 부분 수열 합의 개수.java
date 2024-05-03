import java.util.*;

class Solution {
    public int solution(int[] elements) {
        int[] arr = new int[elements.length * 2];
        for (int i = 0; i < arr.length; i++){
            arr[i] = elements[i % elements.length];
        }
        
        System.out.println(Arrays.toString(arr));
        Set<Integer> set = new HashSet<>();
        for (int i = 1; i< elements.length + 1; i++){
            
            for (int j = 0; j < arr.length - i + 1; j++){
                
                int tmp = 0;
                for (int k = 0; k < i; k++){
                    tmp += arr[j + k];
                }
                set.add(tmp);
            }
        }
        return set.size();
    }
}