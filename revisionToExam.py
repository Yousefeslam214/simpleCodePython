a = 2;
b = 3;
c = 5;


#####1-Python Program to Print Hello world!
# print('Hello,world')


#####2-Python Program to Add Two Numbers
# num1 = input();
# num2 = input();
# sum = int(num1) + int(num2);
# print('The sum of '+str(num1)+' and ' + str(num2) + ' is '+str(sum))


#####3-Python Program to Find the Square Root
# num = 4
# num_sqrt = num ** 0.5
# # print('The square root of %0.3f is %0.3f' + str(num_sqrt))
# print('The square root of %0.1f is %0.1f' %(num , num_sqrt))


#####4-Python Program to Calculate the Area of a Triangle
# num1 = 5;
# num2 = 5;
# num3 = 5;
# s = (num1 + num2 + num2 ) / 2;
# area = (s*(s - num1)*(s - num2)*(s - num3)) ** 0.5
# print('The area of the triangle is %0.1f' %area)


#####5-Python Program to Solve Quadratic Equation
# import cmath
# a = 5;
# b = 5;
# c = 5;

# d = (b**2) - (4*a*c)

# sol1 = (-b-cmath.sqrt((d)/(2*a)))
# sol2 = (-b+cmath.sqrt((d)/(2*a)))

# print('The solution are {0} and {0}'.format(sol1,sol2))


#####6-Python Program to Swap Two Variables
# temp = a
# a = b
# b = temp

# print('The value of a after swapping: {}'.format(a))
# print('The value of b after swapping: {}'.format(b))


#####7-Python Program to Generate a Random Number
# import random

# print(random.randint(0,9))


#####8-Python Program to Convert Kilometers to Miles
# kilometer = float(input('enter km '))

# miles = kilometer * 0.621

# print('%0.2f km is = to %0.2f miles'%(kilometer,miles))


#####9-Python Program to Convert Celsius To Fahrenheit
# cel = 37.5

# fah =(cel * 1.8) + 32
# print('%0.1f cel = %0.1f fah '%(cel,fah))


#####10- Python Program to Check if a Number is Positive, Negative or 0
# num = float(input("Enter a number: "))

# if num > 0:
#        print("Positive")
# elif num < 0:
#        print("Negative")
# else:
#        print("Zero")

#####11- Python Program to Check if a Number is Odd or Even

# num = int(input("Enter a Number: "))

# if (num % 2) == 0 :
#        print("{0} is Even".format(num))
# else :
#        print("{0} is Odd".format(num))


######12- Python Program to Check Leap Year

######13- Python Program to Find the Largest Among Three Numbers

######14- Python Program to Check Prime Number

# num = 10

# if num > 1:
#        for i in range(2,num):
#               if (num % i) == 0:
#                      print(num,"is not a prime number")
#                      print(i,"times",num/i,"is",num)
#                      break
#        else :
#                      print(num,"is a prime number")
# else :
#        print(num,"is not a prime number")


######15- Python Program to Print all Prime Numbers in an Interval

######16- Python Program to Find the Factorial of a Number
# num = 4

# factorial = 1

# if num < 0:
#        print("sorry, don't exist")
# elif num == 0:
#        print("the factoial of 0 is 1")
# else :
#        for i in range(1,num+1):
#               factorial =factorial*i
#        print("The factorial of",num,"is",factorial)


#####17- Python Program to Display the multiplication Table

#####18- Python Program to Print the Fibonacci sequence#####################################

# nterms = int(input("How many terms? "))

# n1 ,n2 = 0,1
# count = 0

# if nterms <= 0:
#        print("Please enter a poitive integer")
# elif nterms == 1:
#        print("fibonacci sequence upto",nterms,":")
#        print(n1)
# else:
#        print("Fibonacci sequence:")
#        while count < nterms :
#               print(n1)
#               nth = n1 + n2
#               n1 =n2
#               n2 =nth
#               count += 1


#####19- Python Program to Check Armstrong Number############################

#####20- Python Program to Find Armstrong Number in an Interval###############

#####21- Python Program to Find the Sum of Natural Numbers ###########################

# num = 4

# if num < 0:
#        print("enter + number")
# else :
#        sum = 0
       
#        while(num>0):
#               sum += num
#               num -= 1
#        print("The sum is", sum)


#####22- Python Program To Display Powers of 2 Using Anonymous Function


# terms = 10 

# res = list(map(lambda x: 2**x,range(terms)))

# print("The total terms are :",terms)
# for i in range(terms):
#        print("2 raised to power ",i,"is",res[i])