import os
import shutil

dataset_path = 'C:/PD/PD_Lab3/dataset'
output_path = 'C:/PD/PD_Lab3/newdataset'
os.makedirs(output_path, exist_ok=True)

for root, dirs, files in os.walk(dataset_path):
    for filename in files:
        class_label = os.path.basename(root)
        new_filename = f"{class_label}_{filename}"
        src_path = root + '/' + filename
        dst_path = output_path + '/' + new_filename        
        shutil.copy(src_path, dst_path)