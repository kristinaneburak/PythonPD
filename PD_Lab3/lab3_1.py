import os
import csv

dataset_path = 'C/PD/PD_Lab3/dataset'
output_csv = 'annotation.csv'

with open(output_csv, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Absolute path', 'Relative path', 'Class label'])

    for root, dirs, files in os.walk(dataset_path):
        for filename in files:
            abs_path = os.path.join(root, filename)
            rel_path = os.path.relpath(abs_path, start=dataset_path)
            class_label = os.path.basename(root)
            csv_writer.writerow([abs_path, rel_path, class_label])
