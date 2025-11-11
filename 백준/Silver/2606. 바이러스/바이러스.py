# dfs
def dfs(node):

	global visited, adj_lst, cnt
	# “현재 node와 직접 연결된 모든 노드들(list)”
	# 즉, adj_lst[node]는 리스트이고, 그 안에는 현재 노드가 갈 수 있는 노드 번호들이 들어 있습니다.
	# 예를 들어:
	# node = 1
	# adj_lst[node] == [2, 4]
	# 즉, 1번에서 갈 수 있는 노드는 2번과 4번이라는 뜻입니다.

	if visited[node] == True:
		return

	visited[node] = True

	cnt += 1

	for adj_node in adj_lst[node]:
		dfs(adj_node)

N = int(input()) # 노드
M = int(input()) # 간선

# 인접 리스트 초기화
adj_lst = [[] for _ in range(N+1)] # padding용
visited = [False for _ in range(N+1)]

# 간선 입력
for _ in range(M):
	a, b = map(int, input().split())
	adj_lst[a].append(b)
	adj_lst[b].append(a) # 양방향 그래프라면 이 줄 추가

cnt = 0
dfs(1)
# print(cnt-1)
print(sum(visited) -1)