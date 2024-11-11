l = [int(x) for x in open('input')]

count = 0 

for i in range(len(l)):
    if i>=3 and l[i]+l[i-1]+l[i-2] > l[i-1]+l[i-2]+l[i-3]:
        count += 1

print(count)
