// example of input

// . . . . . . . . . .
// . . . . . . . . . .
// . . . . . . . . . .
// . . . . # # # # # .
// . . . . # . . . . .
// . . . . # . . . . .
// . . . . # # # # . .
// . . . . # . . . . .
// . . . . # . . . . .
// . . . . # . . . . .

#include <iostream>
using namespace std;

const int MAX_SIZE = 100;

int main() {
  int n;
  cin >> n;

  char matrix[MAX_SIZE][MAX_SIZE];
  char modifiedMatrix[MAX_SIZE][MAX_SIZE];

  // Input the matrix
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      cin >> matrix[i][j];
      modifiedMatrix[i][j] =
          matrix[i][j];  // Copy original matrix to modified matrix
    }
  }

  // Modify the matrix
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (matrix[i][j] == '#') {
        // Set the element to the right if within bounds
        if (j + 1 < n) {
          modifiedMatrix[i][j + 1] = '#';
        }
        // Set the element below if within bounds
        if (i + 1 < n) {
          modifiedMatrix[i + 1][j] = '#';
        }
        // Set the diagonal element if within bounds
        if (i + 1 < n && j + 1 < n) {
          modifiedMatrix[i + 1][j + 1] = '#';
        }
      }
    }
  }

  // Output the modified matrix
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      cout << modifiedMatrix[i][j] << " ";
    }
    cout << endl;
  }

  return 0;
}
