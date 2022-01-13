# a = int(input())
# b = input().split()
# c = int(input())
# d = input().split()
#
# for i in range(c):
#     cnt = 0
#     for j in range(a):
#         if b[j] == d[i]:
#             cnt = cnt +1
#     print(cnt, end =" ")

#dict = {'하이': 300, '헬로': 180}
#print(dict.get('동동', 0))

dic = {}
dic_sec = {}
fir_Cnt = int(input())
fir_Val = input().split()
sec_Cnt = int(input())
sec_Val = input().split()
# list2 = []

for i in range(fir_Cnt):
    if fir_Val[i] not in dic.keys():
        dic[fir_Val[i]] = 1
    elif fir_Val[i] in dic.keys():
        val = dic[fir_Val[i]]
        dic[fir_Val[i]] = val + 1

for j in range(sec_Cnt):
    if sec_Val[j] in dic.keys():
        dic_sec[sec_Val[j]] = dic[sec_Val[j]]
    else:
        dic_sec[sec_Val[j]] = 0

# for val in dic_sec.values():
#     list2.append(val)
# for j in list2:
#     print(j, end=" ")


for value in dic_sec.values():
    print(value, end=' ')
