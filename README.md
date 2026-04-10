# CSC3110 Project 1 - Group 2

Wayne State University  
CSC 3110 - Algorithm Design and Analysis  
Winter 2026 Term Project

## Group Members
- Evangeline Strye
- Kevin Hin
- Muhammad Bazzi
- Nahyun Kim
- Yanyan Cai

## Project Goal
Our team selected **Project 1**. The goal of this project is to read a graph input file and store it in an **adjacency matrix**.

The input includes:
- a list of vertices
- directed weighted edges

The output of the program includes:
- the **vertices array**
- the **adjacency matrix**

Since this project follows the course rubric, it is not just one code file. Our team also prepared the required pseudocode, analysis, and supporting files.

## Algorithm Direction
Because we are working on Project 1, we decided to use two different algorithms that solve the same problem in different ways.

**Algorithm 1:**  
Reads the input and, for each edge, finds the row and column index by checking the vertices list one by one.

**Algorithm 2:**  
Reads the input and first builds a dictionary (hash map), so each vertex can be matched to an index directly.

We chose these two approaches because:
- both solve the same problem
- both produce the same adjacency matrix
- the difference between them is clear
- their efficiency can be compared more easily

## Task Distribution

### Muhammad Bazzi - Input Format / File Processing
**Responsibilities:**
- Understand the input format
- Prepare sample input file(s)
- Handle reading the input file
- Extract the list of vertices from the first line
- Help test whether the input file is being read correctly

**Deliverables:**
- input file(s)
- input format explanation
- code for reading vertices and input structure

---

### Evangeline Strye - Matrix Setup / Output Format
**Responsibilities:**
- Create the adjacency matrix
- Initialize all values to `-999`
- Make sure the matrix size is correct
- Help create the output format
- Print the vertices and matrix clearly

**Deliverables:**
- matrix creation function
- matrix initialization code
- output / printing function

---

### Yanyan Cai - Algorithm 1
**Responsibilities:**
- Implement Algorithm 1
- Use sequential search on the vertices list
- Make sure the result is correct
- Write the pseudocode for Algorithm 1
- Write a short explanation of how Algorithm 1 works

**Deliverables:**
- Algorithm 1 code
- Algorithm 1 pseudocode
- short written explanation

---

### Kevin Hin - Algorithm 2
**Responsibilities:**
- Implement Algorithm 2
- Use a dictionary / hash map to find indices
- Make sure the result matches Algorithm 1
- Write the pseudocode for Algorithm 2
- Write a short explanation of how Algorithm 2 works

**Deliverables:**
- Algorithm 2 code
- Algorithm 2 pseudocode
- short written explanation

---

### Nahyun Kim - Analysis / Organization / Final Merge
**Responsibilities:**
- Compare the two algorithms
- Write the difference section
- Write the asymptotic analysis section
- Help combine everyone’s work
- Organize the final project files before submission

**Deliverables:**
- difference between the two algorithms
- time complexity analysis
- merged final project materials