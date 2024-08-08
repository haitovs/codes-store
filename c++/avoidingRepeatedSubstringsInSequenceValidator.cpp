#include <iostream>
#include <string>
using namespace std;

// Function to check if the sequence is valid
bool isValid(const string& sequence) {
    int length = sequence.length();
    // Check for repeating substrings of all lengths up to half the length of the sequence
    for (int len = 1; len <= length / 2; len++) {
        for (int i = 0; i <= length - 2 * len; i++) {
            if (sequence.substr(i, len) == sequence.substr(i + len, len)) {
                return false; // Found a repeated substring, so return false
            }
        }
    }
    return true; // No repeated substrings found
}

int main() {
    string number;
    cout << "Enter a number composed of digits 0, 1, and 2: ";
    cin >> number;

    // Check if the number contains only 0, 1, and 2
    for (char c : number) {
        if (c != '0' && c != '1' && c != '2') {
            cout << "Invalid input: number must contain only digits 0, 1, and 2." << endl;
            return 1; // Exit with an error code
        }
    }

    // Check if the number is valid
    if (isValid(number)) {
        cout << "The number is valid." << endl;
    } else {
        cout << "The number is not valid." << endl;
    }

    return 0;
}
