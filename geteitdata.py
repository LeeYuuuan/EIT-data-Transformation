"""Get EIT physical data from measurement frames"""
import re
import random
from eitanalysis import get_eit_data
import numpy as np

def generate_file_name(idx):
    """
    generate file name as
    'setup_0000x.eit'
    """
    
    if idx < 100:
        return f"setup_000{idx}.eit"
    if idx < 1000:
        return f"setup_00{idx}.eit"
    if idx < 10000:
        return f"setup_0{idx}.eit"
    
i = 3
data_path = f"orignial_data/day{i}/"
mapping_name_path = f"Data_Collected_by_Experiment/original_data/file_name/day{i}.txt"
file_name_list = []
with open(mapping_name_path) as file:
    lines  = file.readlines()
    for j in range(len(lines)):
        temp = re.split(" |-", lines[j])
        idxl = float(temp[1])
        idxr = float(temp[2])
        idx = random.randint(idxl, idxr)
        file_name_list.append(generate_file_name(idx))

# print(file_name_list)

data_size = len(file_name_list)
one_day_data = np.zeros([data_size, 16, 16])
for count, file_name in enumerate(file_name_list):
    one_file_path = f"Data_Collected_by_Experiment/original_data/day{i}/{file_name}"
    one_day_data[count] = get_eit_data(one_file_path, i, count)

np.save(f"eit_physical_data/dday/day{i}.npy", one_day_data)

    