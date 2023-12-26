import os
import subprocess

cmd = 'pyinstaller --onefile --add-data="templates;templates" --add-data="static;static" __main__.py'
code = subprocess.run(cmd, shell=True)

if code.returncode == 0:
    os.replace("dist/__main__.exe", "mupdog.exe")
