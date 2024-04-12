import sys
input = sys.stdin.read

def is_not_carry(sum_val, target):
    while sum_val > 0 or target > 0:
        num1 = sum_val % 10
        num2 = target % 10
        if num1 + num2 >= 10:
            return False
        sum_val //= 10
        target //= 10
    return True

def backtracking(count, depth, sum_val):
    global result
    result = max(result, count)

    if depth == n:
        return

    for i in range(depth, n):
        if is_not_carry(sum_val, arr[i]):
            backtracking(count + 1, i + 1, sum_val + arr[i])

if __name__ == "__main__":
    data = input().split()
    n = int(data[0])
    arr = list(map(int, data[1:n+1]))

    result = 0
    backtracking(0, 0, 0)
    print(result)