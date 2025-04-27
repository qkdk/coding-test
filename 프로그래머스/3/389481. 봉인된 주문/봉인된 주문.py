'''
1. 완전탐색 방법 -> 불가능 (n이 너무 크다)
2. 규칙을 찾아야함
    -> 알파벳을 보고 순서를
    -> 순서를 보고 알파벳을
    
* 풀이방법
26진수와 같다, 대신 0이 없는
0이 없으니 0값이 오면 몫을 1 빼고, 나머지는 26
1. 알파벳 to 순서
    - 26 ** 자릿수 * 자라의 알파벳( a - > 1, z -> 26)
2. 순서 to 알파벳
    -
3. n 아래에 있는 수들이 제거되면 탐색해야 n + 1을 해준다.
    - +1 했을때 n 이 커짐을 유의
    - 오름차순을 정렬하고 하나 제거할때마다 n을 업데이트
    
* 핵심
0 이 없기때문에 나머지가 0 이라면 몫을 1빼고 나머지를 26으로 맞춰줘야 한다.
'''

from collections import deque

def solution(n, bans):
    bans.sort(key=lambda x: (len(x), x))
    # print(bans)
    for v in bans:
        r = alpha_to_numeric(v)
        if r <= n:
            n += 1
    
    answer = numeric_to_alpha(n)
    
    return answer

def change_char_to_num(alpha: str):
    return ord(alpha) - ord('a') + 1

def alpha_to_numeric(alpha:str):
    length = len(alpha) - 1
    
    result = 0
    for i, v in enumerate(alpha):
         result += change_char_to_num(v) * 26 ** (length - i)
    
    return result

def numeric_to_alpha(num: int):
    # 몫을 나눌수 없을때 까지 계속 나누고
    a = num
    b = float('inf')
    
    q = deque()
    while a != 0:
        b = a % 26
        a = a // 26
        
        if b == 0:
            a -= 1
            b = 26
        
        q.append(b)
    
    result = ""
    while q:
        a = chr(ord('a') + q.pop() - 1)
        result += a
        
    return result
    
