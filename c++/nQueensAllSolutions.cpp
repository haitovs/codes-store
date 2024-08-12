#include <bits/stdc++.h>
using namespace std;

const int BOARD_SIZE = 8;  // Change this to any N value for N-Queens problem
int solutionCount = 0;
int queenPositions[BOARD_SIZE + 1];  // Index from 1 to BOARD_SIZE for easier readability

// Function to check if the current configuration is valid (no conflicts)
bool isValidPosition(int row) {
    for (int previousRow = 1; previousRow < row; previousRow++) {
        if (queenPositions[previousRow] == queenPositions[row] ||  // Same column conflict
            abs(queenPositions[previousRow] - queenPositions[row]) == abs(previousRow - row))  // Diagonal conflict
            return false;
    }
    return true;
}

// Function to recursively place queens and find all solutions
void solve(int currentRow) {
    if (currentRow > BOARD_SIZE) {
        solutionCount++;
        cout << "Solution " << solutionCount << ": " << endl;
        for (int row = 1; row <= BOARD_SIZE; row++) {
            for (int col = 1; col <= BOARD_SIZE; col++) {
                if (col == queenPositions[row])
                    cout << " Q ";  // Place queen
                else
                    cout << " * ";  // Empty space
            }
            cout << endl;
        }
        cout << endl;
    } else {
        for (int col = 1; col <= BOARD_SIZE; col++) {
            queenPositions[currentRow] = col;
            if (isValidPosition(currentRow)) {
                solve(currentRow + 1);  // Recur to place the next queen
            }
        }
    }
}

int main() {
    solve(1);  // Start solving from the first row
    cout << "Total number of solutions: " << solutionCount << endl;
    return 0;
}
