def is_leap_year(year):
    return (year%4==0 and year%100!=0) or (year%400==0)
def count_days(month,year):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif month==2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return "Invalid month"
month=int(input("Enter month:"))
year=int(input("Enter year:"))
days=count_days(month,year)
print(f"Number of days in {month} of year {year} : {days}")