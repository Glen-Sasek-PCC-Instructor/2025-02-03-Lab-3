radius = 0.0
height = 0.0
volumeCubicInches = 0.0
PI = 3.14159

radius = float(input("Enter inches radius of cylinder: "))
height = float(input("Enter inches height of cylinder: "))

volumeCubicInches = PI * (radius ** 2) * height

print('The volume is {:.3f} cubic inches'.format(volumeCubicInches))

