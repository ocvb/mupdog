
from distutils import extension
from fileinput import filename
import os
import signal
import argparse
from updog.utils.path import process_files

base_dir = os.path.abspath(os.getcwd())

directory_files = process_files(os.scandir(base_dir), base_dir)


for file in directory_files:
    (filename, extension) = os.path.splitext(file['name'])
    print(file['name'][-3:])
