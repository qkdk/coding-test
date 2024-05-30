import java.util.*;

class Solution {
    public int solution(int[] arrayA, int[] arrayB) {
        
        // 가장 작은 수의 약수를 구한다.
        // 배열을 돌면서 약수로 나누어 진다면 그래도 아니라면 약수 지우기
        
        // A -> B 로 검사
        // B -> A 로 검사
        int minA = Arrays.stream(arrayA).min().getAsInt();
        int minB = Arrays.stream(arrayB).min().getAsInt();
        
        List<Integer> listA = new ArrayList<>();
        List<Integer> listB = new ArrayList<>();
        // A의 약수들 구하기
        for(int i = 1;i <= minA; i++){
            if (minA % i == 0){
                listA.add(i);
            }
        }
        
        for(int i = 1;i <= minB; i++){
            if (minB % i == 0){
                listB.add(i);
            }
        }
        
        for (int a : arrayA){
            List<Integer> tmpLst = new ArrayList<>();
            for (Integer v : listA){
                if (a % v == 0){
                    tmpLst.add(v);
                }
            }
            listA = tmpLst;
        }
        
        for (int b : arrayB){
            List<Integer> tmpLst = new ArrayList<>();
            for (Integer v : listB){
                if (b % v == 0){
                    tmpLst.add(v);
                }
            }
            listB = tmpLst;
        }
        
        System.out.println(listA);
        System.out.println(listB);
        
        int aa = 0;
        for (int a : listA){
            boolean flag = false;
            for (int b: arrayB){
                if (b % a == 0){
                    flag = true;
                    break;
                }
            }
            
            if (flag == false){
                aa = a;
            }
        }
        
        int bb = 0;
        for (int b : listB){
            boolean flag = false;
            for (int a: arrayA){
                if (a % b == 0){
                    flag = true;
                    break;
                }
            }
            
            if (flag == false){
                bb = b;
            }
        }

        return Math.max(aa, bb);
    }
}