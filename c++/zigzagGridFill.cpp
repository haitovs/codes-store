#include <iostream>
using namespace std;

int main() {
    int row, col, gridSize, value = 1;
    int grid[100][100]; // Define a 100x100 grid

    // Read the grid size from input
    cin >> gridSize;

    // Fill the grid based on the pattern
    for (int col = 1; col <= gridSize; col++) {
        for (int row = 1; row <= gridSize; row++) {
            if (col % 2 == 1) { // For odd columns, fill top to bottom
                grid[row][col] = value;
            } else { // For even columns, fill bottom to top
                grid[gridSize - row + 1][col] = value;
            }
            value++;
        }
    }

    // Output the filled grid
    for (int col = 1; col <= gridSize; col++) {
        for (int row = 1; row <= gridSize; row++) {
            cout << grid[row][col] << " ";
        }
        cout << endl;
    }

    return 0;
}
