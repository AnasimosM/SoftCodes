# Clear Terminal

import platform
import subprocess

if platform.system() == "Windows":
    subprocess.run(["cls"], shell=True)
else:
    subprocess.run(["clear"], shell=True)
