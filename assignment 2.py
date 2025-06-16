'''Write a Python program that:
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.'''
a=int(input("Enter a number: "))
if a==0:
    print(a,"This number is neither even nor odd.")
elif a%2==0:
    print(a,"is a even number.")
elif a%1==0:
    print(a,"is a odd number.")

else:
    print("its a invalid number")


'''Write a Python program that:
1.   Uses a for loop to iterate over numbers from 1 to 50.
2.   Calculates the sum of all integers in this range.
3.   Displays the final sum.'''
for i in range(1,50):
    print(i)


total=sum(range(1,50))
print("The sum of number from 1 to 50 is:",total)



