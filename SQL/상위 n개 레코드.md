# 상위 n개 레코드

```sql
-- 코드를 입력하세요
SELECT NAME
from ANIMAL_INS
order by DATETIME asc
limit 1
```

### LIMIT

- LIMIT은 가장 맨 뒤에 사용
- 정렬까지 다 끝난 후에 최종 Top K개
