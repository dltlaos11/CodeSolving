-- 코드를 입력하세요
SELECT o.ANIMAL_ID, o.ANIMAL_TYPE, o.NAME
from ANIMAL_INS i join ANIMAL_OUTS o
on i.ANIMAL_ID = o.ANIMAL_ID
where i.SEX_UPON_INTAKE like 'Intact%' and o.SEX_UPON_OUTCOME not like 'Intact%'
order by o.ANIMAL_ID
