#leap year
def leap_year(n):
    if (n%4==0 or n%400==0):
        print(n,"leap year")
    else:
        print(n," leap year")
leap_year(2024)