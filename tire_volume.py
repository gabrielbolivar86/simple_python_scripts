#calculate the volume of a tire and storage it on TXT document
#Libraries
import math
from datetime import date
#1st get the data necesary to calculate the tire volume
# tire_width = float(input("Enter the width of the tire in mm (ex 205): "))
# tire_aspect = float(input("Enter the aspect ratio of the tire (ex 60): "))
# tire_diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

#comment the variables of the line 6 to 8 and uncomment 11 to 16 for debuging
tire_width = 185 
print (f"Enter the width of the tire in mm (ex 205): {tire_width}")
tire_aspect = 50
print (f"Enter the aspect ratio of the tire (ex 60): {tire_aspect}")
tire_diameter = 14
print (f"Enter the diameter of the wheel in inches (ex 15): {tire_diameter}")

pi = math.pi

#2nd set new variables in order to apply them to the formula that calculates the volume
w = float(tire_width)
a = float(tire_aspect)
d = float(tire_diameter)
#3rd calculate the tire volume with the formula
v = format(pi*w**2*a*(w*a+2.540*d)/10000000000, '.2f' )

#4th Return data to the user
print(f'The approximate volume is {v} liters')
#From here starts the 2nd week prove
#1st define today on a variable
current_date = date.today()
print (current_date)
#2nd convert the data to storage into string
current_date_str = str(current_date)
tire_width_str = str(tire_width)
tire_aspect_str = str(tire_aspect)
tire_diameter_str = str(tire_diameter)
volume_str = str(v)
#3nd set a variable with the information to storage
data_to_storage = ("|  " + current_date_str +"  |  "+ tire_width_str +"  |   "+ tire_aspect_str +"   |    "+ tire_diameter_str+"    |   "+ volume_str + "   |")
#4th open file that we will use as a database
file_object = open("volume.txt", 'a')
file_object.write(str(data_to_storage))
file_object.write('\n')
file_object.close()