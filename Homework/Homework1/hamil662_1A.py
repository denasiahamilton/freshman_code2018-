#CSCI 1133 Homework1
#Denasia Hamilton
#Problem 1A

def focalLength(obj, img):
        print ("Welcome to the Focal Length Calculator!!")
        object_distance = (input("Enter an object distance, in mm: ")) #input object distance
        image_distance = (input("Enter an image distance, in mm: "))#input image distance
        focal_length = 1/(float(image_distance)) + 1/(float(object_distance))
        print("Focal Length: ", 1/float((focal_length)), "mm")

focalLength("obj", "img")
