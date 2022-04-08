"""Iterate a directory"""
import glob
import os
from pathlib import Path


# Use os.walk()
directory = r"path"
for root, dirs, files in os.walk(directory):
    for f in files:
        print(os.path.join(root, f))

# Use glob.glob()
directory = r"path\**\*.*"
filelist = glob.glob(directory, recursive=True)
for f in filelist:
    print(f)

# Use Path().rglob()
directory = r"path"
filelist = Path(directory).rglob("**\*.*")
for f in filelist:
    print(f)
