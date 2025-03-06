def leapyear(year):
    if (year%400==0 or (year%100!=0 and year%4==0)):
        print(f"{year} is a leap year".format(year))
    else:
        print(f"{year} is not a leap year".format(year))
year=int(input("Enter a year:"))
leapyear(year)
