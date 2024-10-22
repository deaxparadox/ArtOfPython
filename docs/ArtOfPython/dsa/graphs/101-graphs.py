# 
# Implementation of Graphs using Adjacency Matrix;
# 


import asyncio

async def create_adjancency_matrix(graph):
    # Get the number of vertices in the graph
    num_vertices = len(graph)
    
    # Initialize the adjancency matrix with zeros
    adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]
    
    # Fill the adjancency matrix based on the edges in the graph
    for i in range(num_vertices):
        for j in range(num_vertices):
            if graph[i][j] == 1:
                adj_matrix[i][j] = 1
                # For directed graph, set symmetric entries
                adj_matrix[j][i] = 1
    
    return adj_matrix

# The indices represent the vertices, and the values are lists of neighboring values
graph = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
]


async def main():

    # Create the adjacency matrix
    adj_matrix = await create_adjancency_matrix(graph)


    # Print the adjacency matrix 
    for row in adj_matrix:
        print(" ".join(map(str, row)))
        
if __name__ == "__main__":
    asyncio.run(main())