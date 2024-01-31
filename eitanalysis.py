"""This script analyze the .eit data from the scio EIT equipment.
"""

"""example data: Frame_1.eit"""
exm = "data/Frame_1.eit"
with open(exm) as file:
    lines  = file.readlines()
    
l_data = lines[12]
data_list = l_data.split("\t")
print(len(data_list))
print(len(l_data))