import typer
import os
import subprocess
from typing_extensions import Annotated

def srclayout(
	proj_name: Annotated[str, typer.Argument(help="Enter a name for the \
											 project")] = "",
	cli: Annotated[bool, typer.Option(help="Sets up project for a cli app")] = False

):
	"""
	Create a basic file structure for a basic Python project using the src
	layout. Creates a 'hello world' template.
	"""

	folders = ['docs', 'src', 'tests']
	main_file = 'sample.py'
	main_file_name = main_file.replace(".py", "")

	# Sets up the basic folder structure
	for folder in folders:
		os.system(f'mkdir $PWD/{folder}')

	# Consider refactoring into a different function for dir/file creation
	os.system(f'mkdir $PWD/src/{proj_name}')
	os.system(f'touch $PWD/src/{proj_name}/__init__.py')
	os.system(f'touch $PWD/src/{proj_name}/__main__.py')
	os.system(f'touch $PWD/src/{proj_name}/{main_file}')

	# Creates the sample source file
	mod_contents = ['import typer\n',
					'from typing_extensions import Annotated\n',
					'\n',
	                'def hello(\n'
	                '          to_print: Annotated[str, typer.Argument'\
	                '(help="String to print to console")] = ""\n',
	                '):\n',
					'    print(to_print)']

	file = open(f"./src/{proj_name}/{main_file}", "r+")

	for line in mod_contents:
		file.write(line)

	file.close()

	# Creation of the boilerplate for a CLI project
	if cli:
		subprocess.run(["touch", "cli.py"], cwd=f'./src/{proj_name}/')

		main_contents = ['if __name__ == "__main__":\n',
		                 f'    from {proj_name}.cli import app\n'
		                 '    app()'
						]

		cli_contents = ['import typer\n',
						'\n',
						f'from .{main_file_name} import hello\n',
						'\n',
						'app = typer.Typer()\n',
						'app.command()(hello)\n',
						'\n',
						'if __name__ == "__main__":\n',
						'    app()'
						]

		file = open(f"./src/{proj_name}/cli.py", "r+")

		for line in cli_contents:
			file.write(line)
		file.close()

		file = open(f"./src/{proj_name}/__main__.py", "r+")

		for line in main_contents:
			file.write(line)
		file.close()



	# Creates the pyproject.toml
	os.system(f'touch $PWD/pyproject.toml')

	if cli:
		project_contents = ['[project]\n',
							'name = "hello"\n',
							'version = "0.0"\n',
							'dependencies = [typer >= 0.15.3]\n',
							'\n',
							'[project.scripts]\n',
							'hello = "hello.cli:app"\n',
							'\n',
							'[project.entry-points."pipx.run"]\n',
							'hello = "hello.cli:app\n',
							'[build-system]\n',
							'\n',
							'requires = ["hatchling >= 1.27"]\n',
							'build-backend = "hatchling.build"\n'
	                        ]
	else:
		project_contents = ['[project]\n',
							'name = "hello"\n',
							'version = "0.0"\n',
							'dependencies = []\n',
		                   ]

	file = open(f"pyproject.toml", "r+")
	for line in project_contents:
		file.write(line)
	file.close()

