# Analysis of Algorithm 1 and Algorithm 2

## Overview
This project reads a directed weighted graph from an input file and stores it in an adjacency matrix.  
Both Algorithm 1 and Algorithm 2 solve the same problem and give the same final matrix.  
The main difference is how each algorithm finds the position of each vertex in the matrix.

## Algorithm 1
Algorithm 1 uses `sequential search`.  
For each edge `(u, v, w)`, where `u` is the starting vertex, `v` is the ending vertex, and `w` is the weight, the algorithm goes through the vertices list one by one to find the index of `u` and the index of `v`. It then uses those two indices as the row and column of the matrix, and stores `w` in `matrix[i][j]`.

This method is simple and easy to follow, but it can be slower because it keeps searching through the vertices list again and again for every edge.

## Algorithm 2
Algorithm 2 uses a dictionary.  
Before filling the matrix, it makes a dictionary that matches each vertex to its index.

For example:
vertex_dict = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4
}

Then for each edge, it can directly find the row and column index without searching through the whole vertices list.

This makes Algorithm 2 faster than Algorithm 1, especially when the graph gets bigger.

## Difference Between the Algorithms
The biggest difference is how they find the index of a vertex.

- Algorithm 1 searches the vertices list `one by one`.
- Algorithm 2 uses a `dictionary` to get the index directly.

Both algorithms make the same adjacency matrix, but Algorithm 2 avoids repeated searching.

## Time Complexity

Let:
- `V` = number of vertices
- `E` = number of edges

### Algorithm 1
For Algorithm 1, each edge needs the program to look through the vertices list to find where the start vertex and end vertex are.

- Finding `u` takes `O(V)`
- Finding `v` takes `O(V)`

So for one edge, it takes about `O(V)` time overall.

Since there are `E` edges, processing all edges takes:
- `O(EV)`

Also, making the adjacency matrix itself takes:
- `O(V^2)`

So the total time complexity is:
- **O(V^2 + EV)**

### Algorithm 2
Algorithm 2 first makes a dictionary that matches each vertex to its index, and this takes `O(V)` time.

After that, when the program reads each edge, it can find the row and column index much faster by using the dictionary instead of searching the whole vertices list.

So processing all edges takes:
- `O(E)`

Also, creating the adjacency matrix takes:
- `O(V^2)`

So the total time complexity is:
- **O(V^2 + V + E)**

Since `V^2` is bigger than `V`, this can be simplified to:
- **O(V^2 + E)**

## Space Complexity
Both algorithms need an adjacency matrix, and that already takes `O(V^2)` space.

Algorithm 1 does not use much more memory other than the matrix.

Algorithm 2 uses one more dictionary, which takes `O(V)` space.

So Algorithm 2 uses a little more extra memory, but the matrix is still much bigger.  
That is why both algorithms are mainly `O(V^2)` in space.

## Conclusion
Both algorithms solve the problem correctly and create the same adjacency matrix.  
Algorithm 1 is easier to understand because it just searches the list directly.  
Algorithm 2 is more efficient because it uses a dictionary and does not need to keep searching the list.  
So for bigger graphs, Algorithm 2 is the better choice.