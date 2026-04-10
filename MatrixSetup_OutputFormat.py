# MatrixSetup_OutputFormat.py

def createMatrix(v): #v for list of vertices
    
    #initialization
    row1 = []
    for i in v: #create row with the same length as v
        row1.append(-999) #set all values to -999

    mat = []
    for i in v: #create as many rows as the length of v
        mat.append(row1.copy()) 

    return mat

def printMatrix(v, mat): #given the list of vertices, v , and a matrix, mat
    #printing/formatting
    print(f"vertices = {v}")
    print("matrix =")
    for row in mat:
        print(row)






