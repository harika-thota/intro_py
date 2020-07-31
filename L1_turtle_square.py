import turtle     # make all the commands of turtle available

# constructing a square - method 1
square = turtle.Turtle() # initiating turtle
square.forward(100)  # turtle moves forward with distance = 100
square.right(90)     # rotate clockwise by 90 degrees
square.forward(100)
square.right(90)
square.forward(100)
square.right(90)
square.forward(100)


#constructing a square - method 2 using defining a function and adding arguments 

def square2 (length, angle): #defining a function by passing 2 arguments
    square2 = turtle.Turtle()#initialising turtle
    square2.forward(length)  
    square2.right(angle)
    square2.forward(length)
    square2.right(angle)
    square2.forward(length)
    square2.right(angle)
    square2.forward(length)
square2(200, 90)   # calling function with 2 arguments
square2(100/2, 90)


# constructing a square - method 3 using for loop
sua = turtle.Turtle()

for i in range (4):  # loop runs 4 times 
    sua.forward(300) #sua turtle length is S300 ; moves forward = 300
    sua.right(90)


# constructing a rectangle
rect = turtle.Turtle()
rect.forward(100)   #turtle moves forward with distance = 100
rect.right(90)      # rotate clockwise by 90 degrees 
rect.forward(40)
rect.right(90)
rect.forward(100)
rect.right(90)
rect.forward(40)




