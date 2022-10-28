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


const gridTraveler=(m,n)=>{
    const table=Array(m+1).fill().map(()=>{return Array(n+1).fill(0)})
    console.log (table);

    table[1][1]=1;
    for (let i=0;i<=m;i++){
        for (let j=0;j<=n;j++){
            const current=table[i][j];
            if (j+1<=n) table[i][j+1]+=current;
            if (i+1<=m) table[i+1][j]+=current
        }
    }

    return table[m][n];
}


console.log ("gridTraveler(1,1)",gridTraveler(1,1)); //#1
console.log ( "gridTraveler(2,3)",gridTraveler(2,3));// #3
console.log ("gridTraveler(3,2)",gridTraveler(3,2));// #3
console.log ("gridTraveler(3,3)",gridTraveler(3,3)); //#6
console.log ("gridTraveler(18,18)",gridTraveler(18,18)); //#233360