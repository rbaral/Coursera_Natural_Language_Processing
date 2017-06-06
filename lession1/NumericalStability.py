__author__ = 'rbaral'
import math
num1 = 1000000000
factor = math.pow(10,-6)
for i in range(1000000):
    num1+=factor
num2 = 1000000000
sum = num1 - num2

print sum