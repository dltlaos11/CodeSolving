def solution(people, limit):

    people = sorted(people)

    left, right = 0, len(people)-1

    cnt = 0

    while left <= right:

        cnt += 1

        if (people[left] + people[right] <= limit):
            left += 1

        right -= 1  # bitch fly solo

    return cnt

# 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다
# [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면
# 2번째 사람과 4번째 사람은 같이 탈 수 있지만
# 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.
# 구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.
# 사람들의 몸무게를 담은 배열 people
# 구명보트의 무게 제한 limit
# 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return