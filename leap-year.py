<<<<<<< HEAD
 year = int(input("Please specify a year: "))
year = year % 4 == 0 and year % 100 != 0 or year % 4 == 0 and year % 100 == 0 and year % 400 == 0
=======
# first line added.
# second line added.
year = int(input("Please specify a year: "))
year = year % 4 == 0 and year % 100 != 0 and year % 4 == 0 and year % 100 == 0 and year % 400 == 0
>>>>>>> backend
print("Is the year you have speficied LEAP YEAR? - ", year)
print(year)
