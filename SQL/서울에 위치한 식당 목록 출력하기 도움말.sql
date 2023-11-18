SELECT B.Rest_id, rest_name, food_type, favorites, address, round(avg(review_score),2) as score
from rest_review A join rest_info B # rest_info 기준 left join == join
on A.REST_ID = B.REST_ID
# where address like '서울%'
group by B.rest_id # 식당에 해당하는 id 많은 데이터를, idx가 되는 데이터는 안됨
HAVING B.ADDRESS LIKE '서울%'
order by score desc, favorites desc
