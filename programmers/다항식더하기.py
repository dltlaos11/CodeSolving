def solution(polynomial):
    answer = ''
    정렬 = list(filter(lambda x: 'x' in x, polynomial.split(' ')))
    정렬2 = list(filter(lambda x: 'x' not in x, polynomial.split(' + ')))
    print(정렬2)
    sum = 0
    for i in 정렬2:
        sum += int(i)
    cnt = 0
    for i in 정렬:
        print(i.split('x'))
        compare = i.split('x')[0]
        if compare == '':
            cnt += 1
        else:
            cnt += int(compare)
    print(cnt, sum)

    if cnt == 1 and sum == 0:
        answer = 'x'
    elif cnt == 1 and sum != 0:
        answer = f'x + {sum}'
    elif sum != 0 and cnt != 0:
        answer = f'{cnt}x + {sum}'
    elif cnt != 0 and sum == 0:
        answer = f'{cnt}x'

    elif sum != 0 and cnt == 0:
        answer = f'{sum}'
    elif sum == 0 and cnt == 0:
        answer = ''

    return answer