def Z(N, r, c):
    if N == 0: return 0
    hf = 2**(N-1)
    if r < hf and c < hf:
        return Z(N-1, r, c)
    elif r < hf and c >= hf:
        return Z(N-1, r, c-hf)+hf**2
    elif r >= hf and c < hf:
        return Z(N-1, r-hf, c) + (hf**2)*2
    else:
        return Z(N-1, r-hf, c-hf) +(hf**2)*3

N, r, c = map(int, input().split())
print(Z(N, r, c))