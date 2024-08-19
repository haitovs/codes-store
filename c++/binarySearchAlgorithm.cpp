#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

// Function to perform binary search
int binarySearch(const vector<int>& nums, int target) {
  int left = 0;
  int right = nums.size() - 1;

  while (left <= right) {
    int mid = left + (right - left) / 2;

    // Check if target is present at mid
    if (nums[mid] == target) {
      return mid;  // Target found, return the index
    }

    // If target is greater, ignore the left half
    if (nums[mid] < target) {
      left = mid + 1;
    }
    // If target is smaller, ignore the right half
    else {
      right = mid - 1;
    }
  }

  // Target not found, return -1
  return -1;
}

int main() {
  // Sample list of numbers
  vector<int> nums = {2, 4, 7, 10, 14, 20, 25, 30};

  // Sort the list (binary search requires sorted list)
  sort(nums.begin(), nums.end());

  int target;
  cout << "Enter target number: ";
  cin >> target;

  // Perform binary search
  int result = binarySearch(nums, target);

  if (result != -1) {
    cout << "Target found at index: " << result << endl;
  } else {
    cout << "Target not found" << endl;
  }

  return 0;
}
