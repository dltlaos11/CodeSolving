def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
#     333 303030 343434 555 999

    return str(int(''.join(numbers)))
