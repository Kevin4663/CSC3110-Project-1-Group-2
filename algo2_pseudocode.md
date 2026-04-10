### Pseudocode for algorithim2

**Algorithm:** `algorithim2(f)`
**Input:** A file object `f` containing graph data

1.  **Initialize Data**
    - Set `lines` to an empty list.
    - **For each** `line` in `f`:
      - **If** `line.strip()` is not empty:
        - Append `line.strip()` to `lines`.

2.  **Map Vertices**
    - `vertices` $\leftarrow$ split the first element of `lines` by whitespace.
    - Initialize an empty dictionary `vertex_dict`.
    - Set `n` to 0.
    - **For each** `v` in `vertices`:
      - `vertex_dict[v]` $\leftarrow n$
      - Increment `n` by 1.

3.  **Initialize Matrix**
    - Initialize `adj_matrix` as an empty list.
    - **Repeat** for the number of `vertices`:
      - Create an empty list `row`.
      - **Repeat** for the number of `vertices`:
        - Append `-999` to `row`.
      - Append `row` to `adj_matrix`.

4.  **Populate Matrix**
    - **For each** `edge` in `lines` (skipping the first line):
      - `rule` $\leftarrow$ split `edge` by commas.
      - `start` $\leftarrow$ `rule[0]` stripped.
      - `end` $\leftarrow$ `rule[1]` stripped.
      - `weight` $\leftarrow$ `rule[2]` stripped.
      - `row` $\leftarrow$ `vertex_dict[start]`.
      - `col` $\leftarrow$ `vertex_dict[end]`.
      - `adj_matrix[row][col]` $\leftarrow$ integer value of `weight`.

5.  **Output**
    - Print `vertices`.
    - Print "matrix =".
    - **For each** `row` in `adj_matrix`:
      - Print `row`.
