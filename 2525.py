hour, minute = map(int, input().split())
need = int(input())
minute = need + minute
if minute > 59:
    hour = minute//60 + hour
    minute = minute%60
if hour > 23:
    hour = hour - 24
print(hour, minute)
# 