#include <iostream>
using namespace std;

// BalancedSumCombinations: Finds combinations of numbers from 1 to n that balance sums.
int maxValue, numbers[7] = {0, 1, 2, 3, 4, 5, 6}, selections[10], sumGroup, currentSum, index, sum, i, isBalanced;
string combinedSumGroup, combinedCurrentSum;

int main() {
    cin >> maxValue;
    
    while (numbers[1] <= maxValue) {
        // Increment the last element in the array
        numbers[6]++;
        
        // Adjust the array if any number exceeds maxValue/2
        for (i = 6; i > 1; i--)
            if (numbers[i] > maxValue / 2) {
                numbers[i] = numbers[i - 1] + 1;
                numbers[i - 1]++;
            }
        
        // Calculate the sum of the current combination
        sum = 0;
        for (i = 1; i <= 6; i++)
            sum += numbers[i];
        
        // If the sum is less than maxValue, skip this combination
        if (sum < maxValue) 
            goto nextCombination;
        
        // Check all possible selections to find balanced sums
        for (i = 1; i <= maxValue; i++) {    
            // Initialize selection counters and the flag for balanced sum
            for (index = 1; index <= 6; index++) 
                selections[index] = 0; 
            isBalanced = 0;
            
            while (selections[1] < 3) {
                currentSum = i; 
                sumGroup = 0;
                
                // Calculate the sum for both groups based on selections
                for (index = 1; index <= 6; index++) {
                    if (selections[index] == 0) {
                        currentSum += numbers[index];
                    }
                    if (selections[index] == 1) {
                        sumGroup += numbers[index];
                    }
                }
                
                // If the sums match, mark as balanced and stop
                if (currentSum == sumGroup) {
                    isBalanced = 1;
                    goto checkNextCombination;
                }
                
                // Increment the last selection and adjust others if necessary
                selections[6]++;
                for (index = 6; index > 1; index--)
                    if (selections[index] > 2) {
                        selections[index] = 0;
                        selections[index - 1]++;
                    }
            }
            
            // If no balanced sum is found, skip this combination
            if (isBalanced == 0) 
                goto nextCombination;
            
        checkNextCombination:; 
        }
        
        // Print the balanced combination
        for (index = 1; index <= 6; index++)
            cout << numbers[index] << " ";
        cout << endl;
        
        // Display detailed balanced sums for each i
        for (i = 1; i <= maxValue; i++) {    
            for (index = 1; index <= 6; index++) 
                selections[index] = 0; 
            isBalanced = 0;
            
            while (selections[1] < 3) {
                currentSum = i; 
                sumGroup = 0; 
                combinedSumGroup = ""; 
                combinedCurrentSum = to_string(i);
                
                for (index = 1; index <= 6; index++) {
                    if (selections[index] == 0) {
                        currentSum += numbers[index];
                        combinedCurrentSum += " " + to_string(numbers[index]);
                    }
                    if (selections[index] == 1) {
                        sumGroup += numbers[index];
                        combinedSumGroup += " " + to_string(numbers[index]);
                    }
                }
                
                // If the sums match, display the result and stop
                if (currentSum == sumGroup) {
                    isBalanced = 1;
                    cout << i << "= :    -> " << combinedCurrentSum << " : " << combinedSumGroup << endl;
                    goto stopDisplay;
                }
                
                // Increment the last selection and adjust others if necessary
                selections[6]++;
                for (index = 6; index > 1; index--)
                    if (selections[index] > 2) {
                        selections[index] = 0;
                        selections[index - 1]++;
                    }
            }
            
        stopDisplay:; 
        }
        
        break;
        
    nextCombination:; 
    }    
}
