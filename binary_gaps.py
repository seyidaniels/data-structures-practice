def binaryGaps(number):
    binaryRep = str(bin(number))[2:]
    gap = 0
    maxGap = 0
    for symbol in binaryRep:
        if symbol == '0':
            gap += 1
        else:
            if gap > maxGap:
                maxGap = gap
            gap = 0
    return maxGap


b = binaryGaps(529)
print(b)
# 529 / 2 = 264r1
# 264 / 2 = 132r0
# 132 / 2 = 66r0
# 66 / 2 = 33r0
# 33 / 2 = 16r1
# 16 / 2 = 8r0
# 8 / 2 = 4r0
# 4 / 2 = 2r0
# 2 / 2 = 1r0
# 1 / 2 = 0r1

32 / 2
