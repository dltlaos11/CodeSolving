-- 코드를 입력하세요
SELECT HOUR(datetime) as 'Hour', count(datetime) as 'COUNT'
from ANIMAL_OUTS
where HOUR(datetime) BETWEEN 9 AND 19
group by hour(datetime)
order by hour(datetime)