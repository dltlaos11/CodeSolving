def combination(index, level):

	if level == R:
		for c in choose:
			print(c, end=' ')
		print()
		return

	for i in range(index, N):
		choose.append(lst[i])
		combination(i+1, level+1)
		choose.pop()

while True:
	try:
		lst = list(map(int, input().split()))
		N = lst[0]
		R = 6
		lst = lst[1:]
		choose = []

		combination(0,0)
		print()

	except:
		break