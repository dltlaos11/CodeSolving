def solution(picks, minerals):
    ans = []
    tired = [[1, 1, 1],
             [5, 1, 1],
             [25, 5, 1]]
    idx = {"diamond": 0, "iron": 1, "stone": 2}
    
    def dfs(picks, minerals, tired_rate):
        
        if sum(picks) == 0 or minerals == []:
            ans.append(tired_rate)
            return
        
        tmp = minerals[:5]
        
        for i in range(3):
            if picks[i] > 0:
                picks[i] -= 1
                tmp_tired_rate = calc_tired_rate(i, tmp)
                dfs(picks, minerals[5:], tmp_tired_rate+tired_rate)
                picks[i] += 1
            
    def calc_tired_rate(i, minerals):
        tired_rate = 0
        
        for m in minerals:
            tired_rate += tired[i][idx[m]]
        return tired_rate
    
    dfs(picks, minerals, 0)
    ans.sort()
    
    return ans[0]