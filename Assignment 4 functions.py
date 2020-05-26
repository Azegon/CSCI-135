def add (x, y):
    print(x + y)
    return

def payreport(employeeName, hoursWorked, hourlyPay, taxRate):
    print(employeeName)
    print(hoursWorked)
    print(hourlyPay)
    print(taxRate)
    return

def grosspay(hoursWorked, hourlyPay):
    grosspay = hoursWorked*hourlyPay
    return grosspay

def netpay(grossPay, hourlyPay):
    netPay = grossPay - grossPay*hourlyPay
    return netPay

def largestint(user_array):
    largeint = 0
    for x in user_array:
        if x > largeint:
            largeint = x
    return largeint

