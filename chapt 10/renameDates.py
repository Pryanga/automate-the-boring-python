import os, re
import shutil


folder_path = './chapt 10 files'

# us_pattern = MM-DD-YYYY

us_pat = re.compile(r"(.*)(([0][1-9])|1[0-2])(-)(([0-2]\d)|3[0-1])(-\d{4}.*)")



for filename in os.listdir(folder_path):
    results_group = us_pat.search(filename)
    long_filename = os.path.join(folder_path, filename)
    #get the the file path of the filename in relative to the folder_path
    if results_group:
        new_name= re.sub(us_pat, r'\1\5\4\2\7', filename)
        new_name = os.path.join(os.path.dirname(long_filename), new_name)
        shutil.move(long_filename, new_name)
        print('A file has been renamed')


print('Has run over all the files in the given folder')