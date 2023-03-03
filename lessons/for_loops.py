"""demonstrating for loops"""

idx = 0
xs = [1, 2, 3, 4]

while idx < len(xs):
    item = xs[idx]
    print(item)
    idx += 1

for item in xs:
    print(item)

    