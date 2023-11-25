def solution(friends, gifts):
    answer = 0
    cnt_this_mon_gifts = {}
    cnt_gifts_score = {}
    cnt_to_me = {}

    for i in friends:
        cnt_this_mon_gifts[i] = []
        cnt_gifts_score[i] = [0, 0]  # 준선물 받은선물
        cnt_to_me[i] = 0

    for i in gifts:
        arr = i.split(' ')
        cnt_this_mon_gifts[arr[0]].append(arr[1])

    for k, v in cnt_this_mon_gifts.items():
        cnt_gifts_score[k][0] = len(v)
        for i in v:
            cnt_gifts_score[i][1] += 1

    for k, v in cnt_gifts_score.items():
        check = set(cnt_this_mon_gifts[k])
        temp = [k]
        for i in list(check):
            temp.append(i)
            if cnt_this_mon_gifts[k].count(i) > cnt_this_mon_gifts[i].count(k):
                cnt_to_me[k] += 1
            elif cnt_this_mon_gifts[k].count(i) == cnt_this_mon_gifts[i].count(k):
                sum1 = cnt_gifts_score[i][0] - cnt_gifts_score[i][1]
                sum2 = cnt_gifts_score[k][0] - cnt_gifts_score[k][1]
                if sum2 > sum1:
                    cnt_to_me[k] += 1

        check_not_link = set(friends) - set(temp)

        for i in list(check_not_link):
            if cnt_this_mon_gifts[i].count(k) == 0:
                sum1 = cnt_gifts_score[i][0] - cnt_gifts_score[i][1]
                sum2 = cnt_gifts_score[k][0] - cnt_gifts_score[k][1]
                if sum2 > sum1:
                    cnt_to_me[k] += 1
            elif cnt_gifts_score[i] == cnt_gifts_score[k]:
                sum1 = cnt_gifts_score[i][0] - cnt_gifts_score[i][1]
                sum2 = cnt_gifts_score[k][0] - cnt_gifts_score[k][1]
                if sum2 > sum1:
                    cnt_to_me[k] += 1

    max_val = 0
    for k, v in cnt_to_me.items():
        if v > max_val:
            max_val = v
        answer = max_val

    return answer
# 이번달까지 선물을 주고받은 기록을 바탕으로 다음 달에 누가 선물을 많이 받을지 예측

# 두 사람이 선물을 주고받은 기록이 있다면,
# 이번 달까지 두 사람 사이에 더 많은
# 선물을 준 사람이 다음 달에 선물을 하나 받는다.
# 예를들어 A가 B에게 선물을 5번줬고, B가 A에게 3번줬다면 A가 B에게 선물을 하나 받음
# -> 이번달 기록 있다면 많이 준사람이 받음

# 두 사람이 선물을 주고 받은 기록이 하나도 없거나 주고 받은수가 같다면,
# 선물 지수가 더 큰 사람이 선물 지수가 더 작은 사람에게 선물을 하나 받음
# 선물 지수는 이번 달까지 자신이 친구들에게 준 선물의 수에서 받은 선물의 수를 뺀값
# 예를 들어 A가 준선물 3, 받:10, A의 지수:-7
# B가 준선물:3, 받은선물:2, B의 지수: 1
# A,B가 선물을 주고 받은 적이 없거나 정확히 같은 수로 주고받았다면,
# 다음달에 B가 A에게 선물을 하나 받음
# -> 이번달 주고받은 내역이 없거나 같다면, 선물 지수로 따지고 높은 사람이 받음

# 친구들의 이름 문자열 배열: friends
# 이번달까지 주고받은 선물기록: gifts
# 다음달에 가장 많은 선물을 받는 친구가 받을 선물의 수를 return