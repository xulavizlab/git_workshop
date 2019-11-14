import os

thisdir = os.getcwd()
files = os.listdir(thisdir)
files_to_exe = [file for file in files if ".py" in file and file != "searchAndExecute.py"]

for file in files_to_exe:
    os.system('python3 ' + file)
