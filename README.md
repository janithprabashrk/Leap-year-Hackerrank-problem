Leap Year Determination Code
This Python script is_leap(year) function allows you to determine whether a given year is a leap year or not. A leap year is a year that is evenly divisible by 4 but not by 100 unless it is also divisible by 400. Here's a breakdown of how the code works:

Algorithm Explanation:
Input Year: The user is prompted to input a year.

Leap Year Check: The is_leap(year) function takes the input year as a parameter and determines if it's a leap year or not.

Conditions:

It checks if the year is divisible by 4 and not divisible by 100, in which case it sets leap to True.
Alternatively, if the year is divisible by 400, it sets leap to True.
Return Value: The function returns leap, indicating whether the year is a leap year (True) or not (False).

Output: The script prints whether the input year is a leap year or not based on the returned value.

Usage:
python
Copy code
year = int(input("Enter a year: "))
print("Leap year:", is_leap(year))
Simply run the script, enter the desired year when prompted, and it will output whether the year is a leap year or not.

Example:
Input: 2000
Output: Leap year: True
