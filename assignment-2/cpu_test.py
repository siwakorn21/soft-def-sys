import  time

# TESTING
n = 50000
result = []

for i in range(n):
    result.append(time.time_ns())

# WRITE FILE
f = open('result-2.txt', 'w')
f.write(f'{0}, {0 / 10**9} \n')
for i in range(1, len(result)):
    f.write(f'{i}, {(result[i] - result[0]) / (10 ** 9)} \n')
f.close()
