def csSquareAllDigits(n):
    listedNums = [int(x) for x in str(n)]

    squaredList = [x**2 for x in listedNums]

    listToString = [str(integer) for integer in squaredList]
    squaredString = "".join(listToString)
    squaredInteger = int(squaredString)

    return squaredInteger

print(csSquareAllDigits(36))