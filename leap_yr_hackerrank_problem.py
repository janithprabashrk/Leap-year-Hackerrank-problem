def is_leap(year):
    leap = False

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = True

    return leap

year = int(input("Enter a year: "))
print("Leap year:", is_leap(year))


#A year is a leap year if:
#It's divisible by 4, and
#It's not divisible by 100, or
#It's divisible by 400