def solution(genres, plays):
    answer = []
    
    # {장르1: [[노래1 재생 횟수 :노래1 고유 번호],[노래2 재생 횟수: 노래2 고유번호]...]}
    dic={}
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]].append([plays[i],i])
        else : 
            dic[genres[i]] = [[plays[i],i]]
    print(dic)

    # {장르 1 : 모든 장르1의 총 재생 횟수 ,장르 2 : 모든 장르2의 총 재생 횟수...}
    genre_rank ={}
    for genre in dic.keys():
        songs = dic[genre]
        plays_sum = 0
        for song in songs:
            plays_sum+=song[0]
        genre_rank[genre] = plays_sum
    # 장르별 총 재생 횟수가 큰 순으로 정렬 
    genre_rank = sorted(genre_rank.items(), key=lambda x: x[1],reverse=True)
    print(genre_rank)
    
    for genre in genre_rank:
        # 장르별 높은 재생수, 낮은 고유번호 순으로 정렬 내림차순
        song_rank=sorted(dic[genre[0]], key=lambda x:(x[0],-x[1]),reverse=True)
        best_two = 0

        for song in song_rank:
            answer.append(song[1])
            best_two +=1
            if best_two == 2:
                break
    
    return answer
# 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다
# 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.
# 1. 속한 노래가 '많이 재생된 장르'를 먼저 수록합니다.
# 2. 장르 내에서 '많이 재생된 노래'를 먼저 수록합니다.
# 3. 장르 내에서 '재생 횟수가 같은 노래' 중에서는 '고유 번호가 낮은 노래를 먼저' 수록합니다.

# 노래의 장르를 나타내는 문자열 배열 genres
# 노래별 재생 횟수를 나타내는 정수 배열 plays
# 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 