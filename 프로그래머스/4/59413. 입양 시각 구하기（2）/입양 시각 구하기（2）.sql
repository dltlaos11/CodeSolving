-- 코드를 입력하세요
set @hour = -1;
select (@hour := @hour +1) as 'HOUR',
    (select count(hour(datetime))
    from ANIMAL_OUTS
    where hour(datetime) = @hour) as 'COUNT'
from ANIMAL_OUTS
where @hour <=22