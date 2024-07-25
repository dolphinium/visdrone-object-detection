import os
from pathlib import Path
from PIL import Image
from tqdm import tqdm

def visdrone2yolo(dir):    
    def convert_box(size, box):
        # Convert VisDrone box to YOLO xywh box
        dw = 1. / size[0]
        dh = 1. / size[1]
        return (box[0] + box[2] / 2) * dw, (box[1] + box[3] / 2) * dh, box[2] * dw, box[3] * dh

    # Make labels directory
    (dir / 'labels_v2').mkdir(parents=True, exist_ok=True)

    # Iterate over each annotation file
    pbar = tqdm((dir / 'annotations').glob('*.txt'), desc=f'Converting {dir}')
    for f in pbar:
        img_size = Image.open((dir / 'images' / f.name).with_suffix('.jpg')).size
        lines = []
        
        with open(f, 'r') as file:  # Read annotation.txt
            for row in [x.split(',') for x in file.read().strip().splitlines()]:
                # Ignore 'ignored regions' class and certain classes 
                # ignore 0-3-7-8 --> 0:ignored regions 3: bicycle 7:tricycle 8:awning tricycle
                if row[4] == 0 or row[5] in ["0", '3', '7', '8']:  
                    continue

                # Combine pedestrian and people classes into a single class
                if row[5] in ['1', '2']:  # 1: pedestrian or 2: people
                    cls = 0     # 0 = ped/people

                # Combine car and van classes into a single class
                elif row[5] in ['4', '5',"6","9","10"]:  # car, van, truck, bus, motor
                    cls = 1     # 1 = vehicle


                # Convert box coordinates
                box = convert_box(img_size, tuple(map(int, row[:4])))
                lines.append(f"{cls} {' '.join(f'{x:.6f}' for x in box)}\n")

        # Write to label file
        with open(str(f).replace(f'{os.sep}annotations{os.sep}', f'{os.sep}labels_v2{os.sep}'), 'w') as fl:
            fl.writelines(lines)

# Download
dir = Path("../data/VisDrone")

# Convert
for d in ['VisDrone2019-DET-train', 'VisDrone2019-DET-val', 'VisDrone2019-DET-test-dev']:
    visdrone2yolo(dir / d)  # convert VisDrone annotations to YOLO labels