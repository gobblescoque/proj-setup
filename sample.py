import argparse
import os

def create_proj():
	"""
	Create a basic file structure for a basic Python project using the src
	layout. Creates a 'hello world' template.
	"""
	folders = ['docs', 'src', 'tests']
	proj_name = str(input("Enter the project name: "))

	for folder in folders:
		os.system(f'mkdir $PWD/{folder}')
	os.system(f'mkdir $PWD/src/{proj_name}')
	os.system(f'touch $PWD/src/{proj_name}/__init__.py')
	os.system(f'touch $PWD/src/{proj_name}/sample.py')

	file = open(f"./src/{proj_name}/sample.py", "r+")
	file.write(f'print("Hello, World!")')
	file.close()