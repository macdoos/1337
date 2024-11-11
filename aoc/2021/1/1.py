f = open('input','r')
content = f.readlines()
l = [s.replace("\n", "") for s in content]
count = 0
c = 0

for i, x in enumerate(l):
    if (i+1 < len(l) and i - 1 >= 0):
        if (x > l[i-1]):
            count += 1
            print(x + " increased")
        else:
            c += 1
            print(x + " decreased")
    else:
        print("N/A")

print(count)
print(c)
