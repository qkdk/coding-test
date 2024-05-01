// 각 버스마다 인원을 할당
//  각 버스의 시간을 가지고 있고
//  시간을 정렬하고
//  처음부터 탐색
//  count가 m 보다 커지거나, 시간이 커지 버스 시간보다 커지면 그만
//  위 과정들을 다 리스트에 삽입

import java.util.*;

class Solution {
    public String solution(int n, int t, int m, String[] timetable) {
        int[] nTimeTable = new int[timetable.length];
        int[] busTimeTable = new int[n];
        List<List<Integer>> people = new ArrayList<>();
        for (int i = 0; i < n; i++){
            people.add(new ArrayList<>());
        }
        
        int curTime = toInteger("09:00");
        for (int i = 0; i < n; i++){
            busTimeTable[i] = curTime;
            curTime += t;
        }
        
        for (int i = 0; i < timetable.length; i++) {
            nTimeTable[i] = toInteger(timetable[i]);
        }
        
        Arrays.sort(nTimeTable);
        
        int div = 0;
        for (int i = 0; i < n; i++){
            int count = 0;
            int endTime = busTimeTable[i];
            while (true){
                if (div >= timetable.length){
                    break;
                }
                if (nTimeTable[div] > endTime){
                    break;
                }
                if (count >= m){
                    break;
                }
                people.get(i).add(nTimeTable[div]);
                div++;
                count++;
            }
        }
        
        System.out.println(people);        
        
        // 마지막에서 이분탐색
        
        List<Integer> target = people.get(people.size() - 1);
        int lastTime = busTimeTable[people.size() - 1];
        int result = 0;
        // 꽉차있다면
        if (target.size() == m){
            result = target.get(target.size() - 1) - 1;
        }
        else{
            result = lastTime;
        }
        
        // result 되돌리기
        int hour = result / 60;
        int min = result % 60;
        
        return String.format("%02d", hour) + ":" + String.format("%02d", min);
    }
    
    public int toInteger(String time){
        String[] split = time.split(":");
        return Integer.parseInt(split[0]) * 60 + Integer.parseInt(split[1]);
    }
}