import os.path
from pathlib import Path
from typing import Dict
import PySimpleGUI as sg

import pandas as pd

def clear_input(values,windows):
    for key in values:
        windows[key]('')
    return None

"""def data_frame(values,file_name):
    df = pd.DataFrame()
    new_record = pd.DataFrame(values, index=[0])
    df = pd.concat([df, new_record], ignore_index=True).T
    base_dir = Path(__file__).parent
    
    path = os.path.join(base_dir, "Office use only")
    os.makedirs(path,exist_ok = True)
    dir_path = os.path.abspath("Office use only")
    New_path=os.path.join(dir_path,f"{file_name+'.csv'}")
    return df.to_csv(New_path)"""

"""def Upload_files(Folder_name):
    base_path = os.path.dirname(__file__)
    path = os.path.join(base_path, f"{Folder_name}")
    return os.makedirs(path,exist_ok = True)"""


def Upload_files(Folder_name):
    base_dir = Path(__file__).parent
    path = os.path.join(base_dir, "Complete")
    os.makedirs(path, exist_ok=True)
    dir_path = os.path.abspath("Complete")
    New_path = os.path.join(dir_path, f"{Folder_name}")
    os.makedirs(New_path, exist_ok=True)
    return str(New_path)


def data_frame(values,file_name):
    df = pd.DataFrame()
    new_record = pd.DataFrame(values, index=[0])
    df = pd.concat([df, new_record], ignore_index=True).T
    dir_path = Upload_files("Office use only")
    New_path = os.path.join(dir_path, f"{file_name + '.csv'}")
    return df.to_csv(New_path)


