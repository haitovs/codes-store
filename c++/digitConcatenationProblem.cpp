#include <iostream>
using namespace std;

// Declare variables
int targetValue, digitOptions[100], expressions[100], termCount, index, currentSum, digitIndex, resetFlag;
string expressionString;

int main() {
    // Take target value as input from the user
    cout << "Enter the target value: ";
    cin >> targetValue;

    // Reset initial conditions for the target value
    digitOptions[1] = 0;
    resetFlag = 0;

    // Generate all possible expressions for the target value
    while (digitOptions[1] < 3) {
        termCount = 1;  // Initialize term count
        expressions[termCount] = 1;  // Start with the first digit (1)

        // Iterate over digits 1 to 8 to create possible expressions
        for (digitIndex = 1; digitIndex <= 8; digitIndex++) {
            if (digitOptions[digitIndex] == 0) {
                termCount++;
                expressions[termCount] = digitIndex + 1;  // Add digit as a positive term
            }
            else if (digitOptions[digitIndex] == 1) {
                termCount++;
                expressions[termCount] = (digitIndex + 1) * (-1);  // Add digit as a negative term
            }
            else if (digitOptions[digitIndex] == 2) {
                // Concatenate digit to the previous term
                if (expressions[termCount] < 0) {
                    expressions[termCount] = expressions[termCount] * 10 - (digitIndex + 1);
                }
                else {
                    expressions[termCount] = expressions[termCount] * 10 + (digitIndex + 1);
                }
            }
        }

        // Calculate the sum of the current expression
        currentSum = expressions[1];
        expressionString = to_string(expressions[1]);
        for (digitIndex = 2; digitIndex <= termCount; digitIndex++) {
            currentSum += expressions[digitIndex];
            if (expressions[digitIndex] > 0) {
                expressionString += "+" + to_string(expressions[digitIndex]);
            }
            else {
                expressionString += to_string(expressions[digitIndex]);
            }
        }

        // Check if the sum matches the target value
        if (currentSum == targetValue) {
            cout << expressionString << " = " << targetValue << endl;
            goto nextIteration;
        }

        // Update the digitOptions array for the next combination
        digitOptions[8]++;
        for (int i = 8; i > 1; i--) {
            if (digitOptions[i] > 2) {
                digitOptions[i] = 0;
                digitOptions[i - 1]++;
            }
        }
    }

nextIteration:
    return 0;
}