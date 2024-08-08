#include <iostream>
using namespace std;

// Function to count the number of ways to reach the top-right corner of an n x n grid
int countPathsInGrid(int gridSize) {
    int pathGrid[gridSize][gridSize];

    // Initialize the last row and last column to 1, as there's only one way to move to the edge
    for (int i = 0; i < gridSize; i++) {
        pathGrid[i][gridSize - 1] = 1;
        pathGrid[gridSize - 1][i] = 1;
    }

    // Fill in the grid by summing the number of ways from the right and bottom cells
    for (int row = gridSize - 2; row >= 0; row--) {
        for (int col = gridSize - 2; col >= 0; col--) {
            pathGrid[row][col] = pathGrid[row + 1][col] + pathGrid[row][col + 1];
        }
    }

    // Display the grid (optional)
    for (int row = 0; row < gridSize; row++) {
        for (int col = 0; col < gridSize; col++) {
        	if(pathGrid[row][col] >= 10) cout << pathGrid[row][col] << " ";
        	else if(pathGrid[row][col] < 10) cout << pathGrid[row][col] << "  ";
        }
        cout << endl;
    }

    // Return the number of ways to reach the top-right corner from the bottom-left corner
    return pathGrid[0][0];
}

int main() {
    int gridSize;
    cout << "Enter the size of the grid (n): ";
    cin >> gridSize;

    int totalPaths = countPathsInGrid(gridSize);
    cout << "The number of ways to reach the top-right corner is: " << totalPaths << endl;

    return 0;
}
