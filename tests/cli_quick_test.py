import os
import subprocess

# Reinstall CLI tool and empty the testing folder
subprocess.run(["pipx", "uninstall", "proj_setup"])
subprocess.run(["pipx", "install", ".."])
subprocess.run(["rm", "-rf", "testing"])
subprocess.run(["mkdir", "testing"])
subprocess.run(["layout", "--cli", "testeroni"], cwd=r'testing')