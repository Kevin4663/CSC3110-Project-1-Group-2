# Algorithm2.py

INPUT_FILE = "input.txt"

def algorithim2(f):
    lines = []
    for line in f:
        if line.strip(): 
            lines.append(line.strip())


    vertices = lines[0].split() # split by character A B C D E => ['A', 'B', ...]
    vertex_dict = {}
    # build dict
    # {"A":0, "B":1, ...}
    n = 0
    for v in vertices:
         vertex_dict[v] = n
         n+=1
    
    # initialize adj matrix with infinities, -999
    adj_matrix = []
    size = len(vertices)
    for _ in range(size):
        row = [] 
        for _ in range(size):
            row.append(-999)
        adj_matrix.append(row)

    # populate adj matrix
    for edge in lines[1:]: # skip first line
        rule = edge.split(',') # split by commas A, B, 18 => ['A', ' B', ' 18']
        start = rule[0].strip() 
        end = rule[1].strip()
        weight = rule[2].strip()

        row = vertex_dict[start]
        col = vertex_dict[end]

        adj_matrix[row][col] = int(weight)

    print(f"vertices = {vertices}")
    
    print("matrix =")
    for row in adj_matrix:
        print(row)

def main():
    with open(INPUT_FILE) as f:
        algorithim2(f)

if __name__ == "__main__":
        main()
