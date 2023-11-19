-- 코드를 입력하세요
# FIRST_HALF 테이블의 기본 키는 FLAVOR
# ICECREAM_INFO테이블의 FLAVOR는 FIRST_HALF 테이블의 FLAVOR의 외래 키
# 각 아이스크림 성분 타입과 성분 타입에 대한 아이스크림의 총주문량
# 총주문량이 작은 순서대로 조회하는 SQL 문
SELECT i.INGREDIENT_TYPE, sum(f.TOTAL_ORDER) TOTAL_ORDER
from FIRST_HALF f left join ICECREAM_INFO i
on f.flavor = i.flavor
group by i.INGREDIENT_TYPE
order by TOTAL_ORDER asc