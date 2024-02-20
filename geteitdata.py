"""Get EIT physical data from measurement frames"""
import re
import random

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
    
i = 1
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
        file_name = generate_file_name(idx)
        file_name_list.append(file_name)

print(file_name_list)