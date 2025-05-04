import typer
import os
from typing_extensions import Annotated

def srclayout(
	proj_name: Annotated[str, typer.Argument(help="Enter a name for the project")] = ""
):
	"""
	Create a basic file structure for a basic Python project using the src
	layout. Creates a 'hello world' template.
	"""

	folders = ['docs', 'src', 'tests']

	# Sets up the basic folder structure
	for folder in folders:
		os.system(f'mkdir $PWD/{folder}')

	os.system(f'mkdir $PWD/src/{proj_name}')
	os.system(f'touch $PWD/src/{proj_name}/__init__.py')
	os.system(f'touch $PWD/src/{proj_name}/sample.py')

	# Creates the sample source file
	file = open(f"./src/{proj_name}/sample.py", "r+")
	file.write(f'print("Hello, World!")')
	file.close()

	# Creates the pyproject.toml

	contents = ['[project]\n',
				'version = "0.0"\n',
				'dependencies = []\n',
				'\n',
				'[project.scripts]\n',
				'hello = "hello.cli:app"\n',
				'\n',
				'[project.entry-points."pipx.run"]\n',
				'hello = "hello.cli:app\n',
				'[build-system]\n',
				'\n',
				'requires = ["hatchling >= 1.27"]\n',
				'build-backend = "hatchling.build\n'
	]

	os.system(f'touch $PWD/pyproject.toml')

	file = open(f"pyproject.toml", "r+")
	for line in contents:
		file.write(line)
	file.close()
