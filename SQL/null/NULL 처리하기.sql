SELECT animal_type, COALESCE(name, 'No name') AS name, SEX_UPON_INTAKe
FROM animal_ins
ORDER BY animal_id;

# SELECT COALESCE(column1, column2, 'default_value') AS result
# FROM your_table;
# 이 경우, column1이 NULL이 아니라면 column1의 값을 반환하고, 
# 그렇지 않으면 column2의 값을 반환합니다. 
# 만약 column1과 column2가 모두 NULL이라면 'default_value'가 반환됩니다.