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
import random

print(random.randint(0,9))