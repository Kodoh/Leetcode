T = int(input())
results = []

for j in range(T):
    N = int(input())

    pyramid = []
    for i in range(N):
        row = list(map(int, input().split()))
        pyramid.append(row)
        
    level = len(pyramid) - 2
    while level >= 0:
        for i in range(len(pyramid[level])):
            pyramid[level][i] += max(pyramid[level+1][i], pyramid[level+1][i+1])
        level -= 1
            
    results.append(pyramid[0][0])

for result in results:
    print(result)
