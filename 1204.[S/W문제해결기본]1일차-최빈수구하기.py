T = int(input())
for i in range(1,T+1):
    idx = int(input())
    arr = list(map(int, input().split()))
    score = dict()
    for s in arr:
        if s in score:
            score[s] += 1
        else:
            score[s] = 1
    Max = max(score.values())
    key = next(key for key,value in score.items() if value == Max)
    print('#%d %d'%(i, key))

    # arr = list(map(int, input().split()))
    # score = dict()
    # for s in arr:
    #     if s in score: # 첨엔 없으므로 1씩 넣고
    #         score[s] += 1 # 또나오면 1 더하기
    #     else:
    #         score[s] = 1
# ---------------------------------------------------------------------------------

    # list로 된 값을 얻고 싶다면
    # key = [key for key, value in "Dict".items() if value == "값"]

    # 정수로 된 값 ! next() 함수 사용 !!!!😀
    # key = next(key for key, value in "Dict".items() if value == "값")
    # next는 기본값을 지정할 수 있다. 기본값을 지정하면 반복이 끝나더라도 StopIteration이 발생하지 않고
    # 기본값을 출력. 즉, 반복할 수 있을 떄는 해당 값을 출력하고, 반복이 끝났을 떄는 기본값을 출력.

    # >> > it = iter(range(3))
    # >> > next(it, 10)
    # 0
    # >> > next(it, 10)
    # 1
    # >> > next(it, 10)
    # 2
    # >> > next(it, 10)
    # 10