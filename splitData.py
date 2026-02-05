import os
import random
import shutil
from itertools import islice

outputFolderPath = "Dataset/SplitData"
inputFolderPath = "Dataset/all"
splitRatio = {"train": 0.7, "val": 0.2, "test": 0.1}
classes = ["fake", "real"]

try:
    shutil.rmtree(outputFolderPath)
except OSError:
    pass  # Ignore errors if the folder doesn't exist

os.makedirs(f"{outputFolderPath}/train/images", exist_ok=True)
os.makedirs(f"{outputFolderPath}/train/labels", exist_ok=True)
os.makedirs(f"{outputFolderPath}/val/images", exist_ok=True)
os.makedirs(f"{outputFolderPath}/val/labels", exist_ok=True)
os.makedirs(f"{outputFolderPath}/test/images", exist_ok=True)
os.makedirs(f"{outputFolderPath}/test/labels", exist_ok=True)

# Get file names
listNames = os.listdir(inputFolderPath)

# Filter out non-JPG or TXT files and remove extensions
uniqueNames = set(name.split('.')[0] for name in listNames if name.endswith(('.jpg', '.txt')))
uniqueNames = list(uniqueNames)

# Shuffle
random.shuffle(uniqueNames)

# Split counts
lenData = len(uniqueNames)
lenTrain = int(lenData * splitRatio['train'])
lenVal = int(lenData * splitRatio['val'])
lenTest = lenData - (lenTrain + lenVal)

# Split data
lengthToSplit = [lenTrain, lenVal, lenTest]
Input = iter(uniqueNames)
Output = [list(islice(Input, elem)) for elem in lengthToSplit]

print(f'Total Images: {lenData} \nSplit: {len(Output[0])} {len(Output[1])} {len(Output[2])}')

# Copy files
sequence = ['train', 'val', 'test']
for i, out in enumerate(Output):
    for fileName in out:
        imagePath = f'{inputFolderPath}/{fileName}.jpg'
        labelPath = f'{inputFolderPath}/{fileName}.txt'
        if os.path.exists(imagePath):
            shutil.copy(imagePath, f'{outputFolderPath}/{sequence[i]}/images/{fileName}.jpg')
        if os.path.exists(labelPath):
            shutil.copy(labelPath, f'{outputFolderPath}/{sequence[i]}/labels/{fileName}.txt')

print("Split Process Completed...")

# Create data.yaml file
dataYaml = f"""path: ../Data
train: ../train/images
val: ../val/images
test: ../test/images

nc: {len(classes)}
names: {classes}
"""

with open(f"{outputFolderPath}/data.yaml", 'w') as f:
    f.write(dataYaml)

print("Data.yaml file Created...")