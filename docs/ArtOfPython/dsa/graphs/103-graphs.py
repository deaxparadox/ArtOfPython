# 
# Transpose Graphs
# 


import asyncio


# function to add an edge from vertex
# source to vertex object
async def addEdge(adj, src, dest):
    adj[src].append(dest)
    
# function to print adjancency list
# of a graph
async def displayGraph(adj, v):
    for i in range(v):
        print(i, "--> ", end="")
        for j in range(len(adj[i])):
            print(adj[i][j], end=" ")
        print()
        
        
# function to get Transpose of a graph
# taking adjacency list of given graph
# and that of Transpose graph
async def transposeGraph(adj, transpose, v):
    
    # traverse the adjacency list of given
    # graph and for each edge (u, v) add
    # add edge (v, u) in the transpose graph's 
    # adjacency list
    
    for i in range(v):
        for j in range(len(adj[i])):
            await addEdge(transpose, adj[i][j], i)
            
async def main():
    v = 5
    adj = [[] for i in range(v)]
    
    await addEdge(adj, 0, 1)
    await addEdge(adj, 0, 4)
    await addEdge(adj, 0, 3)
    await addEdge(adj, 2, 0)
    await addEdge(adj, 3, 2)
    await addEdge(adj, 4, 1)
    await addEdge(adj, 4, 3)
    
    
    # Finding transpose of graph represented
    # by adjacency list adj[]
    transpose = [[] for i in range(v)]
    
    await transposeGraph(adj, transpose, v)
    
    # displaying adjacency list of 
    # transpose graph i.e. b
    await displayGraph(transpose, v)
    

if __name__ == "__main__":
    asyncio.run(main())