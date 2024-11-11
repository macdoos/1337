f = open('input','r')
content = f.readlines()
l = [s.replace("\n", "") for s in content]

h = 0
d = 0
a = 0

for x in l:
    if x.split()[0] == "down":
        a += int(x.split()[1])
    elif x.split()[0] == "up":
        a -= int(x.split()[1])
    else:
        h += int(x.split()[1])
        y = a*int(x.split()[1])
        d+=y
            
print(h*d)
