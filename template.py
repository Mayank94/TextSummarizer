# here will write all the logic of our code
import os
from pathlib import Path
import logging  

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# the logging format is time and messages


project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",           # this will help in deployement
    f"src/{project_name}/__init__.py",      # these list of files and each file being initialised is done so that we can import diff parts of this project in other files
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",      # we will write the utilities
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py", # contains training and testing pipelines
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",

]


for filepath in list_of_files:
    filepath = Path(filepath)       # this will detect the os and change the path format accordingly
    filedir, filename = os.path.split(filepath)  #splits the folder and file names

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # new empty file will be created only when we either don't have a file at that filepath
        # or the file at that file path is empty
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} already exists")
