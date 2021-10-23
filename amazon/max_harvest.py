def max_harvest(arr, k):
    n = len(arr)
    max_profit = float('-inf')
    # Evaluate all n/2 harvesting options (6 slices->3 options, 4 slices->2 options, and so on)
    for i in range(n // 2):
        sm = 0
        for j in range(k):
            curr_index = i + j
            opposite_index = (curr_index + (
                        n // 2)) % n  # adding n//2 gets us the opposite slice's index. %2 for wrapping around array
            sm += arr[curr_index] + arr[opposite_index]
        max_profit = max(max_profit, sm)
    return max_profit
print(max_harvest([3, -5], 1))  # -2
print(max_harvest([1, 5, 1, 3, 7, -3], 2))  # 16
print(max_harvest([-6, 3, 6, -3], 1))  # 0
