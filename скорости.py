# график лучевых скоростей (дата, скорость)
import matplotlib.pyplot as plt

with open("PZ Mon_v_radial(1).dat", 'r') as f:
    lines = [line.strip() for line in f]
    l=len(lines)
    x = []
    y = []
    for j in range(1, len(lines)):
        for m in range(len(lines[j])):
            if lines[j][m] == " ":
                a=int(lines[j].index(lines[j][m]))
                data = lines[j][0:a]
                x.append(float(data))
                v = lines[j][a:l]
                y.append(float(v))
                break

print(x)
print(y)
plt.scatter(x, y)
plt.title('PZ Mon_v_radial')
plt.xlabel('mjd 24...')
plt.ylabel('vr')
plt.show()
