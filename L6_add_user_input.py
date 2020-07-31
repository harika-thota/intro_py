#Topic -adding two numbers with user input 

#we are using input() function to take input from user
#store input numbers
num1 = input('enter 1st number: ')
num2 = input('enter 2nd number: ')

#Add two numbers
#converting string into float by function float()
sum = float(num1) +float(num2)

#display the sum 
print('The sum of {} and {} is {}'.format(num1,num2,sum))