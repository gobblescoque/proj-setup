import argparse
import os

folders = ['docs', 'src', 'tests']

proj_name = str(input("Enter the project name: "))

for folder in folders:
	os.system('mkdir $PWD/' +  folder)

os.system('mkdir $PWD/src/' + proj_name)