import os

import sys

import logging

log_dir="log"

os.makedirs(log_dir,exist_ok=True)

file_path=os.path.join(log_dir,"logging.log")


formatter="[%(asctime)s - %(name)s - %(levelname)s -%(message)s]"

logging.basicConfig(
    level=logging.INFO,

    format=formatter,


    handlers=[
        logging.FileHandler(file_path),
        logging.StreamHandler(sys.stdout)
    ]


)


logger =logging.getLogger("Health_insurance")

