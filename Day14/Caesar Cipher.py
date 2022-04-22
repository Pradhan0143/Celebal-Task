def caesarCipher(s, k):
    # Write your code here
    temp = []
    for char in s:
        temp.append(ord(char))
    
    for i in range (n):
        if 65 <= temp[i] <= 90:
            temp[i] = (65 + (temp[i] - 65+k)%26)
        
        elif 97 <= temp[i] <= 122:
            temp[i] = (97 + (temp[i] - 97+k)%26)
            
    return "".join(map(chr, temp))