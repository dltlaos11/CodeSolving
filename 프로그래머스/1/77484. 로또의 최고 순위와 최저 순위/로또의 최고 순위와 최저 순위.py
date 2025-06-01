def solution(lottos, win_nums):
    answer = []
    chk_content = [6, 6, 5, 4, 3, 2, 1]  # 인덱스 0~6에 대한 등수 매핑

    cnt = 0
    zero_cnt = 0

    # 맞힌 번호와 0의 개수를 계산
    for num in lottos:
        if num in win_nums:
            cnt += 1
        if num == 0:
            zero_cnt += 1

    min_rank = chk_content[cnt]
    max_rank = chk_content[cnt + zero_cnt]

    answer.append(max_rank)
    answer.append(min_rank)

    return answer