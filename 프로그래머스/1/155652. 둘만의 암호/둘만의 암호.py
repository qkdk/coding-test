def solution(s, skip, index):
    lst = []
    st = set(skip)
    
    # 알파벳 리스트를 만든다.
    # 스킵에 있는거 지우고 
    for c in range(ord('a'), ord('z') + 1):
        if chr(c) in st:
            continue
        else:
            lst.append(chr(c))

    # s 에 있는거에 index 뒤에 있는거 찾는데
    ans = []
    for i, v in enumerate(s):
        # s 인덱스 찾기
        idx = lst.index(v)
        nIdx = idx + index
        if nIdx >= len(lst):
            nIdx = nIdx % len(lst)
        ans.append(lst[nIdx])
        

    # 일다 인덱스 찾고 검색
    return ''.join(ans)