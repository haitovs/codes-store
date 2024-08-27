#include <iostream>
using namespace std;

int numElements, iterationCount, binaryArray[40];

int main() {
  // Input the number of elements
  cin >> numElements;

  // Continue generating binary sequences until the first element becomes 2
  while (binaryArray[1] < 2) {
    iterationCount++;  // Track the number of iterations

    // Print the current iteration number
    cout << endl << iterationCount << "} ";

    // Print the current binary sequence
    for (int i = 1; i <= numElements; i++) {
      cout << binaryArray[i] << " ";
    }

    // Increment the last element of the array
    binaryArray[numElements]++;

    // Carry the increment to the previous elements if needed
    for (int i = numElements; i > 1; i--) {
      if (binaryArray[i] > 1) {
        binaryArray[i] = 0;
        binaryArray[i - 1]++;
      }
    }
  }
}
