import math #import library
#User input the nescesary data
num_items = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))
#operations wuth the data
num_boxes = math.ceil(num_items / items_per_box)
#return data to the user
print(f"For {num_items} items, packing {items_per_box} in each box, you will need {num_boxes} boxes.")