"""
Task: Input format / file processing

1. Reads the graph input file
2. Extracts the vertices from the first line
3. Extracts the directed weighted edges from the remaining lines
4. Prints the parsed result so the team can verify the input was read correctly
"""

def read_graph_input(filename):
    """"
    File format:
    - First line: vertices separated by spaces
      Example: A B C D E
    - Remaining lines: source, destination, weight
      Example: A, B, 18
    Returns:
        vertices: list of strings
        edges: list of tuples (source, destination, weight)
    """
    with open(filename, "r") as file:
        lines = [line.strip() for line in file if line.strip()]

    # First line contains the vertices
    vertices = lines[0].split()

    # Remaining lines contain edges
    edges = []
    for line in lines[1:]:
        parts = [part.strip() for part in line.split(",")]
        source = parts[0]
        destination = parts[1]
        weight = int(parts[2])
        edges.append((source, destination, weight))

    return vertices, edges


def print_parsed_input(vertices, edges):
    #Prints the parsed vertices and edges clearly.
    print("Vertices array:")
    print(vertices)
    print()

    print("Edges read from file:")
    for source, destination, weight in edges:
        print(f"({source}, {destination}, {weight})")


def main():
    filename = "input.txt"
    vertices, edges = read_graph_input(filename)
    print_parsed_input(vertices, edges)


if __name__ == "__main__":
    main()