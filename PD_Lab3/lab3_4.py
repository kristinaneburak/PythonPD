import os
import random

def get_next_instance(class_label, dataset_path):
    if not hasattr(get_next_instance, "instances"):
        instances = []

        for root, dirs, files in os.walk(dataset_path):
            if os.path.basename(root) == class_label:
                instances.extend([os.path.join(root, filename) for filename in files])

        random.shuffle(instances)

        get_next_instance.instances = instances

    if get_next_instance.instances:
        return get_next_instance.instances.pop()
    else:
        return None

class_label = 'brand_words'
dataset_path = ':C/PD/PD_Lab3/dataset'

for _ in range(10):
    next_instance = get_next_instance(class_label, dataset_path)

    if next_instance:
        print(f"Следующий экземпляр класса {class_label}: {next_instance}")
    else:
        print(f"Все экземпляры класса {class_label} закончились.")
