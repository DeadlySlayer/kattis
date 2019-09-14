
x = []
results = []

for i in range(5):
    x.append(input())

for i in range(5):
    scores = x[i].split(" ")
    for i in range(4):
        scores[i] = int(scores[i])
    sumScore = sum(scores)
    results.append(sumScore)

# print(results)
maximum = max(results)
position = results.index(maximum)
print(position+1, maximum)