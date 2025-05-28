import os

from pathlib import Path

# file="src/components/cm.py"

# folder, file=os.path.split(file)

# print(folder)

# os.makedirs(folder,exist_ok=True)

# with open(folder,"w") as file:
#     pass

print(os.path.exists("params.yaml"))

print(os.path.getsize("src/healt_insurance"))