"""This script analyze the .eit data from the scio EIT equipment.
"""

"""example data: Frame_1.eit"""
import numpy as np
# exm = "data/setup_00001.eit"
def get_eit_data(exm, day, count):
    
    vol = np.zeros([16, 16])

    with open(exm) as file:
        lines  = file.readlines()
        i= 19
        # print(float(lines[19].split("\t")))
        while i < 51:
            line_data = lines[i].split("\t")
            
            for j in range(0, len(line_data), 2):
                vol[(i-19)//2, j//2] = float(line_data[j])
            i += 2
        # print(vol)
        np.save(f"eit_physical_data/vol_day{day}_{count}.npy", vol)
    return vol
        

