-- 코드를 작성해주세요

# 사원과 그레이드를 번호 기준으로 조인 하고
# case 써서 등급 기준으로 score 기준으로 등급 매기고
# 다시한번 case 써서 보너스 계산

WITH A AS
(SELECT EMP_NO,
    CASE
        WHEN AVG(SCORE) >= 96 THEN 'S'
        WHEN AVG(SCORE) >= 90 THEN 'A'
        WHEN AVG(SCORE) >= 80 THEN 'B'
        ELSE 'C'
END GRADE
FROM HR_GRADE
GROUP BY EMP_NO)

SELECT A.EMP_NO, E.EMP_NAME, A.GRADE, 
CASE
    WHEN GRADE = 'S' THEN E.SAL * 0.2
    WHEN GRADE = 'A' THEN E.SAL * 0.15
    WHEN GRADE = 'B' THEN E.SAL * 0.1
    ELSE 0
END BONUS
FROM HR_EMPLOYEES E JOIN A ON E.EMP_NO = A.EMP_NO
ORDER BY A.EMP_NO ASC