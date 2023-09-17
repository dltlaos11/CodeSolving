def solution(P, N):
    # P에서 시, 분, 초를 추출하기 위해 문자열을 분리
    judge = P.split(' ')[0]
    time_parts = P.split()[1].split(':')
    hours, minutes, seconds = map(int, time_parts)

    # 시, 분, 초를 초로 변환하여 총 초를 계산
    total_seconds = hours * 3600 + minutes * 60 + seconds

    # 추가할 초(N)를 총 초에 더하기
    total_seconds += N

    # 총 초를 24시간 단위의 시간으로 변환
    total_seconds %= 24 * 3600

    # 변환된 시간을 시, 분, 초로 다시 분리
    hours = total_seconds // 3600
    total_seconds %= 3600
    minutes = total_seconds // 60
    seconds = total_seconds % 60

    if judge == "PM":
        hours += 12
        if hours >= 24:
            hours -= 24
    if judge == "AM":
        if hours >= 12:
            hours -= 12





    # 시, 분, 초를 문자열로 변환하여 24시간 단위 표시로 출력
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


# 예시 테스트 케이스
# print(solution("PM 01:00:00", 10))  # "13:00:10"
print(solution("AM 11:27:35", 0))  # "00:01:00"
