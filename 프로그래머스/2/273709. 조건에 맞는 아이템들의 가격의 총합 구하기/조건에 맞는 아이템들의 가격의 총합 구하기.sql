SELECT SUM(a.PRICE) AS TOTAL_PRICE
FROM ITEM_INFO a
JOIN ITEM_INFO b ON a.ITEM_ID = b.ITEM_ID
WHERE a.RARITY = 'LEGEND';