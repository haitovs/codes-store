#include <cmath>
#include <iostream>
using namespace std;

// Constants
const int MAX_SIZE = 100;

int numElements, subsetFlag[MAX_SIZE], subsetSum1, subsetSum2,
    minDifference = 99999;
int elements[MAX_SIZE], subset1Sum, subset2Sum;
string subset1Elements, subset2Elements, subset1Str, subset2Str;

int main() {
  // Input number of elements and the elements themselves
  cin >> numElements;
  for (int i = 1; i <= numElements; i++) cin >> elements[i];

  // Initialize the subset flag array
  while (subsetFlag[1] < 2) {
    subsetSum1 = 0;   // Sum for the first subset
    subsetSum2 = 0;   // Sum for the second subset
    subset1Str = "";  // Elements in the first subset
    subset2Str = "";  // Elements in the second subset

    // Partition elements into two subsets based on subsetFlag
    for (int i = 1; i <= numElements; i++) {
      if (subsetFlag[i] == 0) {
        subsetSum2 += elements[i];
        subset2Str += " " + to_string(elements[i]);
      } else {
        subsetSum1 += elements[i];
        subset1Str += " " + to_string(elements[i]);
      }
    }

    // Update minimum difference and corresponding subsets if a smaller
    // difference is found
    if (fabs(subsetSum1 - subsetSum2) < minDifference) {
      minDifference = fabs(subsetSum1 - subsetSum2);
      subset1Sum = subsetSum1;
      subset2Sum = subsetSum2;
      subset1Elements = subset1Str;
      subset2Elements = subset2Str;
    }

    // Update the subsetFlag array to generate the next subset combination
    subsetFlag[numElements]++;
    for (int i = numElements; i > 1; i--)
      if (subsetFlag[i] > 1) {
        subsetFlag[i] = 0;
        subsetFlag[i - 1]++;
      }
  }

  // Output the results
  cout << "Minimal Difference: " << minDifference << endl;
  cout << "Subset 1: " << subset2Elements << "  Sum: " << subset2Sum << endl;
  cout << "Subset 2: " << subset1Elements << "  Sum: " << subset1Sum << endl;

  return 0;
}
