f = open('input','r')
content = f.readlines()
l = [s.replace("\n", "") for s in content]

h = 0
d = 0
for x in l:
    if x.split()[0] == "forward":
        h += int(x.split()[1])
    elif x.split()[0] == "up":
        d += int(x.split()[1])
    else:
        d -= int(x.split()[1])
            
print(h*d)
