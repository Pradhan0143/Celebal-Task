def getTotalX(a, b):
    # Write your code here
    ma = max(a)
    mb = min(b)
    count = 0
    for n in range(ma, mb + 1):
        left = all([n % nA == 0 for nA in a])
        right = all([nB % n == 0 for nB in b])
        count += left * right
    return count