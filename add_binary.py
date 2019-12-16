
def addBinary(a, b):
    i = max(len(a), len(b))
    carry = 0
    finalSum = []
    a = a.zfill(i)
    b = b.zfill(i)
    i = i - 1
    while i >= 0:
        val1 = int(a[i])
        val2 = int(b[i])
        carry, singleSum = divmod((val1+val2+carry), 2)
        finalSum.insert(0, str(singleSum))
        i -= 1
    if carry != 0:
        finalSum.insert(0, str(carry))
    final = ''
    return final.join(finalSum)


s = addBinary('1011', '111')
print(s)
