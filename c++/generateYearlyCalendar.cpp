#include <bits/stdc++.h>
using namespace std;

int daysInMonth[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
string monthNames[13] = {
    "",     "January", "February",  "March",   "April",    "May",     "June",
    "July", "August",  "September", "October", "November", "December"};

int main() {
  int year, totalDaysTillNow = 0, dayOfWeek;

  // Get the year from user input
  cout << "Year: ";
  cin >> year;

  // Check if the year is a leap year and adjust February days
  if (year % 4 == 0) daysInMonth[2] = 29;
  if (year % 100 == 0 && year % 400 != 0) daysInMonth[2] = 28;

  // Calculate total days up to the start of the given year
  for (int i = 1; i < year; i++) {
    if (i % 4 == 0 && (i % 100 != 0 || i % 400 == 0))
      totalDaysTillNow += 366;  // Leap year
    else
      totalDaysTillNow += 365;  // Regular year
  }

  // Calculate the day of the week for January 1st of the given year
  dayOfWeek =
      (totalDaysTillNow + 1) % 7 - 1;  // 0=Sunday, 1=Monday, ..., 6=Saturday

  // Print the calendar for each month
  for (int month = 1; month <= 12; month++) {
    cout << endl << monthNames[month] << endl;
    cout << "M  T  W  Th  F  Sa  S" << endl;

    // Print leading empty spaces for the first week
    for (int i = 0; i < dayOfWeek; i++) {
      cout << "*   ";
    }

    // Print days of the month
    for (int day = 1; day <= daysInMonth[month]; day++) {
      if (day < 10)
        cout << day << "  ";
      else
        cout << day << " ";

      // Move to the next line after Saturday (if dayOfWeek reaches 6)
      if (dayOfWeek == 6) {
        cout << endl;
        dayOfWeek = 0;  // Reset to Sunday
      } else {
        dayOfWeek++;
      }
    }
    cout << endl;
  }
}
