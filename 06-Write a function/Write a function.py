def is_leap(year):
    leap = False  # Variable to store the leap year status, initialized as False

    if year % 4 == 0:  # Checks if the year is divisible by 4
        if year % 100 == 0:  # Checks if the year is divisible by 100
            if year % 400 == 0:  # Checks if the year is divisible by 400
                leap = True  # If divisible by 400, it's a leap year
        else:
            leap = True  # If divisible by 4 but not by 100, it's a leap year

    return leap  # Returns the leap year status


year = int(input())  # Takes input for the year to be checked
print(is_leap(year))  # Calls the is_leap function and prints the result
