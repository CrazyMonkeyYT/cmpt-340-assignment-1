####
#name: Thomas Williamson
#Student Id: 588206
#CMPT360 spring 2021
#assignment #1
#title: calcualte triangle on complex plane
#####
import math

#gets point
#check valididty of input and change input to int
def getinput(point):
    try:
        if point[-1] == 'i':

            point = point[:-1].split("+")
        else:
            raise ValueError()
        #convert user input to int
        point[0] = int(point[0])
        point[1] = int(point[1])
    except:
        point = getinput(input('Error incorrect  type\ntry again?\ninput point as "a + bi"'))
    return(point)

#calculates length form each point to point 
def getLength(point1, point2):
    if point1[0] <= point2[0]:
        templeng1 = point2[0]-point1[0]
        if point1[1] <= point2[1]:
            templeng2 = point2[1]-point1[1]
        else:
            templeng2 = point1[1]-point2[1]
    else:
        templeng1 = point1[0]-point2[0]
        if point1[1] <= point2[1]:
            templeng2 = point2[1]-point1[1]
        else:
            templeng2 = point1[1]-point2[1]
    return(math.sqrt((templeng1**2)+(templeng2**2)))

#gets inputs
point1 = getinput(input('input point 1 as "a + bi"'))
point2 = getinput(input('input point 2 as "a + bi"'))
point3 = getinput(input('input point 3 as "a + bi"'))

#gets lengths
length12 = getLength(point1, point2)
length32 = getLength(point3, point2)
length31 = getLength(point3, point1)
#gets angle of each point
angle1 = math.degrees(math.acos(((length12**2)+(length31**2)-(length32**2))/(2*length12*length31)))
angle2 = math.degrees(math.acos(((length12**2)+(length32**2)-(length31**2))/(2*length12*length32)))
angle3 = math.degrees(math.acos(((length32**2)+(length31**2)-(length12**2))/(2*length32*length31)))

#prints results 
print("point1 angle: %.2f" % angle1)
print("point2 angle: %.2f" % angle2)
print("point3 angle: %.2f" % angle3)
print("length point1 - point2: %.2f" % length12)
print("length point2 - point3: %.2f" % length32)
print("length point1 - point3: %.2f" % length31)


