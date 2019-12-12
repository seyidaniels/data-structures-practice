def getFact(n):
    if (n < 1):
        return
    else:
        getFact(n - 1)
        print("Hello world ", n)


getFact(4)
