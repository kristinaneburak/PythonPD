import os
import shutil
import random

dataset_path = 'C:/PD/PD_Lab3/dataset'
output_path = 'C:/PD/PD_Lab3/randomdataset'
os.makedirs(output_path, exist_ok=True)

for root, dirs, files in os.walk(dataset_path):
    for filename in files:
        random_number = random.randint(0, 10000)
        new_filename = f"{random_number}.txt"
        src_path = os.path.join(root, filename)
        dst_path = os.path.join(output_path, new_filename)
        shutil.copy(src_path, dst_path)
