function findSum(array) {
    return array.reduce(function(total, sum) {
        return total + sum
    }, 0);
}


function isPossible(calCounts, requiredCals) {
    // Write your code here
    let list = [];
    let sum = 0;
    let isP = false;

    function lessThanReq(n) {
        return n < requiredCals
    }
    calCounts = calCounts.filter(lessThanReq);
    for (let i = 1; i < calCounts.length; i++) {
        let array = calCounts.slice(i - 1, i + 1);
        sum = findSum(array)
        if (sum == requiredCals) return true;
        if (sum < requiredCals) {
            let minus = requiredCals - sum;
            if (calCounts.includes(minus)) {
                isP = true;
            }
        }
    }
    return isP;

}

d = isPossible([2, 9, 5, 1, 6], 12)
console.log(d)