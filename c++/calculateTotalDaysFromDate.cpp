#include <bits/stdc++.h>
using namespace std;

// Array to store the number of days in each month
int daysInMonth[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
int day, month, year, totalDays, dayCount;

int main() {
    // Input: Day, Month, Year
    cout << "Enter Day: ";
    cin >> day;
    cout << "Enter Month: ";
    cin >> month;
    cout << "Enter Year: ";
    cin >> year;

    // Adjust for leap year if applicable
    if (year % 4 == 0) 
        daysInMonth[2] = 29;
    if (year % 100 == 0 && year % 400 != 0)
        daysInMonth[2] = 28;

    // Validate the date
    if ((month == 2 && day > daysInMonth[2]) || day > daysInMonth[month] || month > 12) {
        cout << "Invalid date" << endl;
        return 0;
    }

    // Calculate the total number of days up to the given year
    for (int i = 1; i < year; i++) {
        if (i % 4 == 0) 
            totalDays = 366; 
        else 
            totalDays = 365;

        if (i % 100 == 0 && i % 400 != 0)
            totalDays = 365;
    
        dayCount += totalDays;
    }

    // Add the days for the months in the current year
    for (int i = 1; i < month; i++) {
        dayCount += daysInMonth[i];
    }

    // Add the days in the current month
    dayCount += day;

    // Output the result
    cout << "Total number of days: " << dayCount << endl;
    return 0;
}
