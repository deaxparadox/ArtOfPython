# 
# Implementations of Graphs represented using adjancency List
# 

import asyncio

async def create_adjacency_list(edges, num_vertices):
    # Initialize the adjacency list
    adj_list = [[] for _ in range(num_vertices)]
    
    # Fill the adjancency list based on the edges in the graph
    for u, v in edges:
        # Since the graph is undirected, push the edges in both directions
        adj_list[u].append(v)
        adj_list[v].append(u)
        
        
    return adj_list

async def main():
    # Undirected Graph of 4 nodes
    num_vertices = 4
    edges = [
        (0, 1),
        (0, 2),
        (1, 2),
        (2, 3),
        (3, 1)
    ]
    
    # create the adjacency list
    adj_list = await create_adjacency_list(edges, num_vertices)
    
    
    # Print the adjacency list
    for i in range(num_vertices):
        print(f"{i} -> {" ".join(map(str, adj_list[i]))}")

if __name__ == "__main__":
    asyncio.run(main())