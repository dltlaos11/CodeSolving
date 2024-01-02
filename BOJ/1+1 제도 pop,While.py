T = int(input())
for test_case in range(1, T + 1):
    buy_item_list = list(map(int, input().split()))

    temp = []
    free_temp = []

    while(len(buy_item_list) != 0):
        temp.append(max(buy_item_list))
        buy_item_list.pop(buy_item_list.index(max(buy_item_list)))
        if len(buy_item_list) == 0:
            break
        else:
            if max(buy_item_list) == temp[0]:
                temp.append(max(buy_item_list))
                buy_item_list.pop(buy_item_list.index(max(buy_item_list)))
        free_temp.append(max(buy_item_list))
        buy_item_list.pop(buy_item_list.index(max(buy_item_list)))
        if len(buy_item_list) == 0:
            break
        else:
            if len(buy_item_list) == 1:
                free_temp.append(max(buy_item_list))
            else:
                if max(buy_item_list) == min(buy_item_list):
                    for i in buy_item_list:
                        temp.append(i)
                        buy_item_list.pop(buy_item_list.index(i))
                        temp.append(i)
                else:
                    temp.append(max(buy_item_list))
                    buy_item_list.pop(buy_item_list.index(max(buy_item_list)))
        print(f'#{test_case} {sum(temp)}')

    # print(f"{test_case} {sum(temp)}")
    # 5 3 4 3
    # 5 temp
    # 3 4 3
    # 4 free
    # 3 3
    # if same
# 1 2 3 4
# 4 temp
# 1 2 3
# 3 free
# 1 2
# 2 temp
# 1 free

# 5 2 5 1
# 5 temp
# 2 5 1
# 5 if max(temp) 같다면 temp
# 2 1
# 2 temp
# 1 free
# test