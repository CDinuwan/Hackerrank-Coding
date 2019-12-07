def is_leap(year):
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                return bool(year)
            else:
                return not(year)
        else:
            return bool(year)
    else:
        return not(year)
year = int(input())
print(is_leap(year))
