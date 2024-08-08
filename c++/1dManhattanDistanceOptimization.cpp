// 1D Manhattan Distance Optimization
#include <iostream>
#include <cmath>
#include <limits>

using namespace std;

// Function to calculate the total movement distance for a given x-coordinate
double calculateTotalMovementX(int points[][2], int n, int x_target) {
    double totalMovement = 0.0;
    for (int i = 0; i < n; ++i) {
        int x = points[i][0];
        totalMovement += abs(x_target - x); // Movement is purely in the x direction
    }
    return totalMovement;
}

// Function to calculate the total movement distance for a given y-coordinate
double calculateTotalMovementY(int points[][2], int n, int y_target) {
    double totalMovement = 0.0;
    for (int i = 0; i < n; ++i) {
        int y = points[i][1];
        totalMovement += abs(y_target - y); // Movement is purely in the y direction
    }
    return totalMovement;
}

// Function to find the optimal x-coordinate to minimize total movement distance
int findOptimalXCoordinate(int points[][2], int n) {
    int optimalX = points[0][0];
    double minMovement = numeric_limits<double>::infinity();

    for (int i = 0; i < n; ++i) {
        int x_target = points[i][0];
        double movement = calculateTotalMovementX(points, n, x_target);
        if (movement < minMovement) {
            minMovement = movement;
            optimalX = x_target;
        }
    }

    return optimalX;
}

// Function to find the optimal y-coordinate to minimize total movement distance
int findOptimalYCoordinate(int points[][2], int n) {
    int optimalY = points[0][1];
    double minMovement = numeric_limits<double>::infinity();

    for (int i = 0; i < n; ++i) {
        int y_target = points[i][1];
        double movement = calculateTotalMovementY(points, n, y_target);
        if (movement < minMovement) {
            minMovement = movement;
            optimalY = y_target;
        }
    }

    return optimalY;
}

int main() {
    int n; // Number of points
    cout << "Enter the number of points: ";
    cin >> n;

    int points[1000][2]; // Array to store points (x, y)

    cout << "Enter the points (x y) one by one:" << endl;
    for (int i = 0; i < n; ++i) {
        cin >> points[i][0] >> points[i][1];
    }

    int optimalX = findOptimalXCoordinate(points, n);
    double minMovementX = calculateTotalMovementX(points, n, optimalX);
    
    int optimalY = findOptimalYCoordinate(points, n);
    double minMovementY = calculateTotalMovementY(points, n, optimalY);

    cout << "Optimal x-coordinate to minimize total movement: " << optimalX << endl;
    cout << "Minimum total movement distance for x: " << minMovementX << endl;
    
    cout << "Optimal y-coordinate to minimize total movement: " << optimalY << endl;
    cout << "Minimum total movement distance for y: " << minMovementY << endl;

    return 0;
}
