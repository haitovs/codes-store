#include <iostream>
#include <string>
using namespace std;

int stackIndex, n;
char stack[100];  // Stack to hold opening brackets
string inputString;

int main() {
  // Input the string containing brackets
  cin >> inputString;

  // Iterate through each character of the string
  for (int i = 0; i < inputString.length(); i++) {
    char currentChar = inputString[i];

    // Check if the current character is an opening bracket
    if (currentChar == '{' || currentChar == '[' || currentChar == '(') {
      stackIndex++;  // Move stack pointer up
      stack[stackIndex] =
          currentChar;  // Push the opening bracket onto the stack
    }
    // Check if the current character is a closing bracket
    else {
      if (currentChar == '}') {
        // Check if the top of the stack is the matching opening bracket
        if (stack[stackIndex] == '{') {
          stackIndex--;  // Pop the top of the stack
        } else {
          stackIndex = -1;  // Mismatch found
          break;
        }
      }
      if (currentChar == ']') {
        if (stack[stackIndex] == '[') {
          stackIndex--;
        } else {
          stackIndex = -1;
          break;
        }
      }
      if (currentChar == ')') {
        if (stack[stackIndex] == '(') {
          stackIndex--;
        } else {
          stackIndex = -1;
          break;
        }
      }
    }
  }

  // Output the result (optional; could include a check for balanced brackets)
}
