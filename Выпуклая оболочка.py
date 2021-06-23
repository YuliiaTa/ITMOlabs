import math
import matplotlib.pyplot as plt

def angle_direction(A, B, C):
    return (B[0] - A[0]) * (C[1] - B[1]) - (B[1] - A[1]) * (C[0] - B[0])

with open("convex.csv", 'r') as fp:
    lines = fp.readlines()
in_data = [ int(x) for x in lines[14].strip().split(";") ]
points = []
xMin = 0
nMin = 0
i = 1
while i < len(in_data):
    if in_data[i-1] == 0:
        if in_data[i] > 0:
            alpha = 90
        elif in_data[i] < 0:
            alpha = 270
        else:
            alpha = 0
    else:
        alpha = math.degrees(math.atan(in_data[i] / in_data[i-1]))
        if in_data[i-1] < 0:
           alpha += 180
        elif in_data[i] < 0:
           alpha += 360

    points.append(( in_data[i-1], in_data[i], alpha ))
    if xMin > in_data[i-1] + in_data[i]:
        xMin = in_data[i-1] + in_data[i]
        nMin = i // 2
    i += 2

points[0], points[nMin] = points[nMin], points[0]

n = len(points)
for i in range(2,n):
    j = i
    while j > 1 and (angle_direction(points[0], points[j-1], points[j]) < 0):
        points[j-1], points[j] = points[j], points[j-1]
        j -= 1

fig = [points[0], points[1]]
for i in range(2, n):
    while angle_direction(fig[-2], fig[-1], points[i]) <= 0:
        fig.pop(-1)
    fig.append(points[i])
fig.append(points[0])



x = [ p[0] for p in points ]
y = [ p[1] for p in points ]
plt.scatter(x, y)

x = [ p[0] for p in fig ]
y = [ p[1] for p in fig ]
plt.plot(x, y)
plt.show()

fig.pop(-1)
print(fig)
with open("out_angles.csv", 'w') as fp:
    fp.write("X,Y\n")
    for j in range(len(fig)):
        aMin = 400
        nMin = 1000
        for i in range(j, len(fig)):
            if aMin > fig[i][2]:
                aMin = fig[i][2]
                nMin = i
        fig[nMin], fig[j] = fig[j], fig[nMin]
        fp.write(str(fig[j][0]) + "," + str(fig[j][1]) + "\n")