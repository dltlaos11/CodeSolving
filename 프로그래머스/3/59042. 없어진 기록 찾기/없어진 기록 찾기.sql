# -- 코드를 입력하세요
# SELECT a.ANIMAL_ID, a.NAME
# from ANIMAL_OUTS as a left join ANIMAL_INS as b
# on a.ANIMAL_ID = b.ANIMAL_ID
# WHERE b.datetime IS NULL
# order by a.ANIMAL_ID





select o.ANIMAL_ID, o.NAME
from ANIMAL_OUTS o  left join ANIMAL_INS i
on i.ANIMAL_ID = o.ANIMAL_ID
where i.DATETIME is null
order by i.ANIMAL_ID








