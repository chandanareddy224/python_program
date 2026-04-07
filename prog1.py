#leap year
def leap_year(n):
    if (n%4==0 or n%400==0):
        print(n,"leap year")
    else:
        print(n,"not a leap year")
leap_year(2024)



def even_or_odd(n):
    if n%2==0:
        print(n,"even")
    else:
        print(n,"odd")
even_or_odd(33)