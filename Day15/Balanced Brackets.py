def isBalanced(s):
    # Write your code here
    stack = []
    db = {'{':'}','(':')','[':']'}
    
    for char in s:
        if char in ['{','(','[']:
            stack.append(char)
            print(stack)
        else:
            if stack:
                top = stack.pop()
                if db[top] != char:
                    return 'NO'
                    break
                            
    return "NO" if stack else "YES"