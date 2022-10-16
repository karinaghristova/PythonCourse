#checks if the given year is a leap year
def is_leap_year(year):
    if year % 400 == 0 and year % 100 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False 

#checks if day is valid for the given month and year
def is_valid_Day(day, month, year):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months[1] = 29 if is_leap_year(year) else 28

    if 1 <= day <= months[month-1]:
        return True
    else:
        return False

#accepts ucn as string and checks if last digit of ucn is valid
def is_valid_checksum(ucn): 
    weight = [2, 4, 8, 5, 10, 9, 7, 3, 6]
    sum = 0
    pos = 0

    while True:
        if pos >= 9:
            break
        c = ucn[pos]
        if c.isdigit():
            digit = int(c)
            sum += digit * weight[pos]
            pos += 1
   
    sum = sum % 11
    sum = sum % 11 if sum < 10 else 0

    if sum == int(ucn[9]):
        return True
    else:
        return False


def is_valid_UCN(ucn, should_bypass_checksum=False):
    # Passing an int ucn is probably not a good idea in the following case:
    # If we're trying to pass an ucn of a person born in 2000/1900/1800 
    # as there will be leading zeroes (especially if they are born between January and September in 1900)
    ucn = str(ucn) #kinda the first thing that popped in my mind to make it work with int input

    y = (int(ucn[0]) * 10) + int(ucn[1])
    m = (int(ucn[2]) * 10) + int(ucn[3])
    d = (int(ucn[4]) * 10) + int(ucn[5])
    validDay = False

    if 1 <= m <= 12:
        validDay = is_valid_Day(d, m, 1900 + y)
    elif 21 <= m <= 32:
        validDay = is_valid_Day(d, m - 20, 1800 + y) #just assuming that people born before 1800 don't have a ucn as it is introduced to our coutry in 1977 :)
    elif 41 <= m <= 52:
        validDay = is_valid_Day(d, m - 40, 2000 + y)
    else:
        return False

    if should_bypass_checksum == False:
        return validDay and is_valid_checksum(ucn)
    else:
        return validDay


#Tests from lecturers
print(is_valid_UCN("6101057509") == True)
print(is_valid_UCN("6101057500", should_bypass_checksum=True) == True)
print(is_valid_UCN("6101057500") == False)
print(is_valid_UCN("6913136669") == False)

#My tests (ucns are randomly generated from the internet)
print(is_valid_UCN(6101057509) == True)
print(is_valid_UCN(6101057507, should_bypass_checksum=True))
print(is_valid_UCN(4809047448) == True) #born in 1948 (int)
print(is_valid_UCN("0546252202") == True) #born in 2005 (string)
print(is_valid_UCN("0422292889") == True) #born in  29.02.1804 (leap year) (probably too old to understand this code)
print(is_valid_UCN(2148211979) == True) #born in 2021 (way too young to understand this code)
