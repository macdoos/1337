import matplotlib.pyplot as plt

f = open('input','r')
content = f.readlines()
l = [s.replace("\n", "") for s in content]

x1s = []
x2s = []
y1s = []
y2s = []

for i in range(len(l)):
    x1 = l[i].split(" -> ")[0].split(',')[0]
    x2 = l[i].split(" -> ")[1].split(',')[0]
    x1s.append(x1)
    x2s.append(x2)

for i in range(len(l)):
    y1 = l[i].split(" -> ")[0].split(',')[1]
    y2 = l[i].split(" -> ")[1].split(',')[1]
    y1s.append(y1)
    y2s.append(y2)

# x axis values
#x = [0,int(x1s[0])]
# corresponding y axis values
#y = [0,int(y1s[0])]

# plotting the points
plt.plot(x1s, y1s, label= "stars", marker= "*")
plt.plot(x2s, y2s, label= "stars", marker= "*", color="red", alpha=0.7)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('aoc')
plt.legend()

# function to show the plot
plt.show()
