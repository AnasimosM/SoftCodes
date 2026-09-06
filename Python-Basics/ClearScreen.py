# Clear Terminal

import platform
import subprocess


def clearscreen():
    if platform.system() == "Windows":
        subprocess.run(["cls"], shell=True)
    else:
        subprocess.run(["clear"], shell=True)
