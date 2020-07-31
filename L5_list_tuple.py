#length of string
nature = "trees"
print ('the length of nature is ', len(nature)) 
print('letters in nature :\n')   
for i in nature:
    print(i)    
    
#counting number of letters in a sentence by using functions
#loop with functions
def length(phrase): #initialising a function with an argument
    count = 0
    for letter in phrase:
        count = count + 1     #increment count by 1
    
    return count             #gives the count of letters
print(length("the wrold will not work the way you want"))     #calling length


#slicing a string
soil = "planting"
print(soil[3]) 
print("planting"[3]) #prints 2nd index value
print("nitaara"[ 0: 6])#[starts: ends before last value]

#lists
print(['think', 1000, 'times', 35.89, 44/2, -87, 6%3]) 
stars = ['sun', 'moon', 'galaxies', 'milkyway', 'satelites', 'luminious', 365, 99.9889]
print(stars)
print(len(stars))

for i in stars:
    print(i)
    
    
print(stars[0:5 ])
stars.append("harika") #adding to list
print(stars)
print(len(stars))     #gives len of stars after addding 
    
#sum of numbers with list which includes a function 
harry = [12, 1, 2, 4]
bank_account = [3, 4, 5, 62]
my_salary = [10, 20, 20, 100]
print('harry = ', harry)
print('bank_account', bank_account)
print('my_salary is', my_salary)

def adding_numbers(numbers):
    cnt = 0
    for element in harry  :
        cnt = cnt + element
    return(cnt)

print(adding_numbers(harry)) # calling function-adding_numbers


#biggest number from the list
num = [1, 2, 3, -2]
print(num)
max = num[0]
for i in num :
    if (i>= max):
        max = i
print('biggest number in list is ', max)


#biggest number finding from list by using functions
x = [21, 2.90, -333]

def big_num(numbers):   #defining function 
    max = x[0]          #initialising 0 th index element to max
    for i in x:
        if (i>= max):
            max = i

    return max          #max number
print(big_num(x))       #calling the function 

