#include<iostream>
using namespace std;

// SpiralMatrixFill: Fills an n x n matrix in a spiral order.
int currentLayer = 1, matrixSize, row, col, counter = 0, totalElements, originalSize;
int matrix[100][100];

int main() {
    cout << "Enter the size of the matrix: ";
    cin >> matrixSize;

    totalElements = matrixSize * matrixSize;
    originalSize = matrixSize;

    // Loop until all elements are filled
    while (counter != totalElements) {
        // Fill the top row of the current layer
        for (col = currentLayer; col <= matrixSize; col++) {
            counter++;
            matrix[currentLayer][col] = counter;
        }
        // Fill the right column of the current layer
        for (row = currentLayer + 1; row <= matrixSize; row++) {
            counter++;
            matrix[row][matrixSize] = counter;
        }
        // Fill the bottom row of the current layer
        for (col = matrixSize - 1; col >= currentLayer; col--) {
            counter++;
            matrix[matrixSize][col] = counter;
        }
        // Fill the left column of the current layer
        for (row = matrixSize - 1; row >= currentLayer + 1; row--) {
            counter++;
            matrix[row][currentLayer] = counter;
        }
        // Move to the next inner layer
        matrixSize--;
        currentLayer++;
    }

    // Print the resulting spiral matrix
    for (int i = 1; i <= originalSize; i++) {
        for (int j = 1; j <= originalSize; j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
}
