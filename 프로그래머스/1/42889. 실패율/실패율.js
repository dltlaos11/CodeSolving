function solution(N, stages) {
    var answer = [];
    let fail = [];
    let cnter = 0;
    for(let i =1; i<N+1;i++){
        let cnt =0;
        for(let j=0;j<stages.length;j++){
            if(stages[j] === i){
                cnt=cnt+1      
            }
        }
        
        cnter =cnter + cnt;
        if (i === 1){
            fail.push({fir: i,sec:cnt/stages.length,thr: cnter})
            }

        if(i !== 1) {
            fail.push({fir: i,sec: cnt/(stages.length-fail[i-2].thr),thr: cnter});
        }
    }

    fail.sort(function(a, b)  {
        return b.sec - a.sec;
    });
    for(let q=0;q<N;q++){
        answer.push(fail[q].fir)
    }
    return answer;
}