select MCDP_CD as '진료과코드',count(APNT_NO) as '5월예약건수'
from APPOINTMENT
where date_format(date_format(APNT_YMD, '%Y-%m-%d'), '%Y-%m') = '2022-05'
group by MCDP_CD
order by count(APNT_NO), MCDP_CD