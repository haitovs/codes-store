#include <iostream>
#include <cctype>
#include <string>

using namespace std;

// Function to encode a string using ROT13 cipher
string rot13_encoder(const string& input) {
    string result = "";  // Initialize result string

    // Iterate over each character in the input string
    for (char ch : input) {
        if (isalpha(ch)) {  // Check if the character is a letter
            // Determine base character ('A' for uppercase, 'a' for lowercase)
            char base = (isupper(ch)) ? 'A' : 'a';
            // Apply ROT13 transformation
            result += (ch - base + 13) % 26 + base;
        } else {
            result += ch;  // Non-alphabetic characters are added unchanged
        }
    }

    return result;  // Return the encoded string
}

// Function to decode a ROT13 encoded string
string rot13_decoder(const string& input) {
    return rot13_encoder(input);  // ROT13 encoding and decoding are the same
}

int main() {
    int choice;
    string text, result;

    // Display menu options
    cout << "Select an option:" << endl;
    cout << "1. Encode text using ROT13" << endl;
    cout << "2. Decode text using ROT13" << endl;
    cout << "Enter your choice (1 or 2): ";
    cin >> choice;
    cin.ignore();  // Ignore the newline character left in the input buffer

    // Prompt user for input text
    cout << "Enter the text: ";
    getline(cin, text);  // Read the full line of text including spaces

    // Process based on user's choice
    if (choice == 1) {
        result = rot13_encoder(text);  // Encode text
        cout << "Encoded Text: " << result << endl;
    } else if (choice == 2) {
        result = rot13_decoder(text);  // Decode text
        cout << "Decoded Text: " << result << endl;
    } else {
        cout << "Invalid choice. Please select 1 or 2." << endl;
    }

    return 0;
}
