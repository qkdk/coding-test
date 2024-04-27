-- 코드를 입력하세요
# 둘이 아이디를 기준으로 조인하고, DateTime 값을 뺀거를 하나 불러온다, id, 이름
# 이 테이블을 정렬

SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS A, ANIMAL_OUTS B
WHERE A.ANIMAL_ID = B.ANIMAL_ID
ORDER BY B.DATETIME - A.DATETIME DESC
LIMIT 2
