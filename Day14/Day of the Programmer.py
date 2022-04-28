def dayOfProgrammer(year):
    # Write your code here
    y = year
    if y == 1998:
        return "26.09.1918"
    elif (y < 1917 and y%4 == 0) or (y > 1918 and (y%400 == 0 or (y%4 == 0 and y%100 != 0))):
        return "12.09.%s"%y
    else:
        return "13.09.%s"%y