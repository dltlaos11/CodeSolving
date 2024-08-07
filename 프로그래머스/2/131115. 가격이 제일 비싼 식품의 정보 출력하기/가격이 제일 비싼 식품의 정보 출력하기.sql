SELECT PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE
FROM FOOD_PRODUCT
GROUP BY PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE
HAVING PRICE = (SELECT MAX(PRICE) FROM FOOD_PRODUCT);

# SELECT PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE
# FROM FOOD_PRODUCT
# WHERE PRICE = (SELECT MAX(PRICE) FROM FOOD_PRODUCT);

# SELECT fp.PRODUCT_ID, fp.PRODUCT_NAME, fp.PRODUCT_CD, fp.CATEGORY, fp.PRICE
# FROM FOOD_PRODUCT fp
# JOIN (SELECT MAX(PRICE) AS max_price FROM FOOD_PRODUCT) sub
# ON fp.PRICE = sub.max_price;

# 집계 함수는 WHERE 절에서 직접 사용할 수 없고, 대신 HAVING 절이나 서브쿼리를 사용