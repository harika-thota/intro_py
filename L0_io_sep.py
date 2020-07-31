#Topic - input , output , seprator

print(1,2,3,4)
print(1,2,3,4, sep ='*') #seprate the values by *
print(3,4,5, sep = '%')  #seprates the value by %

#To make our output look good and clear, we can use str.format() method

name = 'jessica'
age = '12'
print('her name is {} and her age is {}'.format(name,age))
#curly braces are place holders.
#they are printed by using tuple index


print('i would preffer {} ratherthan {}'.format('python', 'c++'))
#first {}-> takes 0 index value = python
#second {}-> takes 1 index value = c++


print('i would preffer {1} ratherthan {0}'.format('python','c++'))
# c++ is taken in first curly brace

num = input ('enter a number:' ) #num is string  
print(num)
#converting string to int and adding a number 
int('10')

print('the final addition is ', num)

# int('2 + 3') is an error 
print(eval('20 + 3')) #evaluate expressions and adding the strings 
print(int(2 + 3 ))


