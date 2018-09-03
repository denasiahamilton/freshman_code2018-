#CSCI 1133 Homework1
#Denasia Hamilton
#Bonus Problem 1

import turtle

def focalLength(obj, img):
        print ("Welcome to the Focal Length Calculator!!")
        object_distance = (input("Enter an object distance, in mm: ")) #input object distance
        image_distance = (input("Enter an image distance, in mm: ")) #input image distance
        focal_length = 1/(float(image_distance)) + 1/(float(object_distance))
        print("Focal Length of your lens is: ", 1/float((focal_length)), "mm")
        line = (1/float((focal_length)) / 2)
        print("Lens:", line, "mm") #distance between f points, placed at origin
        turtle.speed(1) #speed to see the turtle in motion
        turtle.showturtle()
        turtle.screensize(2000,2000)

        #object
        turtle.forward(-float(object_distance)) #to left if positive, to right if negative
        turtle.color(str("#bc1818"))
        turtle.begin_fill()
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.end_fill()
        turtle.color("black")
        turtle.penup()
        turtle.goto(-float(object_distance),20)
        turtle.write("Object",True, align = "center", font=("Ariel", 10, "normal")) #label above lens axis
        turtle.goto(-float(object_distance),0)
        turtle.pendown()

        #focalpoint1 -- -120 #have to go to origin for it to be the right distance
        turtle.goto(0,0) #go to origin; "reset"
        turtle.forward(-float(1/focal_length))
        turtle.begin_fill()
        turtle.dot(9, str("#176825"))
        turtle.end_fill()
        turtle.penup()
        turtle.goto(-float(1/focal_length),-30)
        turtle.write("Focal Point",True, align = "center", font=("Ariel", 10, "normal")) #label below lens axis
        turtle.color("black")
        turtle.goto(-float(1/focal_length),0)
        turtle.pendown()

        #focalpoint2 -- 120 #have to go to the origin for it to be the right distance
        turtle.goto(0,0) #go to origin; "reset"
        turtle.goto(float(1/focal_length),0)
        turtle.begin_fill()
        turtle.dot(9, str("#176825"))
        turtle.end_fill()
        turtle.penup()
        turtle.goto(float(1/focal_length),-30)
        turtle.write("Focal Point",True, align = "center", font=("Ariel", 10, "normal"))
        turtle.color("black")
        turtle.goto(float(1/focal_length),0)
        turtle.pendown()
        turtle.goto(0,0) #go to origin; "reset"

        #image
        turtle.forward(float(image_distance)) #to right if positive, to left if negative
        turtle.color(str("#183870"))
        turtle.begin_fill()
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.end_fill()
        turtle.color("black")
        turtle.penup()
        turtle.goto(float(image_distance),20)
        turtle.write("Image",True, align = "center", font=("Ariel", 10, "normal")) #label above lens axis
        turtle.goto(float(image_distance),0)
        turtle.pendown()
        turtle.goto(0,0)

        #lens
        turtle.color(str("#5e5e5e"))
        turtle.goto(0,100) #to make the vertical line
        turtle.goto(0,-100) #to make the vertical line

focalLength("obj", "img") #calling function
