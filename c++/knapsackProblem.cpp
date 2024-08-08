#include <iostream>
using namespace std;

// Number of items, maximum weight capacity
int num_items, max_weight;

// Arrays for weights, values, and item inclusion tracker
int weights[100], values[100], include_item[100];

// Variables to track current total weight, current total value, 
// maximum value found, and corresponding weight
int current_weight, current_value, max_value, best_weight;

// Strings to store the current subset of items and the best subset
string current_subset, best_subset;

int main() {
    // Input number of items and maximum weight capacity
    cin >> num_items >> max_weight;

    // Input the weight and value of each item
    for (int i = 1; i <= num_items; i++) {
        cout << "Weight of item " << i << ": ";
        cin >> weights[i];
        cout << "Value of item " << i << ": ";
        cin >> values[i];
    }

    // Generate all possible subsets
    while (include_item[1] < 2) {
        // Initialize current total weight and value to 0
        current_weight = 0;
        current_value = 0;
        current_subset = "";

        // Evaluate the current subset
        for (int i = 1; i <= num_items; i++) {
            if (include_item[i] == 0) { // If item i is included in the subset
                current_weight += weights[i];
                current_value += values[i];
                current_subset += to_string(i) + " "; // Add item number to the subset string
            }
        }

        // Check if the current subset is the best so far
        if (current_weight <= max_weight && current_value > max_value) {
            max_value = current_value;
            best_weight = current_weight;
            best_subset = current_subset;
        }

        // Increment the binary counter (to generate the next subset)
        include_item[num_items]++;
        for (int i = num_items; i > 1; i--) {
            if (include_item[i] > 1) {
                include_item[i] = 0;
                include_item[i - 1]++;
            }
        }
    }

    // Output the best solution found
    cout << "Maximum Value: " << max_value << endl;
    cout << "Total Weight: " << best_weight << endl;
    cout << "Items Selected: " << best_subset << endl;

    return 0;
}
