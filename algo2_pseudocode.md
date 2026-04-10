# Algorithm 2

## Pseudocode

n ← length(vertices)
vertex_dict ← empty hash map

for k from 0 to n-1
vertex_dict[vertices[k]] ← k

create matrix[n][n]
for i from 0 to n-1
for j from 0 to n-1
matrix[i][j] ← -999

for each (u, v, w) in edges
i ← vertex_dict[u]
j ← vertex_dict[v]
matrix[i][j] ← w

return matrix

## Explanation

- The algorithm initializes an $n \times n$ matrix with a default value of -999 to represent infinity.
- A hash map (dictionary) is constructed to map each vertex name directly to its integer index.
- Instead of a sequential search, the algorithm uses this map to find row and column indices in constant time.
- Each edge (u, v, w) is processed by retrieving indices directly from the dictionary.
- This approach produces the same adjacency matrix as Algorithm 1 but improves indexing efficiency.

## Time Complexity

- Building the hash map requires a single pass through the vertex list, taking $O(V)$ time.
- Processing each edge requires hash map lookups, which take $O(1)$ time on average.
- For $E$ edges and $V$ vertices, the total time complexity is:

$$O(V + E)$$
