# To access the math library and do the functions sqrt and pow
import math

# For the coordinates of sub one.
x1 = float(input("Enter x1: ") )
y1 = float(input("Enter y1: ") )
# For the coordinates of sub two.
x2 = float(input("Enter x2: ") )
y2 = float(input("Enter y2: ") )

# The difference of sub one and sub two x.
distancex = (x2 - x1)
# The difference if sub one and sub two y.
distancey = (y2 - y1)

# The formula of the total distance of the two coordinates given.
distance = math.sqrt(math.pow(distancex, 2) + math.pow(distancey, 2))
# The output.
print("The total distance is: ", distance)


# Because it is faster than to type it manually. Like from you can see I dont need to type everythng manual because the variables are taking care of it.