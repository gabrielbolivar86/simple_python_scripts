import math

tire_width = float(input("Enter the width of the tire in mm (ex 205): "))
tire_aspect = float(input("Enter the aspect ratio of the tire (ex 60): "))
tire_diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))
pi = math.pi
w = float(tire_width)
a = float(tire_aspect)
d = float(tire_diameter)
v = pi*w**2*a*(w*a+2.540*d)/10000000000
print(f'The approximate volume is {v} liters')