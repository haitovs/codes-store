#include <iostream>
using namespace std;

int limit, primeCounter = 1;
string primeString;
bool isComposite[100000];

int main() {
  // Input the upper limit for finding primes
  cin >> limit;

  // Sieve of Eratosthenes to find prime numbers below the limit
  for (int number = 2; number < limit; number++) {
    if (!isComposite[number]) {
      // Mark multiples of the prime number as composite
      for (int multiple = 2; multiple <= limit / number; multiple++)
        isComposite[number * multiple] = true;

      // Append the prime number to the string and print it
      primeString = primeString + " " + to_string(number);
      primeCounter++;
      cout << number << " ";
    }

    // Every 10th number, reset string and counter based on prime count
    if (number % 10 == 0) {
      if (primeCounter >= 4) {
        // Reset the prime counter and string if more than 4 primes are found
        primeCounter = 0;
        primeString = "";
      } else {
        primeString = "";
        primeCounter = 0;
      }
    }
  }
}
