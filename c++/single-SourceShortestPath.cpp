#include<iostream>
using namespace std;

// Define the maximum size of the graph (10,000 nodes)
const int MAX_NODES = 10000;

// Declare variables
int numNodes, head, tail, currentNode, graph[MAX_NODES], links[MAX_NODES], minDistance[MAX_NODES], adjMatrix[MAX_NODES][MAX_NODES], parentNode;

int main() {
    // Enter the size of the adjacency matrix (number of nodes)
    cin >> numNodes;

    // Populate the adjacency matrix with edge weights
    for (int i = 1; i <= numNodes; i++)
        for (int j = 1; j <= numNodes; j++)
            cin >> adjMatrix[i][j];

    // Initialize starting node values
    graph[1] = 1; 
    links[1] = 0; 
    minDistance[1] = 1; 
    head = 0; 
    tail = 1; 
    currentNode = 1;

    // Process each node in the graph
    while (currentNode != 0) {
        head++; 
        currentNode = graph[head];

        // Traverse neighbors of the current node
        for (int i = 1; i <= numNodes; i++) {
            if (adjMatrix[currentNode][i] > 0) {  // If there's an edge
                // If the node is unvisited or a shorter path is found
                if (minDistance[i] == 0 || (minDistance[currentNode] + adjMatrix[currentNode][i]) < minDistance[i]) {
                    tail++; 
                    graph[tail] = i; 
                    links[i] = currentNode; 
                    minDistance[i] = minDistance[currentNode] + adjMatrix[currentNode][i];
                }
            }
        }
    }

    // Output the shortest paths from node 1 to all other nodes
    for (int i = 2; i <= numNodes; i++) {
        if (links[i] == 0) { 
            cout << i << "-nji baryp bolmayar";  // No path to node i
            continue;
        }
        parentNode = i;
        while (parentNode != 0) {
            cout << parentNode << " -> ";
            parentNode = links[parentNode];
        }
        cout << " Jemi:= " << minDistance[i] - 1 << "manat" << endl;  // Total cost to reach node i
    }
}
