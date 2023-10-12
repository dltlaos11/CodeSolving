# N×N
# 도시의 각 칸은 빈 칸, 치킨집, 집 중 하나
# 도시의 칸은 (r, c)와 같은 형태로 나타내고, r행 c열 또는 위에서부터 r번째 칸, 왼쪽에서부터 c번째 칸을 의미한다. r과 c는 1부터 시작
# 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리
# 0은 빈 칸, 1은 집, 2는 치킨집이다.
# 각각의 집은 치킨 거리를 가지고 있다. 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.
# 이 도시에 있는 치킨집은 모두 같은 프랜차이즈이다. 프렌차이즈 본사에서는 수익을 증가시키기 위해 일부 치킨집을 폐업시키려고 한다. 오랜 연구 끝에 이 도시에서 가장 수익을 많이 낼 수 있는  치킨집의 개수는 최대 M개라는 사실
# 도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜야 한다. 어떻게 고르면, 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성
from itertools import combinations
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
chicken = []
home = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append((i,j))
        if graph[i][j] == 2:
            chicken.append((i,j))

res = sys.maxsize

chicken_combination = list(combinations(chicken,m)) # 치킨집을 m개 고르는 경우의 수, from itertools import combinations

for i in chicken_combination: # 치킨집 중 m개를 고른 값 중
    home_dist =0

    for j in range(len(home)): # 경우의 수에서 고른 치킨집에서 모든 집과의 치킨집 사이의 최솟값 구하기
        dist = sys.maxsize
        for x,y in i:
            dist = min(dist,abs(x-home[j][0])+abs(y-home[j][1]))
        home_dist += dist

    res = min(res,home_dist)

print(res)