def convert(minute):
    return minute*60

x = int(input("Enter the minute:"))
print(str(x) + " minutes = " + str(convert(x)) + " seconds")