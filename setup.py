import os
import sys
from cx_Freeze import setup, Executable

# asset path definition
path = './assets'
asset_complete_list = []

# walk through all subdirectories and files
for root, dirs, files in os.walk(path):
    for file in files:
        full_path = os.path.join(root, file).replace('\\', '/')
        asset_complete_list.append((full_path, full_path))  # (source, destination)

# choose base depending on platform
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # hides the console window

# define executable with custom name and icon
executables = [
    Executable(
        script='main.py',
        target_name='Neon Skyline.exe',  # custom exe name
        icon='icon.ico'  # path to your .ico file
    )
]

# assets and packages import
files = {'include_files': asset_complete_list, 'packages': ['pygame']}

setup(
    name='Neon Skyline',
    version='1.0',
    description='Sidescrolling vessel shooter',
    options={'build_exe': files},
    executables=executables
)

# to build, use:
# python -m setup build

# to generate MSI installer, use:
# python setup.py bdist_msi
