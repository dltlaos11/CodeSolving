-- 코드를 입력하세요
SELECT p.PRODUCT_CODE, sum(SALES_AMOUNT * PRICE) as PRICE
from product p join offline_sale o 
on p.product_id = o.product_id
group by p.PRODUCT_CODE
order by price desc, PRODUCT_CODE
