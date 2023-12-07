class Solution {
    public int[] solution(int[] sequence, int k) {
        
        // 투포인터
        // k 랑 같아지면 시작 인덱스 + 1
        // k 보다 커지면 시작 인덱스 + 1
        // k 보다 작아지면 끝 인덱스 + 1
        // 최소 길이를 저장하고 있고 최소가 된다면 업데이트
        
        int startIndex = 0;
        int endIndex = 0;
        int sum = sequence[0];
        int length = 0;
        
        int answerL = Integer.MAX_VALUE;
        int[] answer = new int[2];
        while (true){
            if (sum < k){
                endIndex++;
                length++;
                if(endIndex == sequence.length){
                    break;
                }
                sum += sequence[endIndex];
            }
            else if (sum > k){
                sum -= sequence[startIndex];
                startIndex++;
                length--;
            }
            else {
                if (length < answerL){
                    answer[0] = startIndex;
                    answer[1] = endIndex;
                    answerL = length;
                }
                
                sum -= sequence[startIndex];
                startIndex++;
                length--;
            }
        }
        return answer;
    }
}