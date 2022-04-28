def strangeCounter(t):
    # Write your code here
    time = 3
    while (1):
        t = t-time
        if t <= 0:
            t = t+time
            return time - t + 1
        time = time*2