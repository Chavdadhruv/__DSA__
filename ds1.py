# # linear array,linkedlist,stacks,queues,hashing
# # non linear trees,graph

# # array stores multiple items of same types
# # memory location continues +4,+4,+4,+4
# # 10,14,18,22,26   array has fix size

# # problem memory westage,homogeneous[same types][flexibility lack]
# # solve this use refrentioal array using address you can put all types in
# # 1 array and store there address in other array [it is slow then array]


# # problem 2 fix size convert this into dynamic size
# # for solve fix error double array size it is called 
# # dynamic array python list is also dynamic array

# Array - Algorithms
# 1. Creating an Array: [1, 2, 3, 4, 5]
# 2. Iterate through Array: [1, 2, 3, 4, 5]
# 3. Get an Element: 3
# 4. Search an Element: 2 found at index 1
# 5. Insert Element(s): [1, 2, 10, 3, 4, 5]
# 6. Delete Element(s): [1, 2, 3, 4, 5]
# 7. Filter an Array: [2, 4]
# 8. Fetch a Sub-Array: [2, 3]
# 9. Merging Arrays: [1, 2, 3] + [4, 5] = [1, 2, 3, 4, 5]
# 10. Reverse Array: [5, 4, 3, 2, 1]
# 11. Rotate Array: [4, 5, 1, 2, 3]

# Linked List - Algorithms [1]
# 1. Creating a Linked List: 1 -> 2 -> 3 -> 4
# 2. Iterate through Linked List: [1, 2, 3, 4]
# 3. Get an Element: 3
# 4. Find an Element: 2 found
# 5. Insert Element(s) At Start: 0 -> 1 -> 2 -> 3 -> 4
# 6. Insert Element(s) At End: 1 -> 2 -> 3 -> 4 -> 5
# 7. Insert Element(s) At Anywhere: 1 -> 2 -> 10 -> 3 -> 4

# Linked List - Algorithms [2]
# 1. Delete Element(s) From Start: 2 -> 3 -> 4
# 2. Delete Element(s) From End: 1 -> 2 -> 3
# 3. Delete Element(s) From Anywhere: 1 -> 3
# 4. IsEmpty: False
# 5. Merging Linked Lists: 1 -> 2 -> 3 + 4 -> 5 -> 6 = 1 -> 2 -> 3 -> 4 -> 5 -> 6
# 6. Reverse Linked List: 4 -> 3 -> 2 -> 1
# 7. Check for Cycles: No cycle detected

# Stack - Algorithms
# 1. Push: [1, 2, 3] after pushing 4
# 2. Pop: [1, 2] after popping 3
# 3. IsEmpty: False
# 4. IsFull: False (assuming a fixed size stack)
# 5. Peek: 3

# Queue - Algorithms
# 1. Enqueue: [1, 2, 3] after enqueueing 4
# 2. Dequeue: [2, 3] after dequeuing 1
# 3. IsEmpty: False
# 4. IsFull: False (assuming a fixed size queue)
# 5. Peek: 1

# Hash Table - Algorithms
# 1. Hash Function (Division Method): Hash of 10 is 0
# 2. Hash Function (Multiplication Method): Hash of 10 is 2
# 3. Hash Function (Universal Hashing): Hash of 10 is 3
# 4. Collision Resolution (Open Addressing): Inserted 10, 20, 30 into table
# 5. Collision Resolution (Linear Probing): Resolved collision with linear probing
# 6. Collision Resolution (Quadratic Probing): Resolved collision with quadratic probing
# 7. Collision Resolution (Double Hashing): Resolved collision with double hashing

# Tree - Algorithms
# 1. Traversal (In Order): [1, 2, 3, 4, 5]
# 2. Height of a Node/Tree: Height is 2
# 3. Depth of a Node: Depth of node 3 is 1
# 4. Degree of a Node: Degree of node 2 is 2
# 5. Insert: Tree after inserting 6: 1 -> 2 -> 3 -> 4 -> 5 -> 6
# 6. Delete: Tree after deleting 3: 1 -> 2 -> 4 -> 5 -> 6

# Heap - Algorithms
# 1. Heapify: [1, 3, 5, 4, 8] transformed into a heap
# 2. Insert Element: [1, 3, 5, 4, 8, 9] after inserting 9
# 3. Delete Element: [1, 3, 5, 8, 9] after deleting root
# 4. Peek (Max/Min Element): 9 (Max Heap)
# 5. Extract (Max/Min Element): 9 extracted, new heap is [1, 3, 5, 8]

