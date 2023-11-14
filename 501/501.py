from collections import Counter

c = Counter()
root = list(input().split(','))
for v in root:
    c[v] += 1
print(c.most_common(1)[0][0])