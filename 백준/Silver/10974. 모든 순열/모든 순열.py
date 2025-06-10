N = int(input())
R = N

check = [False] * N
lst = [i for i in range(1, N+1)]
choose = []


def permutation(level):

	if level == R:
		for i in choose:
			print(i, end=" ")
		print()

		return


	for i in range(0, N):

		if check[i] == True:
			continue

		check[i] = True

		choose.append(lst[i])

		permutation(level+1)

		check[i] = False
		choose.pop()

permutation(0)