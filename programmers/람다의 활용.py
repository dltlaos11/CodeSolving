def solution(score):
    # map_arr = list(map(lambda x: x[0] + x[1], score))
    # sorted_arr = sorted(list(map(lambda x: x[0] + x[1], score)), reverse=True);
    # return (list(map(lambda x: sorted_arr.index(x) + 1, map_arr)))
    정렬된_변수 = sorted([sum(i) for i in score], reverse=True)
    return list(정렬된_변수.index(sum(j)) + 1 for j in score)
