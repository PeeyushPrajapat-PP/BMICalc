#bmi calculator
height_feet = float(input('please enter your height in feet: '))
height_inch = float(input('please enter your inches: '))
weight = float(input('please enter you weight in kg: '))

height_feet_meters = height_feet / float(3.281)
height_inch_meters = height_inch / float(39.37)

height_meters = height_feet_meters + height_inch_meters
# 1 foot = 0.3048m
# 1 inch = 0.0254m


bmi = weight / (height_meters  ** 2)

print('your bmi is', bmi )

print('end of program')
input('press any key to close.')