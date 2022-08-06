const howSum=(targetSum,numbers,memo={})=>{
    if (targetSum in memo) { return memo[targetSum]; }
    if (targetSum==0) return []; 
    if (targetSum<0) return null;

    for (let num of numbers){
        const remainder=targetSum-num;
        //console.log("i=",num, "remainder=",remainder,"targetSum=",targetSum,numbers)
        const remainderResult=howSum(remainder,numbers,memo);
        if (remainderResult!=null) {
            memo[targetSum]= [...remainderResult,num]
            //console.log ("memo[targetSum]",memo[targetSum])
            return memo[targetSum]
        }
    }
    memo[targetSum]=null;
    return null;
}

console.log("howSum(7,[2,3]) ",howSum(7,[2,3]))
console.log ("howSum(7,[5,3,4,7]) ",howSum(7,[5,3,4,7]))
console.log ("howSum(7,[2,4]) ",howSum(7,[2,4]))
console.log ("howSum(8,[2,3,5]) ",howSum(8,[2,3,5]))
console.log ("howSum(8,[3,5,2]) ",howSum(8,[3,5,2]))
console.log ("howSum(300,[7,14]) ",howSum(300,[7,14]) )