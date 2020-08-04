function single(numbers) {
    for (let i = 0; i < numbers.length; i++) {
        for (let j = i + 1; j < numbers.length; j++) {
            if (numbers[i] != numbers[j]) {
                console.log(numbers[j]);
            }
        }
    }
}

single([5, 1, 1, 5, 6]);