# -*- coding: utf-8 -*-
"""
Created on Wed May 29 10:35:51 2024

@author: Emma
"""

                
import os
import shutil

def copy_xlsx_files(source_dir, target_dir):
    # Ensure the target directory exists
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Iterate through the files in the source directory
    for filename in os.listdir(source_dir):
        # Check if the file is a CSV file
        if filename.endswith('.xlsx'):
            # Construct full file path
            source_file = os.path.join(source_dir, filename)
            target_file = os.path.join(target_dir, filename)
            # Copy the file to the target directory
            shutil.copy(source_file, target_file)
            print(f"Copied {filename} to {target_dir}")

# Example usage
source_dir = r"C:\Users\Emma\Desktop\Frequented\Dresden University\Neoma Exchange\CLASSES\Financial Decisions under Uncertainty\Session 10"
target_dir = r"C:\Users\Emma\Desktop\Python with Oga Femi"

copy_xlsx_files(source_dir, target_dir)
