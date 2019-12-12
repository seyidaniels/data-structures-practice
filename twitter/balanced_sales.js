// function balancedSum(sales) {
//     // Write your code here
//     let rightArray = [];
//     let leftArray = [];
//     let rightSum = 0;
//     let leftSum = 0;
//     let index = -1;
//     for (let i = 0, j = sales.length - 1; i < sales.length, j > 0; i++, j--) {
//         leftArray.push(leftSum += sales[i])
//         rightArray.push(rightSum += sales[j])
//     }

//     let intersection = leftArray.filter(value => rightArray.includes(value));

//     return leftArray.findIndex(value => value == intersection[0]) + 1;

// }

function findSum(array) {
    return array.reduce(function(total, sum) {
        return total + sum
    }, 0);
}


function balancedSum(sales) {
    let leftSum = 0
    let rightSum = 0

    for (let i = 0; i < sales.length - 1; i++) {
        leftSum = findSum(sales.slice(0, i));
        rightSum = findSum(sales.slice(i + 1));
        if (rightSum == leftSum) return i;
    }
}



d = balancedSum([1, 2, 1]);
console.log(d);