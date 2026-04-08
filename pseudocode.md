# Algorithm 1 
## Pseudocode

n ← length(vertices)
create matrix[n][n]

for i from 0 to n-1
    for j from 0 to n-1
        matrix[i][j] ← -999

for each (u, v, w) in edges
    i ← -1
    for k from 0 to n-1
        if vertices[k] == u
            i ← k
            break

    j ← -1
    for k from 0 to n-1
        if vertices[k] == v
            j ← k
            break

    if i ≠ -1 AND j ≠ -1
        matrix[i][j] ← w
return matrix


Explanation
The algorithm initializes an n × n matrix with a default value (-999).
For each edge (u, v, w), it searches for the indices of vertices u and v.
Sequential search is used to find indices in the vertices list.
If both vertices are found, the corresponding matrix entry is updated.
The algorithm processes edges one by one without using additional data structures.

Time Complexity
Each edge requires searching through the vertex list.
Searching takes O(V) time.
For E edges, the total time complexity is:

O(E · V)
