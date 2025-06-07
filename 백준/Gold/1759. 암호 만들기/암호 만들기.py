# 6C4
L, C = map(int, input().split())
lst = sorted(list(map(ord, input().split())))
choose = []
모음='aeiou'

def check(words):
	global L

	vow = 0

	for w in words:
		vow += (w in 모음)

	con = L - vow

	return True if (vow >= 1) and (con >= 2) else False

def comb(idx, level):

	global L

	if level == L:
		if(check(''.join(choose))):
			for i in choose:
				print(i, end='')
			print()


	for i in range(idx, C):
		choose.append(chr(lst[i]))
		comb(i+1, level+1)
		choose.pop()

comb(0,0)