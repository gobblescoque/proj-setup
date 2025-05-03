import argparse
import os

folders = ['docs', 'src', 'tests']

proj_name = str(input("Enter the project name: "))

for folder in folders:
	os.system(f'mkdir $PWD/{folder}')
os.system(f'mkdir $PWD/src/{proj_name}')
os.system(f'touch $PWD/src/{proj_name}/__init__.py')
os.system(f'touch $PWD/src/{proj_name}/sample.py')

# sample_text = "Hello, World!"

# Something is broken here, fix later
os.system(f"echo 'print("Hello, World!")' >> $PWD/src/{proj_name}/sample.py")