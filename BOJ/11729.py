def hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return

    hanoi(n - 1, start, 6 - start - end)  # a -> 6-a-b
    print(start, end)  # a -> b
    hanoi(n - 1, 6 - start - end, end)  # 6-a-b -> b


n = int(input())
print(2 ** n - 1) # 하노이 총 수행 횟수
hanoi(n, 1, 3)


# def hanoi(n: int, start: int, end: int, tmp: int):
#     if n == 1:
#         print(start, end)
#     else:
#         hanoi(n - 1, start, tmp, end)
#         print(start, end)
#         hanoi(n - 1, tmp, end, start)
#
#
# n: int = int(input())
#
# print(2 ** n - 1)
# hanoi(n, 1, 3, 2)