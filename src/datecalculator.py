"""
Script which finds the number of days between two georgian dates.

Context is for a science project where it is necessary to run experiments and calculate
the number of full days elasped between seperate days. Since partial days are not
helpful to the experiment we only consider 'whole' days.

- We only consider dates between 01/01/1901 and 31/12/2999
- Dates are inputted in the DD/MM/YYYY format.
- Inputs are made through the command line via the console.
- No libraries are allowed.
- Test libraries are allowed.
- Providing other avenues to provide inputs is a bonus.

The difference is  calculated by converting Georgian Dates into Julian Dates, 
after which they can easily be subtracted from one another to give a accurate
number of days between them. This also helps us avoid the pitfalls of having to
deal with leap years and months with 30 - 31 days.

The algorithm for the Georgian to Julian days was provided courtesy of Wikipedia's
Julian Day article: 
https://en.wikipedia.org/wiki/Julian_day#Converting_Gregorian_calendar_date_to_Julian_Day_Number

Author: Ahmad Chakhachiro
Contact: ahmad.chakhachiro@gmail.com
"""


def verifyValues(value):
    # Verify if the value is empty, or if it corresponds to the date range that
    # we only consider.
    if len(value) < 2 or not value[1] or not value[2]:
        return bool(False)
    if int(value[0]) < 1 or int(value[0]) > 31 :
        return bool(False)
    if int(value[1]) < 1 or int(value[1]) > 12:
        return bool(False)
    if int(value[2]) < 1901 or int(value[2]) > 2999:
        return bool(False)
    return bool(True)

def calculateJulianDate(georgianDate):
    D = int(georgianDate[0])
    M = int(georgianDate[1])
    Y = int(georgianDate[2])
    # Julian Month Constant  which is used several times in our Julian Date conversion.
    JMC = int((M - 14)/12.0)
    
    # Values are casted to ints to truncate values after the decimal point.
    JDN = int((1461*(Y + 4800 + JMC))/4.0)
    JDN += int((367*(M - 2 - (JMC*12)))/12.0)
    JDN -= int((3*((Y + 4900 + JMC)/100))/4.0)
    JDN += D - 32075

    return JDN
    
def calculateDifference():
    firstDate = (raw_input("First Date: ")).split("/")
    if verifyValues(firstDate) == bool(False):
        print("Incorrect date for ", firstDate, " please try again.")
        quit()
    
    secondDate = (raw_input("Second Date: ")).split("/")
    if verifyValues(secondDate) == bool(False) :
        print("Incorrect date for ", secondDate, " please try again.")
        quit()
        
    if (firstDate == secondDate) :
        print('Total number of days in between ' , firstDate, ' & ', secondDate, ' is ', 0, ' days.')
        quit()
    
    julianDateOne = calculateJulianDate(firstDate)
    julianDateTwo = calculateJulianDate(secondDate)  
    julianDifference = julianDateOne - julianDateTwo
    
    # Depending on the order of the dates provided we want to make the value
    # absolute.
    if julianDifference < 0 :
        julianDifference *= -1
        
    print('Total number of days in between ' , firstDate, ' & ', secondDate, ' is ', julianDifference - 1, ' days.')
    quit()

if __name__ == "__main__":
    calculateDifference()

