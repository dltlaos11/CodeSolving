// name -> yearning을 key, value형태로
// photo순회하면서 check
function solution(name, yearning, photo) {
    var answer = [];
    
    const type = {};
    for(let i=0; i<name.length; i++){
        type[name[i]] = yearning[i];
    }
    console.log(type["may"])
    const result = photo.map((val) => 
                          val.reduce((acc, cur) => {
        return acc + (type[cur] || 0)
    },0)
        
    )
    

    return result;
}