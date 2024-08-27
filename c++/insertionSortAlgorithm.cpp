#include <iostream>
using namespace std;

int numElements, array[100], currentElement, position;

int main() {
  // Input the number of elements
  cin >> numElements;

  // Input the elements of the array
  for (int i = 1; i <= numElements; i++) {
    cin >> array[i];
  }

  // Insertion sort algorithm
  for (int i = 2; i <= numElements; i++) {
    currentElement = array[i];  // Element to be inserted in the sorted part
    position = i - 1;

    // Shift elements in the sorted part to make space for the currentElement
    while (position > 0 && array[position] > currentElement) {
      array[position + 1] = array[position];
      position--;
    }

    // Insert the currentElement at the correct position
    array[position + 1] = currentElement;
  }

  // Output the sorted array
  for (int i = 1; i <= numElements; i++) {
    cout << array[i] << " ";
  }
}