# Graph - Algorithms [1]
# 1. Adjacency Matrix: [[0, 1], [1, 0]]
# 2. Add Edge: Added edge (1, 2)
# 3. Remove Edge: Removed edge (1, 2)
# 4. Adjacency List: {1: [2], 2: [1]}
# 5. Add Edge: Added edge (1, 2)
# 6. Remove Edge: Removed edge (1, 2)
# 7. Traverse Nodes (DFS): [1, 2]
# 8. Traverse Nodes (BFS): [1, 2]

# Graph - Algorithms [2]
# 1. Dijkstra's Algorithm: Shortest path [0, 1, 2] with distances [0, 1, 2]
# 2. Floyd-Warshall Algorithm: Shortest paths matrix [[0, 1], [1, 0]]
# 3. Bellman Ford Algorithm: Shortest path [0, 1, 2] with distances [0, 1, 2]
# 4. Kruskal's Algorithm: Minimum Spanning Tree [[0, 1], [1, 2]]
# 5. Prim's Algorithm: Minimum Spanning Tree [[0, 1], [1, 2]]

# Graph - Algorithms [3]
# 1. Check connectivity b/w nodes: Graph is connected
# 2. Find all paths: [0 -> 1 -> 2, 0 -> 2]
# 3. Articulation points: [1]
# 4. Bridges: [0 -> 1]
# 5. Hamiltonian Path: [0 -> 1 -> 2]
# 6. Hamiltonian Cycle: [0 -> 1 -> 2 -> 0]
# 7. Eulerian Path: [0 -> 1 -> 2]
# 8. Eulerian Cycle: [0 -> 1 -> 2 -> 0]
# 9. Find # of islands: 2 islands
# 10. Transitive Closure: [[True, True], [True, True]]

# Graph - Algorithms [4]
# 1. Graph Cycle: Detected
# 2. Topological Sorting: [1, 2, 3]
# 3. Find all topological sorting: [1, 2, 3], [1, 3, 2]
# 4. Kahn's Algorithm: [1, 2, 3]
# 5. Longest Path: [0 -> 1 -> 2] with length 2
# 6. Ford-Fulkerson Algorithm: Maximum flow 5
# 7. Edmonds-Karp Algorithm: Maximum flow 5
# 8. Dinic's Algorithm: Maximum flow 5

# Search Algorithms
# 1. Linear Search: Found 5 at index 2
# 2. Jump Search: Found 5 at index 2
# 3. Binary Search: Found 5 at index 2
# 4. Interpolation Search: Found 5 at index 2
# 5. Exponential Search: Found 5 at index 2
# 6. Ternary Search: Found 5 at index 2

# Sorting Algorithms [1]
# 1. Bubble Sort: [1, 2, 5, 5, 6, 9]
# 2. Selection Sort: [1, 2, 5, 5, 6, 9]
# 3. Insertion Sort: [1, 2, 5, 5, 6, 9]
# 4. Merge Sort: [1, 2, 5, 5, 6, 9]
# 5. Quick Sort: [1, 2, 5, 5, 6, 9]

# Sorting Algorithms [2]
# 1. Binary Insertion Sort: [1, 2, 5, 5, 6, 9]
# 2. 3-way Merge Sort: [1, 2, 5, 5, 6, 9]
# 3. 3-way Quick Sort: [1, 2, 5, 5, 6, 9]
# 4. Counting Sort: [1, 2, 5, 5, 6, 9]
# 5. Radix Sort: [1, 2, 5, 5, 6, 9]
# 6. Bucket Sort: [1, 2, 5, 5, 6, 9]
# 7. Heap Sort: [1, 2, 5, 5, 6, 9]
# 8. Shell Sort: [1, 2, 5, 5, 6, 9]

# Sorting Algorithms [3]
# 1. Tim Sort: [1, 2, 5, 5, 6, 9]
# 2. Odd-Even Sort: [1, 2, 5, 5, 6, 9]
# 3. Comb Sort: [1, 2, 5, 5, 6, 9]
# 4. Cocktail Sort: [1, 2, 5, 5, 6, 9]
# 5. Tree Sort: [1, 2, 5, 5, 6, 9]
# 6. Cartesian Sort: [1, 2, 5, 5, 6, 9]
# 7. Pigeonhole Sort: [1, 2, 5, 5, 6, 9]
# 8. Cycle Sort: [1, 2, 5, 5, 6, 9]
# 9. Strand Sort: [1, 2, 5, 5, 6, 9]
# 10. Pancake Sort: [1, 2, 5, 5, 6, 9]
# 11. Permutation Sort: [1, 2, 5, 5, 6, 9]
# 12. Gnome Sort: [1, 2, 5, 5, 6, 9]
# 13. Bitonic Sort: [1, 2, 5, 5, 6, 9]
# 14. Sleep Sort: [1, 2, 5, 5, 6, 9]
