
with open("input.txt") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines if line.strip()]

vertices = lines[0].split()

edges = []
for line in lines[1:]:
    parts = line.split(',')
    u = parts[0].strip()
    v = parts[1].strip()
    w = int(parts[2].strip())
    edges.append((u, v, w))

n = len(vertices)
matrix = [[-999] * n for _ in range(n)]

for u, v, w in edges:
    
    i = -1
    for idx in range(n):
        if vertices[idx] == u:
            i = idx
            break

    j = -1
    for idx in range(n):
        if vertices[idx] == v:
            j = idx
            break

    if i != -1 and j != -1:
        matrix[i][j] = w

print(f"vertices = {vertices}")
print("matrix =")
for row in matrix:
    print(row)