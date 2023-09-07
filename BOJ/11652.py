import sys
input = sys.stdin.readline
TC = int(input())
cards = {}

for _ in range(TC):
    card = int(input())
    if card not in cards:
        cards[card] = 0
    cards[card] += 1

max_val = -1*sys.maxsize

max_card = 0
for card in cards:
    if cards[card] > max_val:
        max_card = card
        max_val = cards[card]
    elif cards[card] == max_val and max_card > card:
        max_card = card

print(max_card)

# import sys
# input = sys.stdin.readline
#
# n: int = int(input())
# cards = [int(input()) for _ in range(n)]
# cards.sort()
#
# maxCnt = 1
# maxVal = cards[0]
# cnt = 1
#
# for i in range(1, n):
#     if cards[i] == cards[i - 1]:
#         cnt += 1
#     else:
#         cnt = 1
#
#     if cnt > maxCnt:
#         maxCnt = cnt
#         maxVal = cards[i]
#
# print(maxVal)
