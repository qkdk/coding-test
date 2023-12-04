class Solution {
    public long solution(int k, int d) {
        long answer = 0;
        for (int i = 0; i <= d; i += k){
            long maxY = (long) Math.sqrt((long)d*d - (long)i*i);
            answer += maxY / k + 1;
        }
        
        return answer;
    }
}