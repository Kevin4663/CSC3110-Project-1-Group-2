# CSC3110-Project-1-Group-2
Wayne State University CSC 3110 Algorithm Design and Analysis Winter 2026 Term Project 
# Group Members
* Evangeline Strye
* Kevin Hin
* Muhammad Bazzi
* Nahyun Kim
* Yanyan Cai

# **Project Goal**

Our team selected **Project 1**. The goal of this project is to read a graph input and store it in an **`adjacency matrix`**

The input includes:

- a list of vertices
- directed weighted edges

The program output should include:

- the **vertices array**
- the **adjacency matrix**

We also need to complete the project based on the rubric, which means this is **not just one code file**. We need to prepare all required parts as a team.

## **Suggested Algorithm Direction**

Since we are doing Project 1, a good way to create two different algorithms is:

**Algorithm 1:** Read the input and, for each edge, find the row and column index by scanning the vertices list one by one.

**Algorithm 2:** Read the input and build a dictionary/hash map first, so each vertex can be matched to an index directly.

This way:

- both algorithms solve the same problem
- both produce the same adjacency matrix
- the difference is clear
- the efficiency difference is easier to explain

## **Task Distribution**

### Muhammad Bazzi – Input Format / File Processing

**Responsibilities:**

- Understand the input format
- Prepare sample input file(s)
- Handle reading the input file
- Extract the list of vertices from the first line
- Help test whether the file is being read correctly

**Deliverables:**

- input file(s)
- input format explanation
- code for reading vertices / input structure

---

### **Evangeline Strye – Matrix Setup / Output Format**

**Responsibilities:**

- Create the adjacency matrix
- Initialize all values to -999
- Make sure the matrix size is correct
- Help create the output format
- Print vertices and matrix clearly

**Deliverables:**

- matrix creation function
- matrix initialization code
- output / printing function

---

### **Yanyan Cai – Algorithm 1**

**Responsibilities:**

- Implement Algorithm 1
- Use sequential search on the vertices list
- Make sure the result is correct
- Write the pseudocode for Algorithm 1
- Write a short explanation of how Algorithm 1 works
- Algorithm 1 code
- Algorithm 1 pseudocode

**Deliverables:**

- short written explanation

---

### **Kevin Hin – Algorithm 2**

**Responsibilities:**

- Implement Algorithm 2
- Use dictionary / hash map to find indices
- Make sure the result matches Algorithm 1
- Write the pseudocode for Algorithm 2
- Write a short explanation of how Algorithm 2 works

**Deliverables:**

- Algorithm 2 code
- Algorithm 2 pseudocode
- short written explanation

---

### **Nahyun Kim - Member 5 – Analysis / Organization / Final Merge**

**Responsibilities:**

- Compare the two algorithms
- Write the difference section
- Write the asymptotic analysis section
- Help combine everyone’s work
- Organize the final files before submission

**Deliverables:**

- difference between algorithms
- time complexity analysis
- merged final project materials
