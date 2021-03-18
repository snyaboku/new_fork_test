#ask the user to input a single digit integer to a variable 'n'
#then print out all of the even numbers from 0 to n (include n)
n = int(input("Enter a number:"))
i = 1
while n>=i:
    if i % 2 == 0:
        print(i)
    i+=1