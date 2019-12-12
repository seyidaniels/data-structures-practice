
data = []
for i in range(100000):
    if i % 2:
        data.append(i)
    else:
        data.insert(0, i)
        # data.append(i)
        # data.reverse()
print(data)
